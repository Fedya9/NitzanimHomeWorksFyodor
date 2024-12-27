class Person:
    def __init__(self, name, age, address):
        """אתחול פרטי אדם."""
        self.name = name
        self.age = age
        self.address = address
        self.children = []

    def add_child(self, name_child):

        self.children.append(name_child.name)

    def print_details(self):

        print(f"Name of person: {self.name}")
        print(f"Age of person: {self.age}")
        print(f"Address of person: {self.address}")
        print("Names of children:")
        if self.children:
            for child in self.children:
                print(f"- {child}")
        else:
            print("no children")


gau = Person("gau", 14, "tel aviv")
gal = Person("gal", 23, "yafo")
yoav = Person("yoav", 60, "yafo")
yoav.add_child(gau)
yoav.add_child(gal)
golda=Person("golda",0,"tel aviv")
yoav.add_child(golda)
yoav.print_details()