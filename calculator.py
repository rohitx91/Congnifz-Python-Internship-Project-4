# Level 1 - Task 4
# Basic Calculator Program

def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        return num1 / num2
    else:
        return "Invalid operator!"

# --- Main Program ---
print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculator(num1, num2, operator)
print("Result:", result)
