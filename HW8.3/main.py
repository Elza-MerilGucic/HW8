first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
arithmetic_operation = input("Enter one of the following operation +, -, * or /:")

if arithmetic_operation == "+":
    print(first_number + second_number)
elif arithmetic_operation == "-":
    print(first_number - second_number)
elif arithmetic_operation == "*":
    print(first_number * second_number)
elif arithmetic_operation == "/":
    print(first_number / second_number)

else:
    print("This operation is not supported: " + arithmetic_operation)
