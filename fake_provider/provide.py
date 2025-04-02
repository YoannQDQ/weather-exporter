import math
import time
from random import randint, random

import requests

BASE_URL = "http://localhost:8083/weatherstation/updateweatherstation.php?"

PARAMS = {
    "ID": "station-id8",
    "PASSWORD": "password",
    "action": "updateraww",
    "realtime": 1,
    "rtfreq": 5,
    "dateutc": "now",
    "baromin": 30.23,
    "tempf": 37.5,
    "dewptf": 36.6,
    "humidity": 97,
    "windspeedmph": 0.0,
    "windgustmph": 0.0,
    "winddir": 306,
    "rainin": 0.09,
    "dailyrainin": 0.45,
    "solarradiation": 0.0,
    "UV": 0.0,
    "indoortempf": 65.4,
    "indoorhumidity": 50,
}
"ID=station-id8&PASSWORD=password&action=updateraww&realtime=1&rtfreq=5&dateutc=now&baromin=30.23&tempf=37.5&dewptf=36.6&humidity=97&windspeedmph=0.0&windgustmph=0.0&winddir=306&rainin=0.09&dailyrainin=0.45&solarradiation=0.0&UV=0.0&indoortempf=65.4&indoorhumidity=50"


def build_url(params):
    """
    Build the URL with the given parameters.
    """
    return BASE_URL + "&".join(f"{key}={value}" for key, value in params.items())


def cycle(time_s, min_val, max_val, cycle=300, randomness=0.05):
    t = time_s % cycle
    theta = math.pi * 2 * (t / cycle)
    return (
        min_val + (max_val - min_val) * (math.sin(theta) + 1) / 2 + (random() - 0.5) * (max_val - min_val) * randomness
    )


if __name__ == "__main__":
    p = PARAMS.copy()
    i = 0
    while True:
        t = time.time()
        p["tempf"] = cycle(t, 30, 70)
        p["indoortempf"] = cycle(t, 60, 65, randomness=0)
        p["humidity"] = cycle(t, 30, 70, randomness=0.2)
        p["winddir"] = p["winddir"] + randint(-1, 1)
        p["windspeedmph"] = randint(0, 10)
        url = build_url(p)
        print(requests.get(url))
        time.sleep(1)
