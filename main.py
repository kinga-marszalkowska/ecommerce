from typing import Optional
from pydantic import BaseModel
from model import Product
import uvicorn

from fastapi import FastAPI
from fakedb import data

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.get("/products/{product_id}")
def read_product(product_id: int, q: Optional[str] = None):
    if product_id in data.keys():
        return {"product": data[product_id]}
    else:
        return {"error": 404}



@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    return {"product_name": product.name, "product_id": product_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
