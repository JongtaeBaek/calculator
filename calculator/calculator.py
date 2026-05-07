class Calculator:
    def __init__(self):
        self._history: list[str] = []

    def _validate(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Operands must be numbers")

    def _record(self, a, op, b, result):
        self._history.append(f"{a} {op} {b} = {result}")

    def add(self, a, b) -> float:
        self._validate(a, b)
        result = float(a + b)
        self._record(a, "+", b, result)
        return result

    def subtract(self, a, b) -> float:
        self._validate(a, b)
        result = float(a - b)
        self._record(a, "-", b, result)
        return result

    def multiply(self, a, b) -> float:
        self._validate(a, b)
        result = float(a * b)
        self._record(a, "*", b, result)
        return result

    def divide(self, a, b) -> float:
        self._validate(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = float(a / b)
        self._record(a, "/", b, result)
        return result

    def get_history(self) -> list[str]:
        return list(self._history)

    def clear_history(self) -> None:
        self._history.clear()
