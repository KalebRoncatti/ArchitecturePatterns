from datetime import date
from typing import Tuple

from models.pydantic_models import BatchBase, OrderLineBase
from models.models import Batch


def make_batch_and_line(stock_keeping_unit: str,
                        batch_quantity: int,
                        line_quantity: int) -> Tuple[Batch, OrderLineBase]:
    batch_base = BatchBase(reference="batch-001",
                           stock_keeping_unit=stock_keeping_unit,
                           available_quantity=batch_quantity,
                           estimated_time_of_arrival=date.today())
    order_line_base = OrderLineBase(order_id="order-ref",
                                    stock_keeping_unit=stock_keeping_unit,
                                    quantity=line_quantity)
    return Batch(batch_base=batch_base), order_line_base


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch, order_line = make_batch_and_line(stock_keeping_unit='RED-BED',
                                            batch_quantity=20,
                                            line_quantity=2)
    batch.allocate(order_line=order_line)
    assert batch.batch.available_quantity == 18


def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line("ELEGANT-LAMP", 20, 2)
    assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_available_smaller_than_required():
    small_batch, large_line = make_batch_and_line("ELEGANT-LAMP", 2, 20)
    assert small_batch.can_allocate(large_line) is False


def test_can_allocate_if_available_equal_to_required():
    batch, line = make_batch_and_line("ELEGANT-LAMP", 2, 2)
    assert batch.can_allocate(line)


def test_cannot_allocate_if_skus_do_not_match():
    batch_base = BatchBase(reference="batch-001",
                           stock_keeping_unit="UNCOMFORTABLE-CHAIR",
                           available_quantity=20,
                           estimated_time_of_arrival=None)

    different_sku_line = OrderLineBase(order_id="order-123",
                                       stock_keeping_unit="EXPENSIVE-TOASTER",
                                       quantity=10)
    batch = Batch(batch_base=batch_base)
    assert batch.can_allocate(different_sku_line) is False


if __name__ == '__main__':
    test_allocating_to_a_batch_reduces_the_available_quantity()
    test_can_allocate_if_available_greater_than_required()
    test_cannot_allocate_if_available_smaller_than_required()
    test_can_allocate_if_available_equal_to_required()
    test_cannot_allocate_if_skus_do_not_match()

