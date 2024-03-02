import os
import requests
import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.token = os.environ["TOKEN"]
        self.sheets = os.environ["SHEETS"]
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }
        self.response = requests.get(url=self.sheets)
        self.response.raise_for_status()
        self.data = self.response.json()
        self.data_list = self.data["prices"]

        pprint.pprint(self.data_list)

    def update_sheets(self):
        for city in self.data_list:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.sheets}/{city['id']}",
                json=new_data
            )
            print(response.text)


