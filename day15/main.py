import quarter

milk = 200
water = 300
coffee = 100
money = 0.0
def report():
    print(f"water {water}ml")
    print(f"Milk {milk}ml")
    print(f"Coffee {coffee}g")
    print(f"Money ${money:.2f}")

def espresso():
    global  water,coffee

    if (water >=50 and coffee >= 18):
        coin()
        water -= 50
        coffee -= 18
    else:
        print("Not enough")

def latte():
    global water, coffee, milk

    if (water >= 200 and coffee >= 24):
        if (milk >= 150):
            coin()
            water -= 200
            coffee -= 24
            milk -= 150
    else:
        print("Not enough")

def cappuccino():
    global water, coffee, milk

    if (water >= 250 and coffee >= 24):
        if (milk >= 100):
            coin()
            water -= 250
            coffee -= 24
            milk -= 100
    else:
        print("Not enough")


def coin():
    global money
    quarter = input("How many quarter? : ")
    dime = input("How many dimes? : ")
    nickles = input("How many nickles? : ")
    penny = input("How many pennies? : ")
    total = int(quarter)*0.25 + int(dime)*0.1 + int(nickles)*0.05 + int(penny)*0.01
    if (like == "es" and total >= 1.5):
        remain = total - 1.5
        money = money + 1.5
        print(f"Here is ${remain:.2f} in change.")
    elif (like == "la" and total >= 2.5):
        remain = total - 2.5
        money = money + 2.5
        print(f"Here is ${remain:.2f} in change.")
    elif (like == "ca" and total >= 3.0):
        remain = total - 3.0
        money = money + 3.0
        print(f"Here is ${remain:.2f} in change.")
    else:
        print("Please add more coins.")





like = input("What would you like? (Espresso/Latte/Cappuccino) : ").lower()

while like != "exit":
    if (like == "report"):
        report()
    elif (like == "es"):
        espresso()
    elif (like == "la"):
        latte()
    elif (like == "ca"):
        cappuccino()
    else:
        print("Please enter proper input")

    like = input("What would you like? (Espresso/Latte/Cappuccino) : ").lower()


