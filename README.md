# calculator
Title: Simple User Input Calculator
Description:
This is a simple calculator program written in Python that allows a user to input two numbers and a mathematical operation (+, -, *, /). The program will then perform the operation and display the result. Error handling is included for division by zero.

Requirements:
Python 3.6 or higher
Instructions:
Input First Number: The user will be prompted to enter the first number. The input is expected to be a float.

Enter first number: 5.6
This value is stored in the variable num1.

Input Second Number: The user will then be asked to enter the second number, which should also be a float.

Enter second number: 3.2
This value is stored in the variable num2.

Choose Mathematical Operation: The user will then be asked to choose an operation (+, -, *, /).

Enter operation (+, -, *, /): +
The chosen operation is stored in the variable operation.

Perform Calculation: Based on the chosen operation, the program calculates the result and prints it out.

For addition (+):

5.6 + 3.2 = 8.8
For subtraction (-):

5.6 - 3.2 = 2.4
For multiplication (*):

5.6 * 3.2 = 17.92
For division (/):

5.6 / 3.2 = 1.75
Error Handling: If the user tries to divide by zero, the program will display an error message.

Enter operation (+, -, *, /): /
Enter second number: 0
Error: Cannot divide by zero!
Invalid Operation: If an invalid operation is entered, the program will display an error message.

Enter operation (+, -, *, /): %
Invalid operation! Please use +, -, *, or /.
Code Implementation:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

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
License:
This code is shared under the MIT License.

Contributing:
Contributions are welcome! Feel free to submit pull requests to improve this simple calculator program.

Contact:
If you have any questions or feedback, feel free to reach out to the project maintainers.
