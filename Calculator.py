print("Basic Calculator")

num1 = input("Enter the first number: ")

num2 = input("Enter the second number: ")

operator = input("Enter an operator to use (+, -, /, *)")

num1 = int(num1)
num2 = int(num2)

if operator == '+' :
    result = num1 + num2
elif operator == '-' :
    result = num1 - num2
elif operator == '*' :
    result = num1 * num2
elif operator == '/' :
    if num2 == 0:
        result = "Error: Cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operation"

print (f"{num1} {operator} {num2} = {result}")     

