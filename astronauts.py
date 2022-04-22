import csv
import requests
from pathlib import Path

Path('output').mkdir(parents=True, exist_ok=True)

response = requests.get("http://api.open-notify.org/astros.json")
astronauts = response.json()

with open('output/astronauts.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['name', 'craft'])
    writer.writeheader()
    writer.writerows(astronauts['people'])
