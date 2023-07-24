from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, warning_light_is_on):
        self.__warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.__warning_light_is_on:
            return True
        else:
            return False
