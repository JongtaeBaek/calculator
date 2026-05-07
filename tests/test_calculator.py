import pytest
from calculator import Calculator


class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5.0
        assert self.calc.add(1.5, 2.5) == 4.0
        assert isinstance(self.calc.add(1, 2), float)

    def test_subtract(self):
        assert self.calc.subtract(10, 4) == 6.0
        assert self.calc.subtract(0.5, 0.2) == pytest.approx(0.3)

    def test_multiply(self):
        assert self.calc.multiply(3, 7) == 21.0
        assert self.calc.multiply(2.5, 4) == 10.0

    def test_divide(self):
        assert self.calc.divide(10, 2) == 5.0
        assert self.calc.divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)

    def test_invalid_type(self):
        with pytest.raises(TypeError, match="Operands must be numbers"):
            self.calc.add("a", 1)
        with pytest.raises(TypeError, match="Operands must be numbers"):
            self.calc.multiply(1, None)

    def test_history_format(self):
        self.calc.add(2, 3)
        self.calc.divide(10, 2)
        history = self.calc.get_history()
        assert history == ["2 + 3 = 5.0", "10 / 2 = 5.0"]

    def test_history_is_copy(self):
        self.calc.add(1, 1)
        history = self.calc.get_history()
        history.append("tampered")
        assert len(self.calc.get_history()) == 1

    def test_clear_history(self):
        self.calc.add(1, 2)
        self.calc.clear_history()
        assert self.calc.get_history() == []
