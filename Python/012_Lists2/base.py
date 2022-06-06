import random
numlist = int(input("How many random numbers? "))
for x in range (0,numlist):
    randlist = []
    randlist.append(random.randrange(100))
    print(randlist)
    