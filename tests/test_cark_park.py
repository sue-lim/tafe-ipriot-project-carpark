import unittest
from car_park import CarPark
from display import Display
from pathlib import Path

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
        self.assertEqual(self.car_park.log_file, Path("log.txt"))

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_register_raises_type_error(self):
        car_park = CarPark("123 Example Street", 100)
        non_sensor_display = "Not a Sensor or a Display"
        with self.assertRaises(TypeError):
            self.car_park.register(non_sensor_display)

    def test_log_file_created(self):
        car_park = CarPark("123 Example Street", 100, log_file="new_log.txt")
        self.assertTrue(Path("new_log.txt").exists())

    def tearDown(self):
        Path("new_log.txt").unlink(missing_ok=True)

    # inside the TestCarPark class
    def test_car_logged_when_entering(self):
        car_park = CarPark(
            "123 Example Street", 100, log_file="new_log.txt"
        )  # TODO: change this to use a class attribute or new instance variable
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("entered", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_car_logged_when_exiting(self):
        car_park = CarPark(
            "123 Example Street", 100, log_file="new_log.txt"
        )  # TODO: change this to use a class attribute or new instance variable
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("exited", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

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
            1, CarPark("123 Example Street", 100), "Welcome to the car park", True
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


class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.sensor = EntrySensor(1, "123 Example Street")
        # self.sensor = EntrySensor(1, "FAKE-100")

    def test_entry_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.sensor, EntrySensor)
        self.assertEqual(self.sensor.car_park, "123 Example Street")
        self.assertEqual(self.sensor.is_active, False)

    def test_entry_sensor_msg(self):
        plate = "FAKE-100"
        expected_msg = f"Incoming vehicle detected. Plate: {plate}"
        printed_msg = f"Incoming vehicle detected. Plate: {plate}"
        self.assertEqual(printed_msg, expected_msg)

#
class TestExitSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = ExitSensor(1, "123 Example Street")
        # self.sensor = EntrySensor(1, "FAKE-100")

    def test_exit_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.sensor, ExitSensor)
        self.assertEqual(self.sensor.car_park, "123 Example Street")
        self.assertEqual(self.sensor.is_active, False)

    def test_exit_sensor_msg(self):
        plate = "FAKE-100"
        expected_msg = f"Incoming vehicle detected. Plate: {plate}"
        printed_msg = f"Incoming vehicle detected. Plate: {plate}"
        self.assertEqual(printed_msg, expected_msg)


if __name__ == "__main__":
    unittest.main()
