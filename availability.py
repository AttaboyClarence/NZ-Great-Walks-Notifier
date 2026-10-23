import json
from datetime import datetime
import requests
from telegram_message import send_message



def initialise_Milford():

    url = "https://prod-nz-rdr.recreation-management.tylerapp.com/nzrdr/rdr/search/greatwalkplacefacility"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Referer": "https://bookings.doc.govt.nz/",
        "Origin": "https://bookings.doc.govt.nz",
    }


    payload = {
        "accomodation": "",
        "placeId": 873,
        "customerClassificationId": 0,
        "arrivalDate": "2026-11-29",
        "nights": 18
    }


    response = requests.post(url, headers=headers, json=payload)
    
    data = response.json()

    with open("response_Milford.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Status: {response.status_code}")
    
    check_availability_Milford(data)

def check_availability_Milford(data):

    found = False
    huts = data["GreatWalkFacilityData"]
    for hut in huts:
        if hut["FacilityName"] == "Clinton Hut":
            for night in hut["GreatWalkFacilityDateData"]:
                dateFirst = datetime.fromisoformat(
                    night["ArrivalDate"]
                ).date()

                available = night["TotalAvailable"]


                if available >= 2:

                    found = True
                    print(f"Book Now! There are {available} spaces on {dateFirst}")
                    send_message(f"Book Now! There are {available} spaces on {dateFirst}")
                    break
                
                elif available == 1:
                    print(f"Find your wife some nice place to stay for 4 days! You're off on the Milford track!")
                    send_message(f"Find your wife some nice place to stay for 4 days! You're off on the Milford track! There one slot on {dateFirst}")
                
    if not found:
        print("Try Milford again later!")
        '''send_message(
                    "Even though you haven't yet got space for the Milford trail.\n"
                    "Remember, all you need to be content is here.\n "
                    "You have your Lilly ❤️"
                )                     
        '''

def initialise_Routeburn():

    url = "https://prod-nz-rdr.recreation-management.tylerapp.com/nzrdr/rdr/search/greatwalkplacefacility"

    headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Referer": "https://bookings.doc.govt.nz/",
            "Origin": "https://bookings.doc.govt.nz",
        }
    
    payload = {
            "accomodation": "",
            "placeId": 874,
            "customerClassificationId": 0,
            "arrivalDate": "2026-11-25",
            "nights": 22
        }
    
    response = requests.post(url, headers=headers, json=payload)

    print(f"Status: {response.status_code}")

    data = response.json()

    with open("response_Routeburn.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    check_availability_Routeburn(data)

def check_availability_Routeburn(data):
    start_date = datetime(2026, 11, 25).date()
    end_date = datetime(2026, 12, 17).date()
    allowed_facilities = {
        "Lake Mackenzie Campsite",
        "Lake Mackenzie Hut",
        "Routeburn Falls Hut",
    }

    found = False

    for facility in data["GreatWalkFacilityData"]:
        facility_name = facility["FacilityName"]
        if facility_name not in allowed_facilities:
            continue

        for night in facility["GreatWalkFacilityDateData"]:
            arrival_date = datetime.fromisoformat(night["ArrivalDate"]).date()
            available = night["TotalAvailable"]

            if (
                start_date <= arrival_date <= end_date
                and arrival_date.weekday() not in (4, 5)
                and available >= 2
                
            ):
                found = True
                message = (
                    f"Book Now! Routeburn: There are {available} spaces "
                    f"at {facility_name} on {arrival_date}"
                )
            
                print(message)
                send_message(message)
                
    if not found:
        
        print("Try Routeburn again later!")