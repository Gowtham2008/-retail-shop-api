from fastapi import HTTPException, status

products = [
    {"id": 1, "name": "Apple", "price": 100},
    {"id": 2, "name": "Banana", "price": 60},
    {"id": 3, "name": "Orange", "price": 80}
]


def get_all_products():
    return products


def get_product_by_id(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )


def create_product(product):

    for item in products:
        if item["id"] == product.id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Product ID already exists"
            )

    new_product = product.model_dump()
    products.append(new_product)

    return new_product


def update_product(product_id: int, product):

    for item in products:

        if item["id"] == product_id:
            item["name"] = product.name
            item["price"] = product.price

            return item

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )


def patch_product(product_id: int, product):

    for item in products:

        if item["id"] == product_id:

            if product.name is not None:
                item["name"] = product.name

            if product.price is not None:
                item["price"] = product.price

            return item

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )


def delete_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            products.remove(product)

            return {
                "message": "Product deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )