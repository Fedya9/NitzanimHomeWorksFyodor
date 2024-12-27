class GroceryList:
    def __init__(self):
        self.groceries = []

    def add_grocery(self, grocery_name):
        self.groceries.append(grocery_name)

    def reset_grocery(self):
        self.groceries.clear()

    def print_grocery_list(self):
        print(self.groceries)


Mylist = GroceryList()
Mylist.add_grocery("milk")
Mylist.add_grocery("bread")
Mylist.add_grocery("eggs")
Mylist.print_grocery_list()
Mylist.add_grocery("chicken")
Mylist.print_grocery_list()
Mylist.reset_grocery()
Mylist.print_grocery_list()


