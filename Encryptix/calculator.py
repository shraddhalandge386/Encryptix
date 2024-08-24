def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    print("Simple Calculator")
    print("----------------")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = int(input("Enter your choice (1/2/3/4): "))

    if operation == 1:
        result = add(num1, num2)
    elif operation == 2:
        result = subtract(num1, num2)
    elif operation == 3:
        result = multiply(num1, num2)
    elif operation == 4:
        result = divide(num1, num2)
    else:
        print("Invalid operation choice. Please try again.")
        return

    print(f"Result: {num1} {get_operator(operation)} {num2} = {result:.2f}")

def get_operator(operation):
    if operation == 1:
        return "+"
    elif operation == 2:
        return "-"
    elif operation == 3:
        return "*"
    elif operation == 4:
        return "/"

if __name__ == "__main__":
    calculator()