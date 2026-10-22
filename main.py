
import requests
import json
import time
import random
from availability import check_availability

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
def main():



    start = time.perf_counter()

    while True:

        response = requests.post(url, headers=headers, json=payload)

        data = response.json()

        with open("response.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        with open("response.json", "r", encoding="utf-8") as file:
            data = json.load(file)


        check_availability(data)

        
        
        print(response.status_code)

        end = time.perf_counter()

        print(f"Status: {response.status_code}")

        print(f"Request took: {end - start:.2f} seconds")

        delay = random.uniform(6 * 60, 8 * 60)

        print(f"Next check in {delay / 60:.1f} minutes")

        time.sleep(delay)

if __name__ == "__main__":
    main()