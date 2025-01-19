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
        pass
print("Thanks 4 using have a nice day")