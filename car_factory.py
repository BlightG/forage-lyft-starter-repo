from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
from car import Car


class CarFactory():

    @staticmethod
    def create_calliope(current_date,
                        last_service_date,
                        current_mileage,
                        last_service_mileage,
                        wear_array, tire_type):

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)

        if tire_type == "carrigan":
            tire = CarriganTires(wear_array)
        elif tire_type == "octoprime":
            tire = OctoprimeTires(wear_array)
        else:
            raise TypeError('tire type must be "carrigan" or "octoprime"')

        return Car(engine, battery, tire)

    @staticmethod
    def create_glissade(current_date,
                        last_service_date,
                        current_mileage,
                        last_service_mileage,
                        wear_array, tire_type):

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)

        if tire_type == "carrigan":
            tire = CarriganTires(wear_array)
        elif tire_type == "octoprime":
            tire = OctoprimeTires(wear_array)
        else:
            raise TypeError('tire type must be "carrigan" or "octoprime"')

        return Car(engine, battery, tire)

    @staticmethod
    def create_palindrome(current_date,
                          last_service_date,
                          warning_light_is_on,
                          wear_array, tire_type):

        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)

        if tire_type == "carrigan":
            tire = CarriganTires(wear_array)
        elif tire_type == "octoprime":
            tire = OctoprimeTires(wear_array)
        else:
            raise TypeError('tire type must be "carrigan" or "octoprime"')

        return Car(engine, battery, tire)

    @staticmethod
    def create_rorschach(current_date,
                         last_service_date,
                         current_mileage,
                         last_service_mileage,
                         wear_array, tire_type):

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)

        if tire_type == "carrigan":
            tire = CarriganTires(wear_array)
        elif tire_type == "octoprime":
            tire = OctoprimeTires(wear_array)
        else:
            raise TypeError('tire type must be "carrigan" or "octoprime"')

        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex(current_date,
                      last_service_date,
                      current_mileage,
                      last_service_mileage,
                      wear_array, tire_type):

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)

        if tire_type == "carrigan":
            tire = CarriganTires(wear_array)
        elif tire_type == "octoprime":
            tire = OctoprimeTires(wear_array)
        else:
            raise TypeError('tire type must be "carrigan" or "octoprime"')

        return Car(engine, battery, tire)
