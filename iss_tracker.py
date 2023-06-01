import requests
from datetime import datetime

MY_LAT = 40.759781
MY_LONG = -73.817299
UTC_OFFSET = 4

def can_see_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response)
    # print(response.status_code)

    # if response.status_code == 404:
    #     raise Exception("That resource does not exist.")
    # elif response.status_code == 401:
    #     raise Exception("You are not authorized to access this data.")
    response.raise_for_status() #This captures all error responeses instead of having to type if ...etc
    data = response.json()

    position = data['iss_position']
    iss_lat = float(position['latitude'])
    iss_long = float(position['longitude'])

    #position within +5 or -5 degrees of iss position
    if MY_LAT -5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG - 5:
        return True
    # return False

def is_night():
    parameters = {
        # Got these from latlong.net
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0]) - UTC_OFFSET
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0]) - UTC_OFFSET

    if sunrise < 0:
        sunrise += 24
    if sunset < 0:
        sunset += 24

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True