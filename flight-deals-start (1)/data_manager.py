import requests
from dotenv import load_dotenv
import os
load_dotenv("/Users/justinsilva/Documents/Environ_variables/.env")

HEADER = {
    "Authorization": os.getenv("AUTHORIZATION"),
    "token": os.getenv("TOKEN")

}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.header = HEADER
        self.cities = []



    def get_rows(self):
        response = requests.get("https://api.sheety.co/5be5486c198383c6f462a7bcf915270b/flightDeals/prices", headers=self.header)
        return(response.json())


    def get_cities(self):
        info = self.get_rows()['prices']
        for data in info:
            self.cities.append(data["city"])
        return(self.cities)


    def update_codes(self,code,count):
        url = "https://api.sheety.co/5be5486c198383c6f462a7bcf915270b/flightDeals/prices/"

        body = {
                    "price":
                        {
                            "iataCode": code
                        }
                }

        response = requests.put(f"{url}{count}" ,headers=self.header, json=body)
        response.raise_for_status()

