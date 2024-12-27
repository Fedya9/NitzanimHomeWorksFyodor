class Store:
    def __init__(self, computers, screens):
        self.computers = computers
        self.screens = screens

    def get_computers(self):
        return self.computers

    def get_screens(self):
        return self.screens

    def buy_computer_by_color(self, first_color, second_color):
        for computer in self.computers:
            if computer.color == first_color or computer.color == second_color:
                computer.print_details()
                print()
            else:
                continue

    def suggest_screens_to_computer(self, computer):
        list_of_screens_of_computer_company = [
            screen for screen in self.screens if screen.company == computer.company
        ]

        if list_of_screens_of_computer_company:
            print(f"Suggested screens for {computer.company} ({computer.company}):")
            for screen in list_of_screens_of_computer_company:
                screen.print_details()
        else:
            print(f"No screens available for {computer.company}.")


class Computer:
    def __init__(self, color, company, price, shelf_number):
        self.color = color
        self.company = company
        self.price = price
        self.shelf_number = shelf_number

    def get_color(self):
        return self.color

    def get_company(self):
        return self.company

    def get_price(self):
        return self.price

    def get_shelf_number(self):
        return self.shelf_number

    def print_details(self):
        print(
            f"computer color: {self.color}\ncomputer company: {self.company}\ncomputer price: {self.price}\ncomputer num of shelf:{self.shelf_number}")


class Screen:
    def __init__(self, size, company, price, shelf_number):
        self.size = size
        self.company = company
        self.price = price
        self.shelf_number = shelf_number

    def get_size(self):
        return self.size

    def get_company(self):
        return self.company

    def get_price(self):
        return self.price

    def get_shelf_number(self):
        return self.shelf_number

    def print_details(self):
        print(
            f"screen size: {self.size}\nscreen company: {self.company}\nscreen price: {self.price}\nscreen shelf number: {self.shelf_number}")


def main():
    computer1 = Computer("pink", "apple", 2500, 44)
    computer2 = Computer("yellow", "apple", 2333, 78)
    computer3 = Computer("black", "lenovo", 1500, 13)
    screen1 = Screen(44, "apple", 400, 11)
    screen2 = Screen(50, "apple", 600, 99)
    screen3 = Screen(66, "samsung", 1000, 111)
    computers = [computer1, computer2, computer3]
    screens = [screen1, screen2, screen3]
    mine_store = Store(computers, screens)
    mine_store.buy_computer_by_color("pink", "black")
    mine_store.buy_computer_by_color("orange", "purple")
    mine_store.suggest_screens_to_computer(computer1)


main()
