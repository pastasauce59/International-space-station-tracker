import requests
from datetime import datetime, timezone

MY_LAT = 40.759781
MY_LONG = -73.817299
UTC_OFFSET = 4

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
iss_long = float(position['longitude'])
iss_lat = float(position['latitude'])

parameters = {
    # Got these from latlong.net
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])


# time_now = datetime.now(timezone.utc)
time_now = datetime.now()
print(sunrise)
print(sunset)
print(time_now.hour)
