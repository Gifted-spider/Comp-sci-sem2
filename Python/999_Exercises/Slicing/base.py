name = input("What is your name? ")
space = 1
for i in range(0, len(name)):
    if(name[i:i+1] == " "):
        space = i
    print(name[i:i+1])
print(" ")
for x in range(space, len(name)):
    print(name[x:x+1])
print(" ")
for m in range(0,space):
    print(name[m:m+1])