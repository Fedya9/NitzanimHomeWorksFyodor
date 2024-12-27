US = 3.42
FR = 3.54


class Airplane:
    def __init__(self, production_state, number_of_seats, engine, serial_number):
        self.production_state = production_state
        self.number_of_seats = number_of_seats
        self.engine = engine
        self.price = number_of_seats * engine.max_speed
        self.serial_number = serial_number

    def get_price(self):
        if self.production_state == "United States":
            self.price /= US
        else:
            self.price /= FR
        return self.price

    def print_details(self):
        print(
            f"the serial number is: {self.serial_number}\nthe num of seats is: {self.number_of_seats}\nstate of production is: {self.production_state}\nthe price is: {self.get_price()}\nmax speed of engine is: {self.engine.max_speed}")


class Engine:
    def __init__(self, max_speed, last_test_year):
        self.max_speed = max_speed
        self.last_test_year = last_test_year

    def get_max_speed(self):
        return self.max_speed

    def get_last_test_year(self):
        return self.last_test_year

    def print_details(self):
        print(f"max speed:{self.max_speed}\nlast test year:{self.last_test_year}")


engine1 = Engine(200, 2001)
first_plane = Airplane("Fracne", 30, engine1, 420348)
engine2 = Engine(300, 2003)
second_plane = Airplane("United States", 100, engine2, 304950)
engine3 = Engine(240, 2006)
third_plane = Airplane("United States", 50, engine3, 339495)
planes=[first_plane,second_plane,third_plane]
for plane in planes:
    plane.print_details(),plane.engine.print_details()