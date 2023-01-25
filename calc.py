import math
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

def squareroot(x):
    return math.sqrt(x)

def cuberoot(x):
    return math.cbrt(x)

def isprime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return str("Is Not A Prime Number")
  return str("Is A Prime Number")

def tothepowerof(x, y):
    return x ** y

print("Select an operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square A Number")
print("6.Cube A Number")
print("7.Square Root A Number")
print("8.Cube Root A Number")
print("9.Find Out If A Number Is Prime")
print("10.Power Numbers")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")

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

    if choice in ('7'):
        try:
            num1 = float(input("Enter the number you want to square root: "))
        except ValueError:
            print("Invalid input, Please enter a number.")
            continue

        if choice == '7':
            print("The square root of", num1,"=", squareroot(num1))

    if choice in ('8'):
        try:
            num1 = float(input("Enter the number you want to cube root: "))
        except ValueError:
            print("Invalid input, Please enter a number.")
            continue

        if choice == '8':
            print("The cube root of", num1,"=", cuberoot(num1))

    if choice in ('9'):
        try:
            num1 = float(input("Enter the number to check if it's prime: "))
        except ValueError:
            print("Invalid input, Please enter a number.")
            continue

        if choice == '9':
            print(num1, isprime(num1))

    if choice in ('10'):
        try:
            num1 = float(input("Enter the number you want to power: "))
            num2 = float(input("Enter the number you want to power it by: "))
        except ValueError:
            print("Invalid input, Please enter a number.")
            continue

        if choice == '10':
            print(num1, "to the power of", num2, "=", tothepowerof(num1, num2))
            

            
        
        
    next_calculation = input("Do you want to do another calculation? (Yes/No): ")
    if next_calculation == "no":
          break
    else:
        print("Invalid Input")


