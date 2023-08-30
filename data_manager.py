import requests
import os

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
BASIC_AUTH_PARAMS = (USERNAME, PASSWORD)
SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=BASIC_AUTH_PARAMS)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=BASIC_AUTH_PARAMS
            )

    def update_prices(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "lowestPrice": city["lowestPrice"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=BASIC_AUTH_PARAMS
            )
