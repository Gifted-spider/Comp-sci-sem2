numlist = [6,9,32,28,15,22,3,18]
nummax = 0
nummin = 10000000000000
numsum = 0
for i in range(0,len(numlist)):
    if(nummax < numlist[i]):
        nummax = numlist[i]
print("The maximum is:")
print(nummax)

for i in range(0,len(numlist)):
    if(nummin > numlist[i]):
        nummin = numlist[i]
print("The minimum is:")
print(nummin)

for i in range(0,len(numlist)):
    numsum = numsum + numlist[i]
average = numsum / len(numlist)
print("The average is:")
print(average)

