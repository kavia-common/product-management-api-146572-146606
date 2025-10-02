from typing import List

from fastapi import APIRouter, Depends, Path, status

from ..schemas.product import Product, ProductCreate, ProductUpdate
from ..repositories.products_repository import InMemoryProductsRepository
from ..services.products_service import ProductsService

router = APIRouter(prefix="/products", tags=["Products"])


def get_service() -> ProductsService:
    """
    Dependency injection provider for ProductsService.
    In production, swap InMemoryProductsRepository with a persistent implementation.
    """
    repo = InMemoryProductsRepository()
    return ProductsService(repo)


@router.get(
    "",
    response_model=List[Product],
    status_code=status.HTTP_200_OK,
    summary="List products",
    description="Retrieve all products.",
    responses={200: {"description": "List of products returned successfully."}},
)
def list_products(service: ProductsService = Depends(get_service)):
    """
    PUBLIC_INTERFACE
    List all products.

    Returns:
        List[Product]: Array of product resources.
    """
    return service.list_products()


@router.get(
    "/{product_id}",
    response_model=Product,
    status_code=status.HTTP_200_OK,
    summary="Get a product",
    description="Retrieve a single product by its ID.",
    responses={
        200: {"description": "Product returned successfully."},
        404: {"description": "Product not found."},
    },
)
def get_product(
    product_id: int = Path(..., ge=1, description="ID of the product to retrieve"),
    service: ProductsService = Depends(get_service),
):
    """
    PUBLIC_INTERFACE
    Get a product by ID.

    Parameters:
        product_id (int): The ID of the product.

    Returns:
        Product: The requested product resource.
    """
    return service.get_product(product_id)


@router.post(
    "",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
    summary="Create a product",
    description="Create a new product.",
    responses={201: {"description": "Product created successfully."}},
)
def create_product(
    payload: ProductCreate, service: ProductsService = Depends(get_service)
):
    """
    PUBLIC_INTERFACE
    Create a new product.

    Parameters:
        payload (ProductCreate): The product fields to create.

    Returns:
        Product: The created product resource with ID.
    """
    return service.create_product(payload)


@router.put(
    "/{product_id}",
    response_model=Product,
    status_code=status.HTTP_200_OK,
    summary="Update a product",
    description="Update an existing product by its ID.",
    responses={
        200: {"description": "Product updated successfully."},
        404: {"description": "Product not found."},
    },
)
def update_product(
    product_id: int = Path(..., ge=1, description="ID of the product to update"),
    payload: ProductUpdate = None,
    service: ProductsService = Depends(get_service),
):
    """
    PUBLIC_INTERFACE
    Update an existing product by ID.

    Parameters:
        product_id (int): The ID of the product to update.
        payload (ProductUpdate): The fields to update.

    Returns:
        Product: The updated product resource.
    """
    return service.update_product(product_id, payload)


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a product",
    description="Delete a product by its ID.",
    responses={
        204: {"description": "Product deleted successfully."},
        404: {"description": "Product not found."},
    },
)
def delete_product(
    product_id: int = Path(..., ge=1, description="ID of the product to delete"),
    service: ProductsService = Depends(get_service),
):
    """
    PUBLIC_INTERFACE
    Delete a product by ID.

    Parameters:
        product_id (int): The ID of the product to delete.

    Returns:
        None
    """
    service.delete_product(product_id)
    # 204 No Content
    return None
