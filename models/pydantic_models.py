from pydantic import BaseModel
from datetime import date
from typing import Optional, Set, List
from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLineBase(BaseModel):
    order_id: str
    stock_keeping_unit: str
    quantity: int


class BatchBase(BaseModel):
    reference: str
    stock_keeping_unit: str
    available_quantity: int
    estimated_time_of_arrival: Optional[date]
    allocations: Optional[List[OrderLineBase]] = []
