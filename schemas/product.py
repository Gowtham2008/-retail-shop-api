from pydantic import BaseModel, Field


class Products(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0)
 


class ProductCreate(BaseModel):  ##POST — create a product
    name: str
    price: float

class ProductUpdate(BaseModel):   ##PATCH — update only selected fields
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=50
    )
    price: float | None = Field(
        default=None,
        gt=0
    )