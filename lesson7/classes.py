class ToyCar:
    def __init__(self, colour):
        self.colour = colour  # Each car has a color

    def honk(self):
        print("Beep beep!")

    def print_colour(self):
        print(self.colour)


car1 = ToyCar("red")
car1.honk()  # Beep beep!
car1.print_colour()  # red

car2 = ToyCar("blue")
car2.honk()  # Beep beep!
car2.print_colour()  # blue
