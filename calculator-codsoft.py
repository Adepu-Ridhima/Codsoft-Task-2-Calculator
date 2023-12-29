
operator = input("Enter an operation (+ - * /): ")
num1 = float(input("Enter the 1st value: "))
num2 = float(input("Enter the 2nd value: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{Operation} is not a valid operator")