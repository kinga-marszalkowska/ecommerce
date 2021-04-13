from fastapi import FastAPI
from fastapi.testclient import TestClient
from Product_model import Product
from fakedb import data
import random

from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to ecommerce backend"}


def test_read_product():
    product_id = random.choice(list(data.keys()))
    response = client.get("/products/{product_id}".format(product_id=product_id))
    assert response.status_code == 200
    assert response.json() == {"product": data[product_id]}


def test_create_product():
    # (autoincrement) always set id as one more than the last element in the list of data
    _id = list(data.keys())[-1] + 1
    print(_id)
    product = Product(id=_id, name="new test element", price="1256", quantity="56",
                      description="Another element", response_code=200)
    response = client.post("/products/", data=product.to_map())
    print(product.to_map())
    # assert response.status_code == 200
    print(response.json())
    assert response.json() == {"product": data[_id]}
