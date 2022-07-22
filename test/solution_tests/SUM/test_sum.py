import pytest
from solutions.SUM import sum_solution


class TestSum:
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_works(self):
        assert sum_solution.compute(1, 3) == 4, "sum calculation failed"

    def test_sum_arg_out_of_bounds_lower(self):
        with pytest.raises(ValueError) as exc_info:
            sum_solution.compute(-1, 3)
        assert "Argument out of bounds" in str(exc_info.value)

    def test_sum_arg_out_of_bounds_upper(self):
        with pytest.raises(ValueError) as exc_info:
            sum_solution.compute(150, 3)
        assert "Argument out of bounds" in str(exc_info.value)
