# https://api.openweathermap.org/data/2.5/weather?appid=********************&q=Kolkata
# Please replace the 'appid' with your own 'appid'
import requests
res = requests.get('https://ipinfo.io/').json()

api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=*****************&units=metric&q='
# api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=***************&q='
url = api_address + res['city']
json_data = requests.get(url).json()
weatherinfo = json_data['weather'][0]['main']
weatherdes = json_data['weather'][0]['description']
currenttemp = json_data['main']['temp']
feels_like = json_data['main']['feels_like']
temp_min = json_data['main']['temp_min']
temp_max = json_data['main']['temp_max']
print(json_data)
print(weatherinfo)
print(weatherdes)
print(f' current temperature is {currenttemp} degree celsius')
print(f' It feels like {feels_like} degree celsius')
print(f' minimum temperature is {temp_min} degree celsius')
print(f'maximum temperature is {temp_max} degree celsius')
