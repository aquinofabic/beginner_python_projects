import requests  # module allows to send HTTP requests over to python

api_key_2 = '78c6bcb4a66344859f80385138fe0a20'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key_2}")


# print(weather_data.status_code) #200 means the API is authorised and working
# json() converts to a human-readable format - converts data structures into JSON strings
# print(weather_data.json())

if weather_data.json()['cod'] == '404':
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    # 1. Access 'weather' key
    # 2. Access the list of dictionaries, first and only dictionary to access [0]
    # 3. Access 'main' key

    temp = weather_data.json()['main']['temp']
    # 1 Access 'main' key
    # 2 Access 'temp' key

    wind_chill = weather_data.json()['main']['feels_like']
    humidity = weather_data.json()['main']['humidity']
    weather_description = weather_data.json()['weather'][0]['description']
    min_temp = weather_data.json()['main']['temp_min']
    max_temp = weather_data.json()['main']['temp_max']
    wind_speed = round(weather_data.json()['wind']['speed']*1.60934)
    wind_direction = weather_data.json()['wind']['deg']

    print(f"Looking up in {user_input} there are: {weather_description}")
    print(f"The temperature is {temp}°C but feels like {wind_chill}°C, with a humidity of {humidity}%")
    print(f"The temperature ranges from {min_temp}°C to {max_temp}°C")
    print(f"The wind is blowing at {wind_speed}kph, {wind_direction}° from North")


# f-strings provide a concise, convenient way to embed python expressions inside string literals for formatting
# Now write code for the case if there are no cities. if and else statement starting line 15
# Remember to do pip install requests in terminal