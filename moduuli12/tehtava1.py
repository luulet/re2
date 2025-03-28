import requests
import json

pyynto = "https://api.chucknorris.io/jokes/random"
print(requests.get(pyynto).json()["value"])




