from typing import Optional
from pydantic import BaseModel
from Product_model import Product
import uvicorn

from fastapi import FastAPI
from fakedb import data

app = FastAPI()

# Product
@app.get("/")
def read_root():
    return {"msg": "Welcome to ecommerce backend"}


@app.get("/products/{product_id}")
def read_product(product_id: int):
    if product_id in data.keys():
        return {"product": data[product_id]}
    else:
        return {"error": 404}


@app.get("/products/")
def get_all_products():
    return data


@app.post("/products/")
async def create_product(product: Product):
    if product.id in data.keys():
        return {"error": 409}
    else:
        data[product.id] = product
        return {"product": data[product.id]}


@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    return {"product_name": product.name, "product_id": product_id}


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    data[product_id] = {}


# todo 422 Unprocessable Entity error
@app.put("/products/{product_id}")
def subtract_quantity(product_id: int, quantity: int):
    if quantity > data[product_id].quantity:
        return {"error": 405, "message": "cannot get that many elements"}
    else:
        qty = data[product_id].quantity
        data[product_id].quantity = qty - quantity
        return {data[product_id]}


# Stock
def update_stock(product_id: int, quantity: int):
    pass


# Basket
def add_to_basket(product_id: int, quantity: int, customer_id: int):
    pass


def remove_from_basket(product_id: int, customer_id: int):
    pass


def update_quantity(product_id: int, quantity: int, customer_id: int):
    pass

# Customer



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
