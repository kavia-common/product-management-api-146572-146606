"""
FastAPI application entrypoint for Products Backend.

This app exposes REST API endpoints to manage Product resources with CRUD operations.
It is structured with clear layers (schemas, repository, service, routes) for maintainability
and production readiness. The API includes OpenAPI metadata, tags, and CORS configuration.

Environment:
- The app reads config via pydantic BaseSettings (see core/config.py).
- Do not hardcode secrets; use environment variables (see .env.example).

WebSocket:
- Not used in this service.

OpenAPI Docs:
- Styled/organized with tags. Future UI theming should follow the "Ocean Professional" theme.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.products import router as products_router
from .core.config import settings
from .core.docs import get_openapi_tags, get_app_description

# Create FastAPI app with metadata
app = FastAPI(
    title="Products Backend API",
    description=get_app_description(),
    version="1.0.0",
    contact={
        "name": "Products Backend",
        "url": "https://example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=get_openapi_tags(),
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"], summary="Health Check", description="Returns service status.")
def health_check():
    """
    PUBLIC_INTERFACE
    Return the health status of the service.

    Returns:
        dict: A simple status message indicating the service is up.
    """
    return {"status": "ok", "service": "products-backend", "version": app.version}


# Register routers
app.include_router(products_router, prefix="/api/v1")
