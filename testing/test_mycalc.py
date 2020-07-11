import sys
sys.path.append('..')
from pythoncode.caic import Calculator
import pytest


class TestMyCalc:

    def setup_class(self):
        self.cal = Calculator()
        print("setup_class")

    # def setup(self):
    #     print("开始计算")
    #
    # def teardwon(self):
    #     print("计算结束")

    @pytest.mark.add
    #在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
    @pytest.mark.parametrize('self_setup', ['add'], indirect=True)
    @pytest.mark.parametrize('a,b,result', [(1, 1, 2), (-1, -1, -2), (0, 0, 0), (0.1, 0.9, 1)], ids=['add_int', 'add_fushu', 'add_zero', 'add_decimal'])
    def test_add(self, a, b, result, self_setup):
        assert result == self.cal.add(a, b)

    @pytest.mark.sub
    @pytest.mark.parametrize('self_setup', ['sub'], indirect=True)
    @pytest.mark.parametrize('a,b,result', [(2, 1, 1), (-2, 1, -3), (0, 0, 0), (1, 0.9, 0.1)], ids=['sub_int', 'sub_fushu', 'sub_zero', 'sub_decimal'])
    def test_sub(self, a, b, result, self_setup):
        assert result == self.cal.sub(a, b)

    @pytest.mark.div
    @pytest.mark.parametrize('self_setup', ['div'], indirect=True)
    @pytest.mark.parametrize('a,b,result', [(10, 5, 2), (-5, -1, 5), (0, 0, 0), (0.9, 0.1, 9)], ids=['div_int', 'div_fushu', 'div_zero', 'div_decimal'])
    def test_div(self, a, b, result, self_setup):
        assert result == self.cal.div(a, b)

    @pytest.mark.mul
    @pytest.mark.parametrize('self_setup', ['mul'], indirect=True)
    @pytest.mark.parametrize('a,b,result', [(1, 2, 2), (-1, -2, 2), (0, 0, 0), (0.1, 0.9, 0.09)], ids=['mul_int', 'mul_fushu', 'mul_zero', 'mul_decimal'])
    def test_mul(self, a, b, result, self_setup):
        assert result == self.cal.mul(a, b)

