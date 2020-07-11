import sys
sys.path.append('..')
from pythoncode.caic import Calculator
import pytest


def setup_module():
    print("setup_module")


def teardown_module():
    print("teardown_module")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")



class TestCalc:

    def setup_class(self):
        self.cal = Calculator()
        print("setup_class")

    def teardwon_class(self):
        print("teardwon_class")

    def setup(self):
        print("setup")

    def teardwon(self):
        print("teardwon")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,result', [(1, 1, 2), (-1, -1, -2), (0, 0, 0)], ids=['int', 'fushu', 'zero'])
    def test_add(self, a, b, result):
        # cal = Calculator()
        assert result == self.cal.add(a, b)

    @pytest.mark.add
    def test_add1(self):
        # cal = Calculator()
        assert 3 == self.cal.add(1, 2)

    @pytest.mark.div
    def test_div(self):
        # cal = Calculator()
        assert -1 == self.cal.div(1, 2)

def test_1():
    print()