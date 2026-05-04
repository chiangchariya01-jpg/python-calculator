num1 = float(input("Enter first number: 21"))
num2 = float(input("Enter second number: 15"))
op = input("Choose (+, -, *, /): /")
if op == "+":
    print(num1 + num2)
elif op == "/":
    if num2 == 0:
        print(Error: Cannnot divide the by zero)
else:
    print(num1 / num2)
elif op == "**":
    print(num1 ** num2)
elif op == "%":
    print(num1 % num2)
op = input("Choose (+, -, *, /, **, %): ")
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose (+, -, *, /, **, %): ")

    if op == "+":
        print("Result:", num1 + num2)

    elif op == "-":
        print("Result:", num1 - num2)

    elif op == "*":
        print("Result:", num1 * num2)

    elif op == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result:", num1 / num2)

    elif op == "**":
        print("Result:", num1 ** num2)

    elif op == "%":
        print("Result:", num1 % num2)

    else:
        print("Invalid operator")

    again = input("Do you want to continue? (y/n): ")
    if again.lower() != "y":
        print("Goodbye 👋")
        break