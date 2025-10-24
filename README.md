# 🦅 Crésus - AI Trading Advisor

> Intelligent market analysis, portfolio management, and AI-powered trading recommendations

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 📋 Overview

Crésus is an AI-powered trading advisory platform that provides comprehensive market analysis, portfolio management, and intelligent trading recommendations. The platform integrates real-time market data, advanced technical analysis, and AI-driven insights through a seamless Notion-based interface.

### Key Features

- **Portfolio Management**: Track unlimited real and virtual portfolios with detailed P&L analysis
- **AI-Powered Recommendations**: Get intelligent buy/sell/hold recommendations with confidence scores and reasoning
- **Market Analysis**: Real-time technical indicators, fundamental data, and sentiment analysis
- **Backtesting Engine**: Test strategies on historical data
- **Notion Integration**: No-code interface using Notion as primary UI
- **Multi-Platform**: Available via MCP (Model Context Protocol) and REST API

## 🏗️ Architecture

```
User Layer (Notion, Google Sheets, Slack)
          ↓
Integration Layer (APIs)
          ↓
Application Layer (FastAPI, MCP Server)
          ↓
Business Logic (Portfolio Manager, AI Engine, Analysis Engine)
          ↓
Data Layer (PostgreSQL, Redis, S3)
          ↓
External Data (Yahoo Finance, Trade Republic, Alpha Vantage)
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/RomsyFlux/cresus.git
cd cresus

# Copy environment variables
cp .env.example .env
# Edit .env with your API keys

# Start with Docker Compose
docker-compose up -d

# Or install locally
pip install -e .

# Run migrations
alembic upgrade head

# Start the server
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

## 📦 Project Structure

```
cresus/
├── app/                    # Application code
│   ├── api/               # API routes
│   ├── core/              # Core configuration
│   ├── models/            # Database models
│   ├── schemas/           # Pydantic schemas
│   ├── services/          # Business logic
│   ├── integrations/      # External API integrations
│   └── main.py           # Application entry point
├── tests/                 # Test suite
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/                  # Documentation
├── infrastructure/        # IaC (Terraform/Pulumi)
├── docker/               # Docker configurations
├── scripts/              # Utility scripts
└── alembic/             # Database migrations
```

## 🔧 Configuration

### Required API Keys

```bash
# .env file
NOTION_API_KEY=your_notion_key
GOOGLE_SHEETS_CREDENTIALS=path/to/credentials.json
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
DATABASE_URL=postgresql://user:pass@localhost:5432/cresus
REDIS_URL=redis://localhost:6379
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test suite
pytest tests/unit
pytest tests/integration
pytest tests/e2e

# Run linting
black .
flake8 .
mypy app/
```

## 📚 Documentation

- [Full Technical Specifications](docs/SPECIFICATIONS.md)
- [API Documentation](docs/API.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Contributing Guidelines](CONTRIBUTING.md)

## 🗺️ Roadmap

### Phase 1: MVP (Months 1-3) ✅
- [x] Project setup and infrastructure
- [ ] Core integrations (Notion, Google Sheets, Yahoo Finance)
- [ ] Portfolio management
- [ ] AI advisory engine
- [ ] Basic dashboard

### Phase 2: Enhancement (Months 4-6)
- [ ] Advanced analytics and backtesting
- [ ] Trade Republic integration
- [ ] News aggregation and sentiment analysis
- [ ] Custom AI agents

### Phase 3: Scale (Months 7-12)
- [ ] Performance optimization
- [ ] Multi-user support
- [ ] Advanced automation
- [ ] Mobile optimization

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [Notion API](https://developers.notion.com/) - Workspace integration
- [yfinance](https://github.com/ranaroussi/yfinance) - Market data
- [Claude](https://anthropic.com/) & [OpenAI](https://openai.com/) - AI capabilities

## 📞 Support

For questions and support:
- 📧 Email: support@cresus.ai
- 💬 Slack: [Join our community](#)
- 🐛 Issues: [GitHub Issues](https://github.com/RomsyFlux/cresus/issues)

## ⚠️ Disclaimer

Crésus is an advisory tool only. All recommendations are for informational purposes and should not be considered financial advice. Users trade at their own risk. Past performance does not guarantee future results.

---

Made with ❤️ by the Crésus Team