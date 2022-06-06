line = int(input("Please enter a line length: "))
umm = input("Do you want a horizontal or vertical line? ")
x = "*"
if umm == "hor":
    for x in range(0,line):
        print( "*",end= ", ")
if umm == "vert":
    for x in range(0,line):
        print("*")