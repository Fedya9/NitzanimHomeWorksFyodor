class Lamp:
    def __init__(self, light_color):
        self.light_color = light_color
        self.is_on = False

    def turn_on_light(self):
        self.is_on = True

    def turn_off_light(self):
        self.is_on = False

    def print_lamp_status(self):
        print(f"the light of the lamp is {self.light_color} and the lamp is {self.is_on}")


lamp_blue = Lamp("blue")
lamp_orange = Lamp("orange")
lamp_blue.turn_on_light()
lamp_orange.print_lamp_status()
lamp_blue.print_lamp_status()

