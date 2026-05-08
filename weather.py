import requests
from rich import print

latitude = 13.364047
longtitude = 103.860313
API_URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longtitude={longtitude}&current_weather=true"

response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()
    print("--- Weather fetched succesfully")
    print(f"Siemreap current weather is: {data['current_weather']['temperature']} ")
else:
    print("--- Failed to fetch weather ---")