def calculate_nums(num1: int, num2: int, operation: str) -> int:
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 // num2
    else:
        return 0




num_one = int(input("Enter first number: "))
num_two = int(input("Enter second number: "))
print('+')
print('-')
print('*')
print('/')
operation = input("Pick an operation from the choices above: ")

result = calculate_nums(num_one,num_two,operation)
print(f"{num_one} {operation} {num_two} = {result}")