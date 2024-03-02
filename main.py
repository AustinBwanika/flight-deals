#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import flight_search
import notification_manager
from data_manager import DataManager
from flight_search import FlightSearch, check_flights
from flight_data import FlightData
from notification_manager import NotificationManager
import pprint
from datetime import *

sheet_manager = DataManager()
flight_search_manager = FlightSearch()

ORIGIN_CITY_IATA = "LON"

# sheet data has a data type of a list
sheet_data = sheet_manager.data["prices"]
city_names = [sheet_manager.data["prices"][i]["city"] for i in range(0, len(sheet_data))]

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search_manager.return_code(row["city"])

        sheet_manager.data = sheet_data
        sheet_manager.update_sheets()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )