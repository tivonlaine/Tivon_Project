MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money=0


def change():
    print("Please insert coins.")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickels=int(input("How many nickels?: "))
    pennies=int(input("How many pennies?: "))
    total=quarters*.25+dimes*.1+nickels*.05+pennies*.01
    return total

def transaction(money):
    change = total - MENU[option]["cost"]
 #   option=round(option, 2)
    print(f"Here is ${change} in change")
    print(f"Here is your {option}. Enjoy!")
    money += MENU[option]["cost"]
    return money

def enough():
    resources["water"] -= MENU[option]["ingredients"]["water"]
    resources["coffee"] -= MENU[option]["ingredients"]["coffee"]
    resources["milk"] -= MENU[option]["ingredients"]["milk"]

bool=True

while bool:
    option=input("What would you like? (espresso/latte/cappuccino): ")
    if option == "report":
        for i in resources:
            print(i.title(), end=": ")
            print(resources[i])
        print(f"Money: {money}")
    elif option=="off":
        bool=False
    elif option=="espresso":
        if resources["water"]<50:
            print("Sorry, there is not enough water. ")
        elif resources["coffee"]<18:
            print("Sorry there is not enough coffee")
        else:
            total=change()
            if total<MENU["espresso"]["cost"]:
                print("Not enough money.")
                bool=False
            else:
                resources["water"] -= MENU[option]["ingredients"]["water"]
                resources["coffee"] -= MENU[option]["ingredients"]["coffee"]
                money=transaction(money)
    elif option=="latte":
        if resources["water"]<200:
            print("Sorry, there is not enough water. ")
        elif resources["coffee"]<24:
            print("Sorry there is not enough coffee.")
        elif resources["milk"]<150:
            print("Sorry there is not enough milk.")
        else:
            total=change()
            if total<MENU["espresso"]["cost"]:
                print("Not enough money.")
                bool=False
            else:
                money=transaction(money)
                enough()
    elif option=="cappuccino":
        if resources["water"]<250:
            print("Sorry, there is not enough water. ")
        elif resources["coffee"]<24:
            print("Sorry there is not enough coffee.")
        elif resources["milk"]<100:
            print("Sorry there is not enough milk.")
        else:
            total=change()
            if total<MENU["cappuccino"]["cost"]:
                print("Not enough money.")
                bool=False
            else:
                money=transaction(money)
                enough()