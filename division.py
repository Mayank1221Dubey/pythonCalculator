# Initialize a result variable to store the result
result = 0

while True:
    try:
        # Input a number from the user
        num = float(input("Enter a number (or any non-numeric value to stop): "))

        # Ask the user for an operation choice (addition, subtraction, multiplication, or division)
        operation = input("Choose an operation (+ for addition, - for subtraction, * for multiplication, / for division): ")

        if operation == '+':
            # Addition
            result += num
        elif operation == '-':
            # Subtraction
            result -= num
        elif operation == '*':
            # Multiplication
            result *= num
        elif operation == '/':
            # Division
            if num == 0:
                print("Error: Division by zero")
            else:
                result /= num
        else:
            print("Invalid operation")
    except ValueError:
        # If the user enters a non-numeric value, break out of the loop
        break

# Print the final result
print("The result is:", result)
