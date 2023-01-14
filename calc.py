
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

def squared(x):
    return x * x

def cubed(x):
    return x * x * x


print("Select an operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square A Number")
print("6.Cube A Number")


while True:
    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input, Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    if choice in ('5'):
        try:
            num1 = float(input("Enter the number you want to square: "))
        except ValueError:
            print("Invalid input, Please enter a number.")
            continue

        if choice == '5':
            print(num1, "*", num1, "=", squared(num1))

    if choice in ('6'):
        try:
            num1 = float(input("Enter the number you want to cube: "))
        except ValueError:
            print("Invalid input, Please enter a number.")
            continue

        if choice == '6':
            print(num1, "*", num1, "*", num1, "=", cubed(num1))
        
        
        next_calculation = input("Do you want to do another calculation? (Yes/No): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
