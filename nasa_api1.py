'''
Dev. Angel muñoz
Script description
Get and read data from nasa API about space
NAsa Api: https://api.nasa.gov/
https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={FA3OhznLAkrWIdOn1jiCvS6F2cc7zuJMKtj6T7dr}'''
import os
import requests

os.system('clear')
def get_nasa_data(API_KEY):
    print('::: Welcome to nasa api :::')
    url = f'https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={API_KEY}'

    try:
        #api request
        response = requests.get(url)
        response.raise_for_status()
        #read data
        data = response.json()
        #challenge api nasa
        name = data.get("name")
        abs_magnitude = data.get("absolute_magnitude_h")
        diam_km = data["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
        diam_ft = data["estimated_diameter"]["feet"]["estimated_diameter_max"]
        print(f"Nombre del cometa: {name}")
        print(f"Magnitud absoluta h: {abs_magnitude}")
        print(f"Diámetro máximo estimado (km): {diam_km}")
        print(f"Diámetro máximo estimado (ft): {diam_ft}")
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
            
API_KEY = 'FA3OhznLAkrWIdOn1jiCvS6F2cc7zuJMKtj6T7dr'
get_nasa_data(API_KEY)
