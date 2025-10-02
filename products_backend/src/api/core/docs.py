def get_openapi_tags():
    """
    PUBLIC_INTERFACE
    Return OpenAPI tags for organizing endpoints.
    """
    return [
        {
            "name": "Health",
            "description": "Service health and metadata endpoints.",
        },
        {
            "name": "Products",
            "description": "CRUD operations for product resources.",
        },
    ]


def get_app_description() -> str:
    """
    PUBLIC_INTERFACE
    Return the application description including theme guidance.

    The service follows the 'Ocean Professional' theme (blue & amber accents).
    This note serves as a reminder for future documentation/frontends to align
    visuals accordingly.
    """
    return (
        "A REST API for managing products (id, name, price, quantity). "
        "Designed with a clean architecture and production readiness. "
        "Theme: Ocean Professional — Blue (#2563EB) & Amber (#F59E0B) accents."
    )
