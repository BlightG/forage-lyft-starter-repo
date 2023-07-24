from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, wear_array):
        self.__wear_array = wear_array

    def needs_service(self):
        sum = 0
        for i in self.__wear_array:
            sum += i
        if sum >= 3:
            return True
        return False
