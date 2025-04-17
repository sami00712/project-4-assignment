import requests

city_name = "lahore"
api_key = "c8d79eabdc78dbbb94b765232c252645"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    print("Weather description:", data['weather'][0]['description'])
    print("Current Temperature is:", data['main']['temp'], "°C")
    print("Temperature Feels like:", data['main']['feels_like'], "°C")
    print("Humidity is:", data['main']['humidity'], "%")
else:
    print("Failed to retrieve data. Error code:", response.status_code)
