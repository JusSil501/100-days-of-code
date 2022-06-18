import requests
from dotenv import load_dotenv
import os
load_dotenv("/Users/justinsilva/Documents/Environ_variables/.env")

URL = "https://tequila-api.kiwi.com"

HEADER = {
    "apikey": os.getenv("API_KEY")
}

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.codes = []


    def get_codes(self, city):
        query = f"term={city}&location_types=city&limit=1&active_only=true"
        response = requests.get(f"{URL}/locations/query?"+query, headers=HEADER)
        data = response.json()
        return data['locations'][0]['code']

