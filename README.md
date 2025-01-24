﻿# coffee_machine_project
# Resources available in the coffee machine
resources = {
    "water": 500,  # in ml
    "milk": 300,   # in ml
    "coffee": 100, # in grams
}

# Needed resources and prices of coffee types
menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0},
}
money = 0


def check(drink, resources):
    for item in menu[drink]:
        if item != "cost" and menu[drink][item] > resources[item]:
            print(f"Sorry, there isn't enough {item}")
            return False
        print("Booya!")
        return True

def insert_money():
    print("Please insert coins.")
    try:
        total = (
            int(input("How many Andruarters? ")) * 0.25 +
            int(input("How many Andrimes? ")) * 0.10 +
            int(input("How many Andrickles? ")) * 0.05 +
            int(input("How many Andrennies? ")) * 0.01
        )
    except ValueError:
        print("Please try again.")
        return 0.0
    return round(total, 2)
def make_coffee(drink, resources):
    for item in menu[drink]:
        if item != "cost":
            resources[item] -= menu[drink][item]
    return resources, f"Drink your {drink} lazy."
#code
coffe_machine = "on"
while coffe_machine == "on":
    drink = input("What would you like? (espresso: A$1.50 / latte: A$2.50 / cappuccino: A$3.00):")

    if drink == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources["milk"]} ml")
        print(f"Coffee: {resources['coffee']} grams")
        print(f"Money A${money}")
    elif drink == ("off"):
        coffe_machine = "off"
        break
    elif drink in menu:
        check(drink, resources)
        inserted_money = insert_money()
        if inserted_money >= menu[drink]["cost"]:
            change = round(inserted_money - menu[drink]["cost"], 2)
            if change > 0:
                    print(f"Here is A${change} in change.")
                    money += menu[drink]["cost"]
                    print("Resources before:")
                    print(resources)
                    resources, coffee = make_coffee(drink, resources)
                    print("Resources now:")
                    print(resources)
                    print(coffee)
        else:
            print("Theres not enough money, r u sure u know how 2 count.")

print("Thanks 4 using have a nice day")
