from pydantic import BaseModel
from datetime import date
from typing import Optional


class BatchBase(BaseModel):
    reference: str
    stock_keeping_unit: str
    available_quantity: int
    estimated_time_of_arrival: Optional[date]


class OrderLineBase(BaseModel):
    order_id: str
    stock_keeping_unit: str
    quantity: int

