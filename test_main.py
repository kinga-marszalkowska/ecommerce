import json

from fastapi import FastAPI
from fastapi.testclient import TestClient
from Product_model import Product
from fakedb import data
import random
from fastapi.encoders import jsonable_encoder

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
    created_product_id = max(data.keys()) + 1
    product = Product(id=created_product_id, name="new test element", price=1256, quantity=56,
                      description="Another element")
    response = client.post("/products/", data=json.dumps(jsonable_encoder(product)))
    assert response.status_code == 200
    assert response.json() == {"product": data[created_product_id]}
