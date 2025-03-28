import requests
import json


def weather(api_key, q):
    base = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": q,
        "appid": api_key,
        "units": "metric"
    }
    search = requests.get(base, params=params)
    return search.json()

def main():
    api_key = "8096a9dbf4212bdaea977ed635abbbee"
    print(f'Anna kaupunkin nimi, ja ohjelma antaa sinulle kaupungin säätiedot')
    q = input(" > ")

    data = weather(api_key, q)

    print(f'Lämpötila: {data["main"]["temp"]} °C')
    print(f'Sääolosuhde on: {data["weather"][0]["main"]}')

main()