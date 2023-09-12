# Initialize a variable to store the sum
total = 0

while True:
    try:
        # Input a number from the user
        num = float(input("Enter a number (or any non-numeric value to stop): "))

        # Add the entered number to the total
        total += num
    except ValueError:
        # If the user enters a non-numeric value, break out of the loop
        break

# Print the result
print("The sum of the entered numbers is:", total)
