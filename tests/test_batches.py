from datetime import date

from models.pydantic_models import BatchBase, OrderLineBase
from models.models import Batch


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch_base = BatchBase(reference="batch-001",
                           stock_keeping_unit="SMALL-TABLE",
                           available_quantity=20,
                           estimated_time_of_arrival=date.today())
    line_base = OrderLineBase(order_id='order-ref',
                              stock_keeping_unit="SMALL-TABLE",
                              quantity=2)
    batch = Batch(batch=batch_base,
                  order_line=line_base)

    batch.allocate()

    assert batch.batch.available_quantity == 18


if __name__ == '__main__':
    test_allocating_to_a_batch_reduces_the_available_quantity()
