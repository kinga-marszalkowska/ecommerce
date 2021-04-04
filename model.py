from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    description: str

    response_code: Optional[int] = None
    error_message: Optional[str] = None

    def to_string(self, pretty: bool = False):
        return self.name, self.price
