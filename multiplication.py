# Initialize a variable to store the result
result = 0

while True:
    try:
        # Input a number from the user
        num = float(input("Enter a number (or any non-numeric value to stop): "))

        # Subtract the entered number from the result
        result -= num
    except ValueError:
        # If the user enters a non-numeric value, break out of the loop
        break

# Print the result
print("The result of the subtraction is:", result)
