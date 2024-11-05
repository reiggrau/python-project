class Vehicle:
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_maker_model(self):
        print(f"I'm a {self.maker} {self.model}.")


my_car = Vehicle('Ford', 'Fusion')

# print(my_car.maker)
# print(my_car.model)
my_car.moves()
my_car.get_maker_model()

your_car = Vehicle('Renault', 'Clio')
your_car.get_maker_model()

# Inheritance


class GolfCart(Vehicle):
    pass  # Inherit everything as it is


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")  # Modifies the method


class Airplane(Vehicle):
    def __init__(self, maker, model, faa_id):
        super().__init__(maker, model)  # Inherit everything from parent
        self.faa_id = faa_id  # Add a new property

    def moves(self):
        print(f"{self.faa_id} flies along...")


my_cart = GolfCart('Yamaha', 'GC100')
my_truck = Truck('Mack', 'Pinnacle')
my_airplane = Airplane('Cessna', 'Skyhawk', 'N-12345')

my_cart.moves()
my_truck.moves()
my_airplane.moves()

# Polymorphism
# methods/functions/operators with the same name that can be executed on many objects or classes
for v in (my_car, your_car, my_cart, my_truck, my_airplane):
    v.get_maker_model()
    v.moves()

mytuple = ("apple", "banana", "cherry")

print(len(mytuple))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(len(thisdict))
