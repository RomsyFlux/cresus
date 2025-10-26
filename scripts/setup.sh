#!/bin/bash
# Setup script for Crésus development environment

set -e

echo "🦅 Setting up Crésus development environment..."

# Check Python version
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
if (( $(echo "$PYTHON_VERSION < 3.11" | bc -l) )); then
    echo "❌ Python 3.11+ is required. Current version: $PYTHON_VERSION"
    exit 1
fi
echo "✅ Python $PYTHON_VERSION detected"

# Check Docker
echo "Checking Docker..."
if ! command -v docker &> /dev/null; then
    echo "⚠️  Docker is not installed. Install Docker to use containerized services."
else
    echo "✅ Docker detected"
fi

# Create virtual environment
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
pip install -r requirements-dev.txt
echo "✅ Dependencies installed"

# Install pre-commit hooks
echo "Installing pre-commit hooks..."
pre-commit install
echo "✅ Pre-commit hooks installed"

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "✅ .env file created. Please update it with your configuration."
else
    echo "✅ .env file already exists"
fi

# Check if Docker is running
if command -v docker &> /dev/null && docker info &> /dev/null; then
    echo "Starting Docker services..."
    docker-compose up -d db redis
    echo "✅ Docker services started"
    
    # Wait for database
    echo "Waiting for database to be ready..."
    sleep 5
    
    # Run migrations
    echo "Running database migrations..."
    alembic upgrade head
    echo "✅ Migrations completed"
else
    echo "⚠️  Docker is not running. Please start Docker and run 'docker-compose up -d'"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Update .env with your API keys"
echo "2. Run 'make run-dev' to start the development server"
echo "3. Visit http://localhost:8000/docs for API documentation"
echo ""
echo "Happy coding! 🚀"
