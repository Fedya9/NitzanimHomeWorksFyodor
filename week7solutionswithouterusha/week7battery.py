class Battery:
    def __init__(self):
        self.percentage = 100

    def get_percentage(self):
        return self.percentage

    def set_percentage(self, percentage):
        self.percentage = percentage

    def use_battery(self, percentage_to_use):
        if self.percentage >= percentage_to_use:
            self.percentage -= percentage_to_use
            print(self.percentage)
        else:
            print("battery low")


b = Battery()
b.use_battery(50)
b.use_battery(65)
print(b.get_percentage())
