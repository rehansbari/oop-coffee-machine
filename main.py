from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
#item = MenuItem()
admin_function = MoneyMachine()

user_coffee_choice = ""
while user_coffee_choice != "off":
    user_coffee_choice = input(f"What would you like? {menu.get_items()}: ")
    if user_coffee_choice == "report":
        coffee.report()
        admin_function.report()
    else:
        drink = menu.find_drink(user_coffee_choice)
        if coffee.is_resource_sufficient(drink) and admin_function.make_payment(drink.cost):
            coffee.make_coffee(drink)