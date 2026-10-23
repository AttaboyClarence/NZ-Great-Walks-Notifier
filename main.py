
import requests
import json
import time
import random
from availability import initialise_Milford
from availability import initialise_Routeburn

def main():



    

    while True:

        start = time.perf_counter()
    
        initialise_Milford()

        initialise_Routeburn()
        
        delay = random.uniform(6 * 90, 11 * 60)

        print(f"Next check in {delay / 60:.2f} minutes")

        end = time.perf_counter()

        print(f"Request took: {end - start:.2f} seconds")

        time.sleep(delay)

if __name__ == "__main__":
    main()