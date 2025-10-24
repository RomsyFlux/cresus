.PHONY: help install dev-install test lint format clean docker-build docker-up docker-down migrate

help:
	@echo "Crésus Development Commands:"
	@echo "  make install       - Install production dependencies"
	@echo "  make dev-install   - Install development dependencies"
	@echo "  make test          - Run tests"
	@echo "  make test-cov      - Run tests with coverage"
	@echo "  make lint          - Run linters"
	@echo "  make format        - Format code"
	@echo "  make clean         - Clean temporary files"
	@echo "  make docker-build  - Build Docker images"
	@echo "  make docker-up     - Start Docker services"
	@echo "  make docker-down   - Stop Docker services"
	@echo "  make migrate       - Run database migrations"

install:
	pip install -r requirements.txt

dev-install:
	pip install -r requirements-dev.txt
	pre-commit install

test:
	pytest tests/ -v

test-cov:
	pytest tests/ --cov=app --cov-report=html --cov-report=term

test-unit:
	pytest tests/unit -v

test-integration:
	pytest tests/integration -v

test-e2e:
	pytest tests/e2e -v

lint:
	black --check app/ tests/
	flake8 app/ tests/
	mypy app/
	isort --check-only app/ tests/

format:
	black app/ tests/
	isort app/ tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -rf htmlcov/
	rm -f .coverage

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

migrate:
	alembic upgrade head

migrate-create:
	alembic revision --autogenerate -m "$(msg)"

run-dev:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

run-worker:
	celery -A app.worker worker --loglevel=info

run-scheduler:
	celery -A app.worker beat --loglevel=info