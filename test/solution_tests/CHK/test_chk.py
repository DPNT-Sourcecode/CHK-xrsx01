import pytest
from solutions.CHK import checkout_solution


class TestCheckout:
    def test_sum_checkout(self):
        assert checkout_solution.checkout("ABC") == 100