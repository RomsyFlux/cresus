"""Integration tests for API endpoints."""

import pytest
from uuid import uuid4


def test_root_endpoint(client):
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data


def test_health_check(client):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_create_portfolio(client):
    """Test portfolio creation via API."""
    payload = {
        "user_id": str(uuid4()),
        "name": "API Test Portfolio",
        "type": "virtual",
        "currency": "USD",
        "initial_capital": 10000.0,
    }

    response = client.post("/api/v1/portfolios/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "API Test Portfolio"
    assert data["type"] == "virtual"


def test_list_portfolios(client):
    """Test listing portfolios via API."""
    response = client.get("/api/v1/portfolios/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
