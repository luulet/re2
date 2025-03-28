import requests
import json


def weather(api_key, q):
    base = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": q,
        "appid": api_key,
        "units": "metric"
        "lan": "fin"
    }
    search = requests.get(base, params=params)
    return search.json()

def main():
    api_key = "8096a9dbf4212bdaea977ed635abbbee"
    print(f'Anna kaupunkin nimi, ja ohjelma antaa sinulle kaupungin säätiedot')
    q = input(" > ")

    data = weather(api_key, q)

    print(json.dumps(data, indent=2))

    print(data["main"]["temp"])
    print(data["weather"][0]["description"])

main()