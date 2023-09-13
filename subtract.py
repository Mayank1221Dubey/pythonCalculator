import sys

def subtract(a, b):
    return a - b

if len(sys.argv) != 3:
    print("Usage: python subtraction.py <operand1> <operand2>")
    sys.exit(1)

operand1 = float(sys.argv[1])
operand2 = float(sys.argv[2])

result = subtract(operand1, operand2)
print("Result:", result)
print("I am Mayank Dubey and I live in pune")
print("I know My day will come definitely")
