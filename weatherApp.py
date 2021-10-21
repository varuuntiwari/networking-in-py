import requests

# Username: public_api
# Email: satruyaydu@yevme.com
# Password: abcdefgh1

API_KEY = "d437009152d470751c5b42639497a43e"

def callAPI(key):
    url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+key
    data = requests.get(url).json()
    return data

city = input("Enter name of city to get weather: ")

data = callAPI(city)
temp = data['main']['temp'] - 273.15
print(f'''The temperature in {city} is {temp:.2f} C°. The weather looks {data['weather'][0]['main']}
and the description is {data['weather'][0]['description']}. The humidity is {data['main']['humidity']}.''')