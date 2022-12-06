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


def report(resource):
    print(f"Water: {resource['water']}ml\nMilk: {resource['milk']}ml\nCoffee: {resource['coffee']}g"
          f"\nMoney: ${resource['money']}")


def enough_ingredients(drink, resource_dict):
    not_enough = 0
    ingredient_na = ""
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resource_dict[item]:
            not_enough += 1
            ingredient_na = item
            break
    if not_enough == 0:
        return True
    else:
        return False, print(f"Sorry there is not enough {ingredient_na}.")


def coins():
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    coins_received = quarters + dimes + nickles + pennies
    return coins_received


def transaction_successful(drink, coins_inserted):
    if coins_inserted < MENU[drink]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        resources["money"] += MENU[drink]["cost"]
        if coins_inserted > MENU[drink]["cost"]:
            coins_surplus = coins_inserted - MENU[drink]["cost"]
            print(f"Here is ${'{:.2f}'.format(coins_surplus)} in change.")
        return True


def make_coffee(drink, resource_dict):
    for item in MENU[drink]["ingredients"]:
        resource_dict[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink}☕. Enjoy!")


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

machine_on = True
while machine_on:
    order = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'off':
        machine_on = False
    elif order == 'report':
        report(resources)
    else:
        if enough_ingredients(order, resources):
            print("Please insert coins.")
            if transaction_successful(order, coins()):
                make_coffee(order, resources)
        else:
            machine_on = False

