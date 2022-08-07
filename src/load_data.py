import requests
import os
from pathlib import Path
import json

endpoint = os.environ['ENDPOINT']
# "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json"
mapping_endpoint = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"

def load_exchange_rates():
    response = requests.get(endpoint)
    return response.json()

def load_currency_mappings():
    response = requests.get(mapping_endpoint)
    return response.json()


def save(response):
    date = response['date']
    folder_name = Path(date.replace("-", "_"))
    folder_name.mkdir(parents=True, exist_ok=True)
    with open(folder_name/f"response.json", "w") as json_writer:
        json.dump(response, json_writer)


if __name__ == "__main__":
    data = load_exchange_rates()
    mappings = load_currency_mappings()
    print(data)
    save(data)
