from fastapi import FastAPI
from fastapi.testclient import TestClient
from fakedb import data
import random

from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_read_product():
    product_id = random.choice(list(data.keys()))
    response = client.get("/products/{product_id}".format(product_id=product_id))
    assert response.status_code == 200
    assert response.json() == {"product": data[product_id]}
