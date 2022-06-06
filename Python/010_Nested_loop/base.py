symbol = input("Please enter the symbol you'd like to use: ")
line = int(input("Please enter a line length: "))
many = int(input("Please enter a width: "))
for x in range(0,many):
    for x in range(0,line):
        print(symbol, end="")
    print(x)