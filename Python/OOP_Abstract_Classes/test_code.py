# The parent class
class Amenity:
    def __init__(self, is_running):
        self.is_running = is_running

    def set_is_running(self, currently_running):
        self.is_running = currently_running
        print(f"{self} is running: {self.is_running}")


# Children classes. We first use the __init__ method to add properties to the class, and
# the super().__init__ method to inherit all the parents class functionality
class Gas(Amenity):
    def __init__(self, is_running, cubic_feet):
        self.cubic_feet = cubic_feet
        super().__init__(is_running)

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.cubic_feet}/cuft of gas>"


class Electricity(Amenity):
    def __init__(self, is_running, watts):
        self.watts = watts
        super().__init__(is_running)

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.watts}/watts of electricity>"


class Water(Amenity):
    def __init__(self, is_running, gallons):
        self.gallons = gallons
        super().__init__(is_running)

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.gallons}/gallons of water>"


# Driver Code
g = Gas(False, 236)
e = Electricity(False, 104.2)
w = Water(True, 16)
g.set_is_running(True)
g.set_is_running(False)
e.set_is_running(True)
e.set_is_running(False)
w.set_is_running(True)
w.set_is_running(False)

# We import ABC and abstractmethod from the abc module
from abc import ABC, abstractmethod


# Amenity becomes our abstract base class (ABC)
class Amenity(ABC):
    def turn_on(self):
        pass


# We extend our ABC to three new child classes
class Electricity(Amenity):
    def turn_on(self):
        print("You flipped the light switch!")


class Water(Amenity):
    def turn_on(self):
        print("You pressed the faucet up!")


class Gas(Amenity):
    def turn_on(self):
        print("You turned the knob on the stovefront!")


# Driver code
W = Electricity()
W.turn_on()
E = Water()
E.turn_on()
G = Gas()
G.turn_on()


# Define two classes that have similar implementation and therefore can be mixed and matched in an iteration.
class Gas:
    def __init__(self, price, unit):
        self.price = price
        self.unit = unit

    def info(self):
        print(f"I am gas. My price is {self.price}, measured in {self.unit}.")

    def make_sound(self):
        print("psssssssssssssss")


class Water:
    def __init__(self, price, unit):
        self.price = price
        self.unit = unit

    def info(self):
        print(f"I am water. My price is {self.price}, measured in {self.unit}.")

    def make_sound(self):
        print("whooooooosh")


# Driver Code
g = Gas(0.43, 'cu/ft')
w = Water(0.075, 'gallons')
for amenity in (g, w):
    amenity.make_sound()
    amenity.info()

