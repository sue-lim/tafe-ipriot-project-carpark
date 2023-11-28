class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None,
                 displays=None):  # instead of using plate_list, we have parameter names as plates
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"Welcome to car park at {self.location}, with {self.capacity} bays."
        # def __str__ returns a string containing the car park's location and capacity
