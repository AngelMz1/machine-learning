'''
Dev. Angel muñoz
Script description
Get and read data from nasa API about space
NAsa Api: https://api.nasa.gov/
https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={FA3OhznLAkrWIdOn1jiCvS6F2cc7zuJMKtj6T7dr}
'''

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
        print(data)
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
            
API_KEY = 'FA3OhznLAkrWIdOn1jiCvS6F2cc7zuJMKtj6T7dr'
get_nasa_data(API_KEY)
