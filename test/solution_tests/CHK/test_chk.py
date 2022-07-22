import pytest
from solutions.CHK import checkout_solution


class TestCheckout:
    def test_sum(self):
        assert checkout_solution.compute(1, 2) == 3
