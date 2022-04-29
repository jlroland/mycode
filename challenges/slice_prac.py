#!/usr/bin/python3

import requests

URL= "http://api.open-notify.org/astros.json"
loc_url = "http://api.open-notify.org/iss-now.json"

def main():
    # requests.get() requests info from the URL
    # .json() method transforms that data into a Pythonic dictionary!
    sliceme = requests.get(URL).json()
    loc_slice = requests.get(loc_url).json()
    #print(sliceme)
    #print(type(sliceme))
    #print(loc_slice)
    print(f"People in Space:  {sliceme['number']}")
    
    for person in sliceme['people']:
        print(f"{person['name']} is on the {person['craft']}")
    
    print(f"\nCURRENT LOCATION OF THE ISS:\nLon: {loc_slice['iss_position']['longitude']}\nLat: {loc_slice['iss_position']['latitude']}")
main()

