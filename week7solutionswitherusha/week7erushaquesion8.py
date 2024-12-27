class Animal:
    def __init__(self, type, age):
        self.type = type
        self.age = age

    def make_sound(self):
        print(f"ovvvvvvv im {self.type}")

    def show_age(self):
        self.make_sound()  , print(f"im {self.age} years old")


class Dolphin(Animal):
    def __init__(self, type, age, speed_under_water):
        super().__init__(type, age)
        self.speed_under_water = speed_under_water

    def show_speed(self):
        print(f"Im {self.type} just look, i swim in speed of {self.speed_under_water} under yhe water")

    def use_solar(self):
        print(f"im swimming into the water in speed of {self.speed_under_water} and use solar brrr")


dolphin = Dolphin("DOLPHIN", 11, 99)
dolphin.make_sound()
dolphin.show_age()
dolphin.show_speed()
dolphin.use_solar()
