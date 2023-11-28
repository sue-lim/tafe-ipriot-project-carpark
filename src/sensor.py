class Sensor:
    """Provide sensors to detect cars"""
    def __init__(self, id, car_park , is_active = False, ):
        self.id = id
        self.car_park = car_park
        self.is_active = is_active or False

    def __str__(self):
        return f"{self.id}: Sensor is {'is active' if self.is_active else 'if active'}"

class EntrySensor(Sensor):
    ...

class ExitSensor(Sensor):
    ...