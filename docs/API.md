# API Documentation

## Overview

The Crésus API is a RESTful API built with FastAPI. It provides comprehensive endpoints for portfolio management, market data, analysis, and AI-powered recommendations.

Base URL: `http://localhost:8000/api/v1`

## Authentication

Currently, the API does not require authentication. Authentication will be added in Phase 2.

## Endpoints

### Portfolios

#### List Portfolios
```http
GET /api/v1/portfolios/
```

Response:
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "name": "My Portfolio",
    "type": "real",
    "currency": "USD",
    "initial_capital": 10000.0,
    "is_active": true,
    "created_at": "2025-01-01T00:00:00",
    "updated_at": "2025-01-01T00:00:00"
  }
]
```

#### Create Portfolio
```http
POST /api/v1/portfolios/
Content-Type: application/json

{
  "user_id": "uuid",
  "name": "My Portfolio",
  "type": "virtual",
  "currency": "USD",
  "initial_capital": 10000.0
}
```

#### Get Portfolio
```http
GET /api/v1/portfolios/{portfolio_id}
```

#### Update Portfolio
```http
PATCH /api/v1/portfolios/{portfolio_id}
Content-Type: application/json

{
  "name": "Updated Name",
  "is_active": false
}
```

#### Delete Portfolio
```http
DELETE /api/v1/portfolios/{portfolio_id}
```

#### Get Portfolio Performance
```http
GET /api/v1/portfolios/{portfolio_id}/performance
```

Response:
```json
{
  "portfolio_id": "uuid",
  "total_value": 12500.0,
  "total_cost": 10000.0,
  "total_pnl": 2500.0,
  "total_return_percent": 25.0,
  "num_positions": 5
}
```

### Stocks

#### Get Stock Information
```http
GET /api/v1/stocks/{symbol}
```

Response:
```json
{
  "symbol": "AAPL",
  "name": "Apple Inc.",
  "sector": "Technology",
  "industry": "Consumer Electronics",
  "market_cap": 3000000000000,
  "current_price": 175.50,
  "previous_close": 174.20,
  "pe_ratio": 28.5
}
```

#### Get Stock Price
```http
GET /api/v1/stocks/{symbol}/price
```

#### Get Historical Data
```http
GET /api/v1/stocks/{symbol}/history?period=1mo&interval=1d
```

### Orders

#### List Orders
```http
GET /api/v1/orders/
```

#### Create Order
```http
POST /api/v1/orders/
Content-Type: application/json

{
  "portfolio_id": "uuid",
  "symbol": "AAPL",
  "side": "buy",
  "quantity": 10,
  "price": 175.50,
  "order_date": "2025-01-01T10:00:00",
  "notes": "Initial purchase"
}
```

### Recommendations

#### List Recommendations
```http
GET /api/v1/recommendations/
```

#### Generate Recommendations
```http
POST /api/v1/recommendations/generate
Content-Type: application/json

{
  "portfolio_id": "uuid"
}
```

### Sync

#### Sync with Notion
```http
POST /api/v1/sync/notion
```

#### Sync with Google Sheets
```http
POST /api/v1/sync/gsheet
```

#### Get Sync Status
```http
GET /api/v1/sync/status
```

## Error Responses

The API uses standard HTTP status codes:

- `200 OK` - Success
- `201 Created` - Resource created
- `204 No Content` - Success with no response body
- `400 Bad Request` - Invalid request
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

Error response format:
```json
{
  "detail": "Error message"
}
```

## Rate Limiting

API requests are rate limited to 60 requests per minute per IP address.

## Interactive Documentation

Swagger UI: `http://localhost:8000/docs`
ReDoc: `http://localhost:8000/redoc`
