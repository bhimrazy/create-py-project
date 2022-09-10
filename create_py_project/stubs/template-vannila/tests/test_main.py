from src.main import find_sum


def test_find_sum():
    """Test for function find_sum.
    """
    s = find_sum(1, 1)
    assert s == 2
