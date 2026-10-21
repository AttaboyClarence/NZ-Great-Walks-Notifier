import json
from datetime import datetime



def check_availability(data):

    huts = data["GreatWalkFacilityData"]
    for hut in huts:
        if hut["FacilityName"] == "Clinton Hut":
            for night in hut["GreatWalkFacilityDateData"]:
                dateFirst = datetime.fromisoformat(
                    night["ArrivalDate"]
                ).date()

                available = night["TotalAvailable"]


                if available >= 2:
                    print(f"Book Now! There are {available} spaces on {dateFirst}")
                elif available == 1:
                    print(f"Find your wife some nice place to stay for 4 days! You're off on the Milford track!")
                                      