from sensor import Sensor
from display import Display


class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None,
                 displays=None):  # instead of using plate_list, we have parameter names as plates
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    @property
    # decorator, which allows a methods to act like an attribute
    def available_bays(self):
        # car_park.available_bays
        return self.capacity - len(self.plates)

    def register(self, component):
        """ Registers component of a car park"""
        # if  it's not either a Sensor or a Display, throw an error
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type!")

        # otherwise if it's a Sensor, append to Sensors
        if isinstance(component, Sensor):
            self.sensors.append(component)
        # else, it's a Display, append to Displays
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)

    def update_displays(self):
        for display in self.displays:
            display.update({"Bays": self.available_bays, "Temperature": 42})
            print(f"Updating: {display}")

    def __str__(self):
        return f"Welcome to car park at {self.location}, with {self.capacity} bays."
        # def __str__ returns a string containing the car park's location and capacity
