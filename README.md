# Python & U.S. Census API Starter Project

This is a simple starter script created for a presentation on basic Python, APIs, and the `requests` library.

This script connects to the U.S. Census Bureau's API, fetches the total population for all states from the 2019 American Community Survey (ACS), and then processes and prints the results in a clean, human-readable format.

## Features

  * Demonstrates how to make a `GET` request to a public API.
  * Uses the `requests` library to pass parameters (like variables and geography).
  * Includes a required API key and checks if it's valid.
  * Handles basic error checking for HTTP status codes (200, 401).
  * Parses the JSON response (which is a list of lists).
  * Loops through the data and uses f-strings to print formatted output.

## Requirements

  * Python 3.x
  * The `requests` library

## Setup & Installation

**1. Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

**2. Install Dependencies**

This project requires the `requests` library. You can install it using pip:

```bash
pip install requests
```

(Note: You could also run `pip freeze > requirements.txt` and have users install from that file).

## Configuration: Get Your API Key

This script **will not work** until you provide a valid U.S. Census API key. Getting one is free and immediate.

**Step 1:** Go to the official Census API key signup page:
[https://api.census.gov/data/key\_signup.html](https://api.census.gov/data/key_signup.html)

**Step 2:** Fill out the short form (you can list "Student" or "Developer" for organization).

**Step 3:** Check your email. The Census Bureau will instantly email you a 40-character API key.

**Step 4:** Open the `census_starter.py` file and find this line:

```python
# BEFORE
API_KEY = "PASTE_YOUR_API_KEY_HERE"
```

**Step 5:** Paste your key as a string. It should look like this (this is a fake key):

```python
# AFTER
API_KEY = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
```

## How to Run

Once you have installed `requests` and added your API key, you can run the script from your terminal:

```bash
python census_starter.py
```

## Expected Output

If it's successful, you will see the following in your terminal:

```
Connecting to U.S. Census API...
Success! (Status Code: 200)

--- Processed Population Data ---
State: Alabama            Population: 4,903,185
State: Alaska             Population: 731,545
State: Arizona            Population: 7,278,717
State: Arkansas           Population: 3,017,804
State: California         Population: 39,512,223
State: Colorado           Population: 5,758,736
State: Connecticut        Population: 3,565,287
... (and so on for all states) ...
```

If you see an "ERROR: Please get a valid API key..." message, double-check that you've pasted your key correctly and saved the file.

## Next Steps

This script is just the beginning\! Try to modify it to:

1.  **Get different data:** Look at the [Census ACS 1-Year Variables](https://api.census.gov/data/2019/acs/acs1/variables.html) and try to get a different statistic, like median household income (`B19013_001E`).
2.  **Change the geography:** Instead of `for=state:*`, try getting data for all *counties in one state* (`for=county:*&in=state:06` for California).
3.  **Save the data:** Instead of just printing the data, try writing it to a new CSV file\!
