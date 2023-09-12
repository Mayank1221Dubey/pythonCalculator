import sys

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

if len(sys.argv) != 3:
    print("Usage: python division.py <operand1> <operand2>")
    sys.exit(1)

operand1 = float(sys.argv[1])
operand2 = float(sys.argv[2])

result = divide(operand1, operand2)
print("Result:", result)
