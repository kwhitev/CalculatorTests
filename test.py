import pytest
from app.calculator import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_multiply_success(self):
        assert self.calc.multiply(self, 1, 5) == 5
    def test_division_success(self):
        assert self.calc.division(self, 1, 1) == 1
    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 1, 1) == 0
    def test_adding_success(self):
        assert self.calc.adding(self, 5, 1) == 6
    def teardown(self):
        print('Выполнение метода Teardown')