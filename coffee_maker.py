from menu import Menu, MenuItem

class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"water: {self.resources.get('water')}ml\n"
              f"milk:   {self.resources.get('milk')}ml\n"
              f"coffee: {self.resources.get('coffee')}gr")


    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        men=Menu()
        menuitem = men.find_drink(drink)
        if menuitem != None:
            if menuitem.ingredients['water'] > self.resources['water']:
                print("Sorry there is not enough water")
                return False
            if menuitem.ingredients['milk'] > self.resources['milk']:
                print("Sorry there is not enough milk")
                return False
            if menuitem.ingredients['coffee'] > self.resources['coffee']:
                print("Sorry there is not enough coffee")
                return False
        else:
            return False
        return True

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        #קודם תורידו את הכמויות ואח"כ תדפיסו:
        self.resources['water'] -= order.ingredients['water']
        self.resources['milk'] -= order.ingredients['milk']
        self.resources['coffee'] -= order.ingredients['coffee']
        print(f"Here is your {order.name} ☕️. Enjoy!")


