import requests
import json

# Fetch data from API
response = requests.get('https://randomuser.me/api/?results=20')

# Parse JSON data
data = json.loads(response.text)

# Loop through each user
for user in data['results']:
    # Get first and last name
    first_name = user['name']['first']
    last_name = user['name']['last']
    
    # Get name of street from location
    street_name = user['location']['street']['name']
    
    # Print first and last name, and street name
    print(f"{last_name}, {first_name}")
    print(street_name)
