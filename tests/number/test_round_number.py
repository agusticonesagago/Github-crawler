import pytest

from helpers.number import get_round_number


@pytest.mark.unit
class TestRoundNumber:
    def test_number_with_extra_zeros(self):
        assert get_round_number("52.0") == str(52)

    def test_number_with_decimals(self):
        assert get_round_number("52.01") == str(52.01)

    def test_empty_number(self):
        assert get_round_number("") is None
