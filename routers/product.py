from fastapi import APIRouter, status,Depends, HTTPException
from schemas.product import Products, ProductUpdate
from services import product as product_service

from sqlalchemy.orm import Session
from database.connection import get_db
from database.models import Product
from schemas.product import ProductCreate

router = APIRouter()


@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


 

@router.post("/products", status_code=201)
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    new_product = Product(
        name=product.name,
        price=product.price
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@router.get("/products/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product

@router.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    existing_product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if existing_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    existing_product.name = product.name
    existing_product.price = product.price

    db.commit()
    db.refresh(existing_product)

    return existing_product

@router.patch("/products/{product_id}")
def patch_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    existing_product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if existing_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product.name is not None:
        existing_product.name = product.name

    if product.price is not None:
        existing_product.price = product.price

    db.commit()
    db.refresh(existing_product)

    return existing_product


@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    existing_product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if existing_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(existing_product)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }




