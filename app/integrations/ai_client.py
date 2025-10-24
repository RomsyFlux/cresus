"""AI service clients (OpenAI and Anthropic)."""

from typing import Dict, List, Optional
import openai
import anthropic

from app.core.config import settings
from app.core.logging import logger


class AIClient:
    """Client for AI services."""

    def __init__(self):
        # Initialize OpenAI
        if settings.OPENAI_API_KEY:
            openai.api_key = settings.OPENAI_API_KEY
            self.openai_client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        else:
            self.openai_client = None

        # Initialize Anthropic
        if settings.ANTHROPIC_API_KEY:
            self.anthropic_client = anthropic.Anthropic(
                api_key=settings.ANTHROPIC_API_KEY
            )
        else:
            self.anthropic_client = None

    async def generate_recommendation(
        self,
        symbol: str,
        analysis_data: Dict,
        provider: str = "openai",
    ) -> Dict:
        """Generate trading recommendation using AI."""
        prompt = self._build_recommendation_prompt(symbol, analysis_data)

        if provider == "openai" and self.openai_client:
            return await self._generate_with_openai(prompt)
        elif provider == "anthropic" and self.anthropic_client:
            return await self._generate_with_anthropic(prompt)
        else:
            raise ValueError(f"AI provider {provider} not available or not configured")

    async def _generate_with_openai(self, prompt: str) -> Dict:
        """Generate recommendation using OpenAI."""
        try:
            response = self.openai_client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert financial advisor providing trading recommendations.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
            )

            content = response.choices[0].message.content
            return self._parse_recommendation(content)
        except Exception as e:
            logger.error("OpenAI API error", error=str(e))
            raise

    async def _generate_with_anthropic(self, prompt: str) -> Dict:
        """Generate recommendation using Anthropic Claude."""
        try:
            response = self.anthropic_client.messages.create(
                model=settings.ANTHROPIC_MODEL,
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}],
            )

            content = response.content[0].text
            return self._parse_recommendation(content)
        except Exception as e:
            logger.error("Anthropic API error", error=str(e))
            raise

    def _build_recommendation_prompt(self, symbol: str, analysis_data: Dict) -> str:
        """Build prompt for AI recommendation."""
        return f"""
Analyze the following stock and provide a trading recommendation:

Symbol: {symbol}
Current Price: ${analysis_data.get('current_price', 'N/A')}
Market Cap: ${analysis_data.get('market_cap', 'N/A')}
P/E Ratio: {analysis_data.get('pe_ratio', 'N/A')}
RSI: {analysis_data.get('rsi', 'N/A')}
MACD: {analysis_data.get('macd', 'N/A')}
50-day MA: ${analysis_data.get('ma_50', 'N/A')}
200-day MA: ${analysis_data.get('ma_200', 'N/A')}

Provide your recommendation in the following JSON format:
{{
  "action": "buy|sell|hold",
  "confidence_score": 0.0-1.0,
  "target_price": 0.00,
  "stop_loss": 0.00,
  "time_horizon": "short-term|medium-term|long-term",
  "reasoning": "Detailed explanation of your recommendation"
}}
"""

    def _parse_recommendation(self, content: str) -> Dict:
        """Parse AI response into structured recommendation."""
        import json

        try:
            # Try to extract JSON from response
            start = content.find("{")
            end = content.rfind("}") + 1
            if start != -1 and end > start:
                json_str = content[start:end]
                return json.loads(json_str)
            else:
                # Fallback if no JSON found
                return {
                    "action": "hold",
                    "confidence_score": 0.5,
                    "reasoning": content,
                }
        except json.JSONDecodeError:
            logger.warning("Failed to parse AI response as JSON")
            return {
                "action": "hold",
                "confidence_score": 0.5,
                "reasoning": content,
            }
