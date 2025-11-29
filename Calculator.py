
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def squareroot(x, y):
    return x ** 0.5


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Modulus")

while True:
    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
       
            try: 
                num1 = float(input("Enter number to find square root: "))
            except ValueError:
                print("Square root of", num1, "=", squareroot(num1 , 0))
                next_calculation = input("Let's do next calculation? (yes/no): ")
                if next_calculation == "no":
                    break
            continue        
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
            print(num1, "**", num2, "=", power(num1, num2))

        elif choice == '6':
            print(num1, "√", num2, "=", squareroot(num1))
        
        # check if user wants another calculation
        # break the while loop if answer is no6

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
        print("Invalid Input")