from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    options = menu.get_items()
    choice = input(f"What do you want?{options}: ").lower()
    if choice == "off":
        break
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        beverage = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(beverage) and money_machine.make_payment(beverage.cost):
            coffee_maker.make_coffee(beverage)
