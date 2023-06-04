import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

# Function to calculate square root of a number
def squareRoot(x):
    return math.sqrt(x)

# Function to calculate sine of an angle in degrees
def sine(x):
    return math.sin(math.radians(x))

# Function to calculate cosine of an angle in degrees
def cosine(x):
    return math.cos(math.radians(x))

# Function to calculate tangent of an angle in degrees
def tangent(x):
    return math.tan(math.radians(x))

# Function to calculate logarithm (base 10) of a number
def logarithm(x):
    return math.log10(x)

# Main calculator function
def calculator():
    print("Welcome to Advanced Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Sine")
    print("7. Cosine")
    print("8. Tangent")
    print("9. Logarithm")
    print("10. Quit")

    while True:
        choice = input("Enter your choice (1-10): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                if num2 != 0:
                    print("Result:", divide(num1, num2))
                else:
                    print("Error: Cannot divide by zero")

        elif choice == '5':
            num = float(input("Enter a number: "))
            print("Result:", squareRoot(num))

        elif choice == '6':
            angle = float(input("Enter an angle in degrees: "))
            print("Result:", sine(angle))

        elif choice == '7':
            angle = float(input("Enter an angle in degrees: "))
            print("Result:", cosine(angle))

        elif choice == '8':
            angle = float(input("Enter an angle in degrees: "))
            print("Result:", tangent(angle))

        elif choice == '9':
            num = float(input("Enter a number: "))
            print("Result:", logarithm(num))

        elif choice == '10':
            print("Thank you for using Advanced Calculator")
            break

        else:
            print("Invalid choice. Please try again.")


# Calling the calculator function to start the calculator
calculator()
