#!/bin/bash
# Test runner script

set -e

echo "🧪 Running tests..."

# Run linting
echo "Running linters..."
black --check app/ tests/
flake8 app/ tests/ --max-line-length=120 --extend-ignore=E203,W503
isort --check-only app/ tests/
mypy app/ --ignore-missing-imports

echo "✅ Linting passed"

# Run tests with coverage
echo "Running tests with coverage..."
pytest tests/ --cov=app --cov-report=html --cov-report=term --cov-report=xml -v

echo "✅ All tests passed"
echo ""
echo "📊 Coverage report generated at htmlcov/index.html"
