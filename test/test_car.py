import unittest
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class TestCaoulet(unittest.TestCase):
    def test_capulet_needs_service(self):
        engine = CapuletEngine(40000, 0)
        self.assertTrue(engine.needs_service())

    def test_capulet_doesnt_need_service(self):
        engine = CapuletEngine(20000, 0)
        self.assertFalse(engine.needs_service())


class TestWilloughby(unittest.TestCase):
    def test_willoughby_needs_service(self):
        engine = WilloughbyEngine(70000, 0)
        self.assertTrue(engine.needs_service())

    def test_willpughby_doesnt_need_service(self):
        engine = WilloughbyEngine(20000, 0)
        self.assertFalse(engine.needs_service())


class Teststrenman(unittest.TestCase):
    def test_sternman_needs_service(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_sternman_doesnt_need_service(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())


class Testspindler(unittest.TestCase):
    def test_spindler_battery_needs_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - 4)
        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_doesnt_need_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - 2)
        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class Testnubbin(unittest.TestCase):
    def test_nubbin_battery_needs_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - 5)
        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_doesnt_need_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - 2)
        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class Testcarrigan(unittest.TestCase):
    def test_carrigan_tires_needs_service(self):
        wear_array = [0.3, 0.95, 0.3, 0.3]
        tire = CarriganTires(wear_array)
        self.assertTrue(tire.needs_service())

    def test_carrigan_tires_doesnt_need_service(self):
        wear_array = [0.3, 0.35, 0.3, 0.3]
        tire = CarriganTires(wear_array)
        self.assertFalse(tire.needs_service())


class Testoctoprime(unittest.TestCase):
    def test_octoprime_tires_needs_service(self):
        wear_array = [0.8, 0.95, 0.8, 0.8]
        tire = OctoprimeTires(wear_array)
        self.assertTrue(tire.needs_service())

    def test_carrigan_tires_doesnt_need_service(self):
        wear_array = [0.3, 0.35, 0.3, 0.3]
        tire = OctoprimeTires(wear_array)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
