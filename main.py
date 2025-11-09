import requests
import json
import sys # Using sys.exit() for a clean stop

# --- 1. CONFIGURATION ---

# IMPORTANT: Go to https://api.census.gov/data/key_signup.html to get your own free API key.
# Paste your key as a string in the variable below:
API_KEY = "PASTE_YOUR_API_KEY_HERE"

# The base URL for the 2019 1-Year ACS survey
# (ACS = American Community Survey)
base_url = "https://api.census.gov/data/2019/acs/acs1"

# The parameters for our query
# We're "getting" two variables: NAME and the code for Total Population
# We're getting them "for" all states
params = {
    "get": "NAME,B01001_001E",
    "for": "state:*",
    "key": API_KEY  # Pass the API key to the request
}

# --- 2. VALIDATE API KEY ---
if API_KEY == "PASTE_YOUR_API_KEY_HERE":
    print("="*50)
    print("ERROR: Please get a valid API key and paste it into")
    print("       the API_KEY variable at the top of this script.")
    print("Get your key from: https://api.census.gov/data/key_signup.html")
    print("="*50)
    sys.exit() # Stop the script

# --- 3. MAKE THE API CALL ---
print(f"Connecting to U.S. Census API...")
try:
    response = requests.get(base_url, params=params)

    # --- 4. CHECK FOR A GOOD RESPONSE ---
    
    # Check the "status code" of the response.
    # 200 means "OK" / "Success"
    if response.status_code == 200:
        print("Success! (Status Code: 200)")
        
        # .json() parses the JSON text from the response into a Python list of lists.
        data = response.json()
        
        # --- 5. PROCESS AND PRINT THE DATA ---
        print("\n--- Processed Population Data ---")
        
        # The first item (index 0) in the list is the header
        header = data[0]
        
        # All other items (from index 1 to the end) are the data rows
        data_rows = data[1:]
        
        # Loop through each row in the data_rows
        for row in data_rows:
            # Based on our 'get' param, index 0 is NAME, index 1 is B01001_001E
            state_name = row[0]
            population_str = row[1]
            
            # Convert population string to an integer for formatting
            try:
                population_int = int(population_str)
                
                # Print a nicely formatted string!
                # {state_name:<18} left-aligns the state name in a space of 18 chars
                # {population_int:,.0f} formats the integer with commas
                print(f"State: {state_name:<18} Population: {population_int:,.0f}")
                
            except ValueError:
                # Handle cases where data might not be a valid number
                print(f"Could not parse population data for {state_name}")
        
    elif response.status_code == 401:
        # 401 means "Unauthorized"
        print(f"Error: API returned status code {response.status_code} (Unauthorized)")
        print("Please check that your API_KEY is correct and valid.")
        
    else:
        # If the status code was something else, print the error
        print(f"Error: API returned status code {response.status_code}")
        print("Response Text:")
        print(response.text)

except requests.exceptions.RequestException as e:
    # This catches other errors, like no internet connection
    print(f"An error occurred with the request: {e}")
