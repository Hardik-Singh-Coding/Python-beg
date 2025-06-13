from enum import Enum

city_name = input("Enter your city: ")
temperature = float(input(("Enter temprature: ")))

weather_details = {
    'name': city_name,
    'temp': temperature
}

class weather(Enum):
    COLD = "Weather is cold"
    MODERATE = "Weather is moderate"
    HOT = "Weather is hot"

if temperature > 30:
    w_type = weather.HOT
elif temperature >= 15:
    w_type = weather.MODERATE
elif temperature < 15:
    w_type = weather.COLD

# print(w_type.value)

weather_report = []

weather_report.append({
    'city': weather_details['name'],
    'temperature': weather_details['temp'],
    'message': w_type.value
})

final_report = weather_report[0]

print("Weather: ")
print(f"City: {final_report['city']}")
print(f"Temperature: {final_report['temperature']}")
print(f"{final_report['message']}")