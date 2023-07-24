from abc import ABC, abstractmethod
from serviceable import Serviceable
# from battery.battery import Battery
# from engine.engine import Engine


class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.__engine = engine
        self.__battrey = battery
        self.__tire = tire

    def needs_service(self):
        if self.__engine.needs_service() or self.__battrey.needs_service() or self.__tire.needs_service():
            return True
        else:
            return False
