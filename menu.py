class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, milk, cream, syrup, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "milk": milk,
            "cream": cream,
            "syrup": syrup
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="espresso", milk=60, cream=150, syrup=24, cost=234),
            MenuItem(name="cappuccino", milk=80, cream=90, syrup=125, cost=295),
            MenuItem(name="latte", milk=100, cream=125, syrup=150, cost=375),
        ]
# milk = water , 
    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
