import requests
from flight_data import FlightData
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_API_KEY = "DzqLVa0iq2r2d6khyfZtJhm6PctrS6oE"


class FlightSearch:

# This class is responsible for talking to the Flight Search API.

    def return_code(self, city_name):
        heade = {'apikey': TEQUILA_API_KEY}
        parameters = {
            "term": city_name,
            "location_types": "city",

        }

        response = requests.get(url=TEQUILA_ENDPOINT,params=parameters, headers=heade)
        results = response.json()["locations"]
        response.raise_for_status()
        code = results[0]['code']

        return code


def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
    headers = {"apikey": TEQUILA_API_KEY}
    query = {
        "fly_from": origin_city_code,
        "fly_to": destination_city_code,
        "date_from": from_time.strftime("%d/%m/%Y"),
        "date_to": to_time.strftime("%d/%m/%Y"),
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "max_stopovers": 0,
        "curr": "GBP"
    }

    response = requests.get(
        url=f"{TEQUILA_ENDPOINT}/v2/search",
        headers=headers,
        params=query,
    )

    try:
        data = response.json()["data"][0]
    except IndexError:
        print(f"No flights found for {destination_city_code}.")
        return None

    flight_data = FlightData(
        price=data["price"],
        origin_city=data["route"][0]["cityFrom"],
        origin_airport=data["route"][0]["flyFrom"],
        destination_city=data["route"][0]["cityTo"],
        destination_airport=data["route"][0]["flyTo"],
        out_date=data["route"][0]["local_departure"].split("T")[0],
        return_date=data["route"][1]["local_departure"].split("T")[0]
    )
    print(f"{flight_data.destination_city}: £{flight_data.price}")
    return flight_data






