import sys

def add(a, b):
    return a + b

if len(sys.argv) != 3:
    print("Usage: python addition.py <operand1> <operand2>")
    sys.exit(1)

operand1 = float(sys.argv[1])
operand2 = float(sys.argv[2])

result = add(operand1, operand2)
print("Result:", result)
