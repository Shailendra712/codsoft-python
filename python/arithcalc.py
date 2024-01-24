def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice. Please enter a valid option.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    if choice == 1:
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == 2:
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == 3:
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == 4:
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()
