from fastapi import FastAPI, status,HTTPException
from pydantic import BaseModel


app = FastAPI()


class Products(BaseModel):
    id: int
    name: str
    price: float


products = [
    {"id": 1, "name": "Apple", "price": 100},
    {"id": 2, "name": "Banana", "price": 60},
    {"id": 3, "name": "Orange", "price": 80}
]


@app.get("/")
def home():
    return {"message": "Welcome to Retail shop"}


# GET - all products
@app.get("/products")
def get_products():
    return products


# POST - add product
@app.post("/products", status_code=status.HTTP_201_CREATED)
def add_product(product: Products):
    products.append(product.model_dump())
    return product


# GET - product by ID (Path Parameter)
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {"message": "Product not found"}


# PUT - update product
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Products):
    for item in products:
        if item["id"] == product_id:
            item["name"] = product.name
            item["price"] = product.price
            return item

    return {"message": "Product not found"}

# PATCH - update product
#why product_update class becoz in class Product req all values so we create saparate class for patch
class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None

@app.patch("/products/{product_id}")
def patch_product(product_id: int, product_update: ProductUpdate):
    for item in products:
        if item["id"] == product_id:
            if product_update.name is not None:
                item["name"] = product_update.name
            if product_update.price is not None:
                item["price"] = product_update.price
            return item

    return {"message": "Product not found"}

#delete product
@app.delete("/products/{product_id}")
def delete_product(product_id:int):
    for product in products:
        if product["id"]==product_id:
            products.remove(product)
            return {"message":"Product deleted successfully"}
    raise HTTPException(status_code=404,detail="Product not found")      