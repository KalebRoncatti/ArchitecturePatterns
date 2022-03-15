from typing import Any

from models.pydantic_models import BatchBase, OrderLineBase
from exceptions.exceptions import InsufficientAvailableQuantity


class Batch:
    def __init__(self,
                 batch_base: BatchBase):
        self.batch = batch_base

    def can_allocate(self, order_line: OrderLineBase) -> bool:
        if self.batch.available_quantity >= order_line.quantity and self.batch.stock_keeping_unit == order_line.stock_keeping_unit:
            return True
        else:
            return False

    def allocate(self, order_line: OrderLineBase) -> Any:
        if self.can_allocate(order_line=order_line):
            self.batch.available_quantity -= order_line.quantity
        else:
            raise InsufficientAvailableQuantity
