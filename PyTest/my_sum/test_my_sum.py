import pytest

arg = []

@pytest.fixture
def sum() -> int:
    total = 0
    for val in arg:
        total += val
    return 1

def test_sum(sum):
    assert sum() == 3