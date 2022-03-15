from models.pydantic_models import BatchBase, OrderLineBase


class Batch:
    def __init__(self,
                 batch: BatchBase,
                 order_line: OrderLineBase):
        self.batch = batch
        self.order_line = order_line

    def allocate(self):
        self.batch.available_quantity -= self.order_line.quantity
