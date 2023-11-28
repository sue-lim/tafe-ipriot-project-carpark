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

    def register(self, component):
        """ Registers component of a carpark"""
        # if  it's not either a Sensor or a Display, throw an error
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type!")

        # otherwise if it's a Sensor, append to Sensors
        if isinstance(component, Sensor):
            self.sensors.append(component)
        # else, it's a Display, append to Displays
        elif isinstance(component, Display):
            self.displays.append(component)

    def __str__(self):
        return f"Welcome to car park at {self.location}, with {self.capacity} bays."
        # def __str__ returns a string containing the car park's location and capacity
