#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
data_man = DataManager()
flight_man = FlightData()
cities = data_man.get_cities()


count = 2
for city in cities:
    code = flight_man.get_codes(city)
    data_man.update_codes(code, count)
    count += 1





