# 🚀 Crésus Quick Start Guide

Welcome to Crésus! This guide will help you get started quickly.

## 📦 Repository

**GitHub:** https://github.com/RomsyFlux/cresus

## 🎯 What is Crésus?

Crésus is an AI-powered trading advisor that provides:
- 📊 Portfolio management and tracking
- 🤖 AI-driven trading recommendations
- 📈 Technical and fundamental analysis
- 🔄 Notion and Google Sheets integration
- 📰 Market news and sentiment analysis

## ⚡ Quick Setup (5 minutes)

### Prerequisites
```bash
# Required
- Python 3.11+
- Docker & Docker Compose
- Git

# Recommended
- VS Code or PyCharm
- Postman or Insomnia (for API testing)
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/RomsyFlux/cresus.git
cd cresus

# 2. Run setup script
chmod +x scripts/setup.sh
./scripts/setup.sh

# 3. Configure environment
cp .env.example .env
# Edit .env with your API keys (can be added later)

# 4. Start services
docker-compose up -d

# 5. Run the application
make run-dev
```

### Verify Installation

```bash
# Check health
curl http://localhost:8000/health

# Open API documentation
open http://localhost:8000/docs
```

## 🔑 Required API Keys

You'll need these API keys (get them as you build features):

1. **Notion API** - https://notion.so/my-integrations
   - Create an integration
   - Copy the Internal Integration Token

2. **Google Sheets API** - https://console.cloud.google.com
   - Create a project
   - Enable Google Sheets API
   - Create service account credentials

3. **OpenAI API** - https://platform.openai.com/api-keys
   - Sign up and create API key

4. **Anthropic Claude** - https://console.anthropic.com
   - Sign up and create API key

5. **Yahoo Finance** - No API key needed (uses yfinance library)

6. **Alpha Vantage** (Optional) - https://www.alphavantage.co/support/#api-key
   - Free tier: 500 requests/day

## 📝 First Steps

### 1. Create Your First Portfolio

```bash
curl -X POST "http://localhost:8000/api/v1/portfolios/" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "your-user-id",
    "name": "My First Portfolio",
    "type": "virtual",
    "currency": "USD",
    "initial_capital": 10000.0
  }'
```

### 2. Get Stock Information

```bash
curl "http://localhost:8000/api/v1/stocks/AAPL"
```

### 3. Record an Order

```bash
curl -X POST "http://localhost:8000/api/v1/orders/" \
  -H "Content-Type: application/json" \
  -d '{
    "portfolio_id": "your-portfolio-id",
    "symbol": "AAPL",
    "side": "buy",
    "quantity": 10,
    "price": 175.50,
    "order_date": "2025-01-01T10:00:00"
  }'
```

## 🧪 Testing

```bash
# Run all tests
make test

# Run specific test suite
pytest tests/unit
pytest tests/integration

# Check code coverage
make test-cov
```

## 📚 Documentation

- **API Docs:** http://localhost:8000/docs
- **Full Specifications:** [docs/SPECIFICATIONS.md](SPECIFICATIONS.md)
- **API Reference:** [docs/API.md](API.md)
- **Deployment Guide:** [docs/DEPLOYMENT.md](DEPLOYMENT.md)
- **Contributing:** [CONTRIBUTING.md](../CONTRIBUTING.md)

## 🐛 Troubleshooting

### Database Connection Error
```bash
# Check if PostgreSQL is running
docker-compose ps

# Restart database
docker-compose restart db

# Check logs
docker-compose logs db
```

### Redis Connection Error
```bash
# Restart Redis
docker-compose restart redis

# Test Redis connection
redis-cli ping
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.11+
```

## 🆘 Getting Help

- **Issues:** https://github.com/RomsyFlux/cresus/issues
- **Discussions:** https://github.com/RomsyFlux/cresus/discussions
- **Email:** support@cresus.ai

## 🗺️ Roadmap

- **Phase 1 (Months 1-3):** MVP with core features
- **Phase 2 (Months 4-6):** Advanced analytics and integrations
- **Phase 3 (Months 7-12):** Scale and optimization

See [GitHub Issues](https://github.com/RomsyFlux/cresus/issues) for detailed milestones.

## 📊 Project Status

- ✅ Project structure setup
- ✅ Core API endpoints defined
- ✅ Database models created
- 🔄 External integrations (in progress)
- 🔄 AI recommendation engine (in progress)
- ⏳ Technical analysis engine (planned)
- ⏳ Notion dashboard (planned)

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

```bash
# Create a feature branch
git checkout -b feature/amazing-feature

# Make your changes and commit
git commit -m "feat: add amazing feature"

# Push and create PR
git push origin feature/amazing-feature
```

## 📜 License

MIT License - see [LICENSE](../LICENSE) for details.

---

**Ready to build?** Start with [Week 1 Action Items](https://github.com/RomsyFlux/cresus/issues/6) 🚀
