import pytest
from calculations import sum


def test_sum_works():
    assert sum(1, 3) == 4, "sum calculation failed"


def test_sum_arg_out_of_bounds():
    with pytest.raises(ValueError) as exc_info:
        sum(-1, 3)
    assert "Argument out of bounds" in str(exc_info.value)
