import requests

api_key = "YOUR_API_KEY"
city = "Delhi"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

res = requests.get(url)
data = res.json()

print(data["weather"][0]["description"])