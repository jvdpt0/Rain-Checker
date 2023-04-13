import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

endpoint = 'https://api.openweathermap.org/data/2.8/onecall'
api_key = os.environ.get("OWM_APIKEY") #Set your own api key
account_sid = "AC0fa2df110cf8cba102dd82a492a289da"
auth_token = os.environ.get('AUTH_TOKEN') #Set your own auth token

parameters = {
    "lat": -18.9893051,
    'lon': -49.4713826,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data['hourly']
hourly_data_slice = hourly_data[0:12]
will_rain = False



for object in hourly_data_slice:
    if object['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's going to rain today, remember to bring an ☂️",
    from_="+15074456521",
    to="+5584999533866"
    )
print(message.status)