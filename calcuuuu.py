# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function raises x to the power y
def power(x, y):
    return x ** y

# This function calculates the square root of x
def square_root(x):
    return x ** 0.5

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power (x^y)")
print("6. Square Root (√x)")

while True:
    # take input from the user
    choice = input("Enter choice (1/2/3/4/5/6): ")

    # operations that require two numbers
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "^", num2, "=", power(num1, num2))

    # square root only needs one number
    elif choice == '6':
        try:
            num = float(input("Enter number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if num < 0:
            print("Cannot take square root of a negative number.")
        else:
            print("√", num, "=", square_root(num))

    else:
        print("Invalid Input")
        continue

    next_calculation = input("Lets do next calculation? (yes/no): ")
    if next_calculation.lower() == "no":
        break