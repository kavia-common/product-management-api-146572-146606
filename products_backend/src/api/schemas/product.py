from typing import Optional
from pydantic import BaseModel, Field, PositiveInt, confloat, constr


class ProductBase(BaseModel):
    """Shared fields for Product input/output models."""

    name: constr(strip_whitespace=True, min_length=1, max_length=200) = Field(
        ..., description="Product name"
    )
    price: confloat(ge=0, multiple_of=0.01) = Field(
        ..., description="Unit price of the product"
    )
    quantity: PositiveInt | int = Field(
        ..., ge=0, description="Available quantity in stock"
    )


class ProductCreate(ProductBase):
    """
    PUBLIC_INTERFACE
    Schema for creating a product.

    Fields:
        name (str): Name of the product, required.
        price (float): Non-negative, two decimal increments.
        quantity (int): Non-negative integer.
    """

    pass


class ProductUpdate(BaseModel):
    """
    PUBLIC_INTERFACE
    Schema for updating a product (partial update supported).

    Fields are optional; only provided fields will be updated.
    """

    name: Optional[constr(strip_whitespace=True, min_length=1, max_length=200)] = Field(
        None, description="Product name"
    )
    price: Optional[confloat(ge=0, multiple_of=0.01)] = Field(
        None, description="Unit price of the product"
    )
    quantity: Optional[PositiveInt | int] = Field(
        None, ge=0, description="Available quantity in stock"
    )


class Product(ProductBase):
    """
    PUBLIC_INTERFACE
    Schema representing a product resource with ID.
    """

    id: int = Field(..., description="Unique identifier of the product")

    class Config:
        from_attributes = True
