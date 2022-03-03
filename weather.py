import json
import requests

def get_weather_desc_and_temp():

    api_key = 'd970ad78f6ff7d691c26c4d610556580'
    city = 'Orlando'
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()
    # print(json)

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {
        "description": description,
        "temp_min": temp_min,
        "temp_max": temp_max
    }
   

def main():
    get_weather_info = get_weather_desc_and_temp()
    print("Today's forecast is", get_weather_info.get("description"))
    print("the minimum temperature is", get_weather_info.get("temp_min"))
    print("the maximum temperature is", get_weather_info.get("temp_max"))

main()