import json
from datetime import datetime
import requests
from telegram_message import send_message





def check_availability(data):

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
        print("Try again later!")
        '''send_message(
                    "Even though you haven't yet got space for the Milford trail.\n"
                    "Remember, all you need to be content is here.\n "
                    "You have your Lilly ❤️"
                )                     
        '''
