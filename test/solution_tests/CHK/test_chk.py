import pytest
from solutions.CHK import checkout_solution


class TestCheckout:
    def test_sum_checkout(self):
        assert checkout_solution.checkout("ABC") == 100
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AF") == -1
        assert checkout_solution.checkout("AAAAAAF") == -1
        # assert checkout_solution.checkout("BABACAGA") == 45 + 130 + 20 - 1 + 50
        assert checkout_solution.checkout("BABACAGA") == -1
        assert checkout_solution.checkout("AxA") == -1





