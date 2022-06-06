howmany = int(input("How many items are you purchasing? "))
fullprice = 0
for x in range(0,howmany):
    item = input("What item are you purchasing? ")
    price = float(input("How much is the item? "))
    print("Thank you for purchasing " + item)
    print("____________________________")
    fullprice = fullprice + price
print("For " + str(howmany) + " items, your total is " + str(fullprice))
print("Have a nice day!")