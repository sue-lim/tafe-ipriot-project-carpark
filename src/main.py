from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
car_park = CarPark(location="Moondalup", capacity=100, log_file="moondalup.txt")
print(car_park)

# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(id=1, is_active=True, car_park=CarPark)
print(entry_sensor)

# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(id=2, is_active=False, car_park=CarPark)
print(exit_sensor)

# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=CarPark)
print(display)

# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
entry_sensor = EntrySensor(id=1, car_park=car_park, is_active=True)
# ensure the entry_sensor instance is initialised and parameters are set to be utilised
for entering_cars in range(10):
    entry_sensor.detect_vehicle()

# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
exit_sensor = ExitSensor(id=1, car_park=car_park, is_active=True)
# ensure the exit_sensor instance is initialised and parameters are set to be utilised
for exiting_cars in range(2):
    exit_sensor.detect_vehicle()