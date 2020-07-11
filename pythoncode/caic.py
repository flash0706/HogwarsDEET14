from decimal import Decimal

class Calculator:
    def add(self, a, b):
        return Decimal(a) + Decimal(b)

    def sub(self, a, b):
        return Decimal(a) - Decimal(b)

    def mul(self, a, b):
        c = (Decimal(a) * Decimal(b)).quantize(Decimal(0.000))
        return c

    def div(self, a, b):
        try:
            return Decimal(a) / Decimal(b)
        except Exception :
            print('除法运算异常', Exception)