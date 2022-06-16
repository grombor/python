import pytest

@pytest.fixture
def do_sum(n):
    # return (lambda *args : sum(*args))
    return lambda a: a + n

