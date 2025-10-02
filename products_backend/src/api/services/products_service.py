from typing import List

from fastapi import HTTPException, status

from ..schemas.product import Product, ProductCreate, ProductUpdate
from ..repositories.products_repository import (
    IProductsRepository,
    ProductNotFoundError,
)


class ProductsService:
    """
    PUBLIC_INTERFACE
    Service layer for product operations.

    This layer encapsulates business rules and coordinates with the repository.
    """

    def __init__(self, repo: IProductsRepository) -> None:
        self.repo = repo

    def list_products(self) -> List[Product]:
        return self.repo.list()

    def get_product(self, product_id: int) -> Product:
        try:
            return self.repo.get(product_id)
        except ProductNotFoundError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=str(e)
            ) from e

    def create_product(self, payload: ProductCreate) -> Product:
        return self.repo.create(payload)

    def update_product(self, product_id: int, payload: ProductUpdate) -> Product:
        try:
            return self.repo.update(product_id, payload)
        except ProductNotFoundError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=str(e)
            ) from e

    def delete_product(self, product_id: int) -> None:
        try:
            self.repo.delete(product_id)
        except ProductNotFoundError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=str(e)
            ) from e
