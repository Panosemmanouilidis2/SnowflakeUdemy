import requests
import json
from datetime import datetime
from snowflake.snowpark import Session
import snowflake.connector
import sys
import pytz
import logging
# initiate logging at info level
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(levelname)s - %(message)s')

# Set the IST time zone
ist_timezone = pytz.timezone('America/New_York')

# Get the current time in IST
current_time_ist = datetime.now(ist_timezone)

# Format the timestamp
timestamp = current_time_ist.strftime('%Y_%m_%d_%H_%M_%S')
# Create the file name
file_name = f'air_quality_data_{timestamp}.json'

today_string = current_time_ist.strftime('%Y_%m_%d')
# Following credential has to come using secret whie running in automated way
def snowpark_basic_auth():
    connection_parameters = {
       user:"PANOSEMMANOUILIDIS",
       password:"PANAGIOTIS79",
       account:"ca51374.europe-west2.gcp",
       warehouse:"LOAD_WH",
       database:"DEV_DB",
       schema:"STAGE_SCH",
       role:"SYSADMIN",
       authenticator:"snowflake"
    }
    # creating snowflake session object
    return Session.builder.configs(connection_parameters).create()
    import requests
import json
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

def get_air_quality_data(api_key, cities):
    api_url = 'https://api.weatherbit.io/v2.0/current'
    
    all_city_data = {}  # Dictionary to store results for each city

    for city in cities:
        params = {
            'key': api_key,  
            'format': 'json',
            'city': city  # Fetch data for each city
        }

        headers = {
            'accept': 'application/json'
        }

        try:
            # Make the GET request
            response = requests.get(api_url, params=params, headers=headers)

            logging.info(f'Got response for {city}, checking status code...')

            if response.status_code == 200:
                logging.info(f'Successfully retrieved data for {city}')
                json_data = response.json()

                # Store data in dictionary
                all_city_data[city] = json_data

            else:
                logging.error(f"Error fetching data for {city}: {response.status_code} - {response.text}")

        except Exception as e:
            logging.error(f"An error occurred while fetching data for {city}: {e}")

    # Save all data to a JSON file
    file_name = "air_quality_data.json"
    with open(file_name, 'w') as json_file:
        json.dump(all_city_data, json_file, indent=2)

    logging.info(f'All data written to {file_name}')
    return all_city_data

# Function to print available cities from the response
def print_available_cities(air_quality_data):
    print("\nCities included in the response:")
    for city in air_quality_data.keys():
        print(f"- {city}")

# Replace with your actual API key
api_key = 'd7e70465170641e087c7ccefe8b87ec6'

# List of cities to fetch data for
cities = ['London', 'New York', 'Paris', 'Tokyo', 'Delhi']

# Fetch air quality data for multiple cities
air_quality_data = get_air_quality_data(api_key, cities)

# Print available cities
print_available_cities(air_quality_data)
from snowflake.snowpark import Session

def snowflake_connection():
    connection_parameters = {
        "user": "PANOSEMMANOUILIDIS",
        "account": "CA51374.europe-west2.gcp",
        "password": "Panagiotis79",
        "warehouse": "LOAD_WH",
        "database": "DEV_DB",
        "schema": "STAGE_SCH",
        "role": "SYSADMIN",
        "authenticator": "snowflake"  # Required for MFA
    }
    return Session.builder.configs(connection_parameters).create()

# Test connection
sf_session = snowflake_connection()
print(sf_session.sql("SELECT CURRENT_VERSION()").collect())
