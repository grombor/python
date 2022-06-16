import pytest

class TestClass:

    def test_1(self):
        assert True

    def test_2(self):
        assert 1 == 0, "There should be 1"

    def f(self):
        return 3

    def test_function(self):
        assert self.f() == 3

    def myfunc(self):
        raise ValueError("Exception 123 raised")

    def test_match(self):
        with pytest.raises(ValueError, match=r".* 123 .*"):
            self.myfunc()
