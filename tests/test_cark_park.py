import unittest
from car_park import CarPark
from display import Display
from sensor import EntrySensor, ExitSensor


class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    # def test_logging_of_cars_entering_car_park(self):
    #     self.car_park.add_car("NEW-01")
    #     with self.car_park.log_file.open("r") as f:
    #         last_write = f.readlines()[-1]
    #     self.assertIn("NEW-01", last_write)
    #     self.assertIn("entered", last_write)
    #
    # def test_logging_of_cars_existing_car_park(self):
    #     self.car_park.add_car("NEW-01")
    #     self.car_park.remove_car("NEW-01")
    #     with self.car_park.log_file("r") as f:
    #         last_write = f.readlines()[-1]
    #     self.assertIn("NEW-01", last_write)
    #     self.assertIn("exited", last_write)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display(
            1, CarPark("123 Example Street", 100),
            "Welcome to the car park", True
        )

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")


# class TestEntrySensor(unittest.TestCase):
#     def setUp(self):
#         self.sensor = EntrySensor(1, "123 Example Street")
#         # self.sensor = EntrySensor(1, "FAKE-100")
#
#     def test_entry_sensor_initialised_with_all_attributes(self):
#         self.assertIsInstance(self.sensor, EntrySensor)
#         self.assertEqual(self.sensor.car_park, "123 Example Street")
#         self.assertEqual(self.sensor.is_active, False)
#
#     def test_entry_sensor_msg(self):
#         plate = "FAKE-100"
#         expected_msg = f"Incoming vehicle detected. Plate: {plate}"
#         printed_msg = f"Incoming vehicle detected. Plate: {plate}"
#         self.assertEqual(printed_msg, expected_msg)
#
#
# class TestExitSensor(unittest.TestCase):
#     def setUp(self):
#         self.sensor = ExitSensor(1, "123 Example Street")
#         # self.sensor = EntrySensor(1, "FAKE-100")
#
#     def test_exit_sensor_initialised_with_all_attributes(self):
#         self.assertIsInstance(self.sensor, ExitSensor)
#         self.assertEqual(self.sensor.car_park, "123 Example Street")
#         self.assertEqual(self.sensor.is_active, False)
#
#     def test_exit_sensor_msg(self):
#         plate = "FAKE-100"
#         expected_msg = f"Incoming vehicle detected. Plate: {plate}"
#         printed_msg = f"Incoming vehicle detected. Plate: {plate}"
#         self.assertEqual(printed_msg, expected_msg)


if __name__ == "__main__":
    unittest.main()
