from typing import Dict, List
from threading import RLock

from ..schemas.product import Product, ProductCreate, ProductUpdate


class ProductNotFoundError(Exception):
    """Raised when a product is not found by the repository."""


class IProductsRepository:
    """
    PUBLIC_INTERFACE
    Interface for a Products repository.

    Methods:
        list() -> List[Product]
        get(product_id: int) -> Product
        create(payload: ProductCreate) -> Product
        update(product_id: int, payload: ProductUpdate) -> Product
        delete(product_id: int) -> None
        clear() -> None
    """

    def list(self) -> List[Product]:
        raise NotImplementedError

    def get(self, product_id: int) -> Product:
        raise NotImplementedError

    def create(self, payload: ProductCreate) -> Product:
        raise NotImplementedError

    def update(self, product_id: int, payload: ProductUpdate) -> Product:
        raise NotImplementedError

    def delete(self, product_id: int) -> None:
        raise NotImplementedError

    def clear(self) -> None:
        raise NotImplementedError


class InMemoryProductsRepository(IProductsRepository):
    """
    PUBLIC_INTERFACE
    In-memory implementation of the Products repository.

    Thread-safe for typical single-process deployments using a re-entrant lock.
    """

    def __init__(self) -> None:
        self._items: Dict[int, Product] = {}
        self._lock = RLock()
        self._seq = 0

    def _next_id(self) -> int:
        with self._lock:
            self._seq += 1
            return self._seq

    def list(self) -> List[Product]:
        with self._lock:
            return list(self._items.values())

    def get(self, product_id: int) -> Product:
        with self._lock:
            if product_id not in self._items:
                raise ProductNotFoundError(f"Product {product_id} not found")
            return self._items[product_id]

    def create(self, payload: ProductCreate) -> Product:
        with self._lock:
            new_id = self._next_id()
            product = Product(id=new_id, **payload.model_dump())
            self._items[new_id] = product
            return product

    def update(self, product_id: int, payload: ProductUpdate) -> Product:
        with self._lock:
            if product_id not in self._items:
                raise ProductNotFoundError(f"Product {product_id} not found")

            current = self._items[product_id]
            data = current.model_dump()

            updates = payload.model_dump(exclude_unset=True)
            data.update(updates)
            updated = Product(**data)
            self._items[product_id] = updated
            return updated

    def delete(self, product_id: int) -> None:
        with self._lock:
            if product_id not in self._items:
                raise ProductNotFoundError(f"Product {product_id} not found")
            del self._items[product_id]

    def clear(self) -> None:
        with self._lock:
            self._items.clear()
            self._seq = 0
