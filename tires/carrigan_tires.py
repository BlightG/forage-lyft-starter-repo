from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, wear_array):
        self.__wear_array = wear_array

    def needs_service(self):
        for i in self.__wear_array:
            if i >= 0.9:
                return True
        return False
