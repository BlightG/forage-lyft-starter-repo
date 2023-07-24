from battery.battery import Battery


class NubbinBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.__last_service_date = last_service_date
        self.__currnet_date = current_date

    def needs_service(self):
        service_threshold_date = self.__last_service_date.replace(
            year=self.__last_service_date.year + 4)
        if service_threshold_date < self.__currnet_date:
            return True
        else:
            return False
