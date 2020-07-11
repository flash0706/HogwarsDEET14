from decimal import Decimal

class Calculator:
    def add(self, a, b):
        try:
            return Decimal(a) + Decimal(b)
        except Exception:
            print('加法运算异常', Exception)

    def sub(self, a, b):
        try:
            return Decimal(a) - Decimal(b)
        except Exception:
            print('减法运算异常', Exception)

    def mul(self, a, b):
        try:
            c = (Decimal(a) * Decimal(b)).quantize(Decimal(0.000))
            return c
        except Exception:
            print('乘法运算异常', Exception)

    def div(self, a, b):
        try:
            return Decimal(a) / Decimal(b)
        except Exception :
            print('除法运算异常', Exception)