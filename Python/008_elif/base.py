x = int(input("Please enter the first number: "))
operation = input("Please enter the operation: ")
y = int(input("Please enter the second number "))
if operation == "+":
    ans = x + y
    print(str(x) + "+" + str(y) + "=" + str(ans))
elif operation == "-":
    ans = x - y
    print(str(x) + "-" + str(y) + "=" + str(ans))
elif operation == "*":
    ans = x * y
    print(str(x) + "*" + str(y) + "=" + str(ans))
elif operation == "/":
    ans = x / y
    print(str(x) + "/" + str(y) + "=" + str(ans))