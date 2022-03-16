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
            self.batch.allocations.append(order_line)
        else:
            raise InsufficientAvailableQuantity

    def deallocate(self, order_line: OrderLineBase) -> Any:
        if order_line in self.batch.allocations:
            self.batch.available_quantity += order_line.quantity
            self.batch.allocations.remove(order_line)

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.batch.reference == self.batch.reference

    def __hash__(self):
        return hash(self.batch.reference)


