# Get first number from user
num1 = float(input("Enter first number: "))

# Get second number from user  
num2 = float(input("Enter second number: "))

# Get mathematical operation from user
operation = input("Enter operation (+, -, *, /): ")

# Perform the operation and display result
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation! Please use +, -, *, or /.")
