import random
placelist = ["IHOP", "Tickle Tree Cafe", "Baja Fresh"]
r = random.randrange(3)
print(placelist)
choice = input("Please choose a restaurant: ")
if(choice == "IHOP"):
    menu = ["pancakes", "omelettes", "waffles"]
    print("recommended:")
    print(menu[r])
elif(choice == "Tickle Tree Cafe"):
    menu = ["Mint lemonade", "Grilled Cheese", "Chopped salad"]
    print("recommended:")
    print(menu[r])
elif(choice == "Baja Fresh"):
    menu = ["Spanish rice", "Burrito", "Enchilada"]
    print("recommended:")
    print(menu[r])