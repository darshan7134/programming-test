class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()  # Convert operation to lowercase for consistency

    def calculate(self) -> float:
        if self.operation == 'addition':
            return self.add()
        elif self.operation == 'subtraction':
            return self.subtract()
        elif self.operation == 'multiplication':
            return self.multiply()
        elif self.operation == 'division':
            return self.divide()
        else:
            raise ValueError("Invalid operation. Please use 'addition', 'subtraction', 'multiplication', or 'division'.")

    def add(self) -> float:
        return self.a + self.b

    def subtract(self) -> float:
        return self.a - self.b

    def multiply(self) -> float:
        return self.a * self.b

    def divide(self) -> float:
        if self.b == 0:
            raise ValueError("Cannot divide by zero.")
        return self.a / self.b

if __name__ == "__main__":
    a = 20.0
    b = 5.0
    operation = 'addition'  # Change this to 'subtraction', 'multiplication', or 'division' as needed

    calculator = Calculator(a, b, operation)
    result = calculator.calculate()
    print(f"The result of {operation} between {a} and {b} is: {result}")
