# product-management-api-146572-146606

Products Backend — FastAPI service exposing CRUD endpoints for Product resources (id, name, price, quantity).

## Quick Start

1. Create and configure environment
   - Copy `.env.example` to `.env` in `products_backend/` and adjust values if needed.

2. Install dependencies
   - Use Python 3.11+
   - `pip install -r products_backend/requirements.txt`

3. Run (development)
   - `uvicorn products_backend.src.api.main:app --reload --host 0.0.0.0 --port 3001`

4. API Docs
   - Swagger UI: http://localhost:3001/docs
   - OpenAPI JSON: http://localhost:3001/openapi.json

## API Summary

- Health: `GET /`
- Products (prefix `/api/v1/products`)
  - `GET /api/v1/products` — List products
  - `POST /api/v1/products` — Create a product
  - `GET /api/v1/products/{product_id}` — Get product by ID
  - `PUT /api/v1/products/{product_id}` — Update product by ID
  - `DELETE /api/v1/products/{product_id}` — Delete product by ID

## Architecture

- `schemas/` — Pydantic models for request/response validation
- `repositories/` — Data access layer (in-memory by default; replaceable)
- `services/` — Business logic layer
- `routes/` — API endpoints
- `core/` — App config and OpenAPI docs helpers

This service is designed with clean separation of concerns and production readiness in mind. Future extensions can swap the repository with a database-backed implementation without changing the API layer.

## Theme

The project references the "Ocean Professional" theme (blue & amber accents) for future documentation or UI alignment.
