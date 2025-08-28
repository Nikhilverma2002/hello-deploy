# BarbequenationScrap
A professional Scrapper of barbeque nation. Not for public purposes.


## Features

- Fetches buffet data for multiple branches.
- Displays all available slots for each buffet.
- Highlights changes in buffet prices or plans compared to the previous fetch.
- Configurable refresh interval and number of days to fetch.
- Streamlit interface for interactive and scrollable data visualization.

---

## Creation Structure

- `dashboard.py`  
  - Fetches buffet data for each branch and slot.
  - Splits slot timings into individual rows.
  - Highlights price changes compared to the last fetch.
  - Streamlit interface with auto-refresh.

- `main2.py`  
  - Fetches buffet slot data for all slots defined in configuration.
  - Highlights new or updated rows using color coding.
  - Streamlit dashboard with auto-refresh and sidebar controls.

# Installing dependencies
  - pip install -r requirements.txt
  - Dependencies include:

    1. streamlit

    2. pandas

    3. requests
# Running the files
    - Make sure you have the output folder designated within the folder of main files to save the excel files.
    - Streamlit file - dashboard.py - command is streamlit dashboard.py
    - Python file - main2.py - command is python main2.py

# Sidebar Controls

    -Refresh interval: Time in seconds to auto-refresh the data.

    -Days to fetch: Number of days ahead to fetch buffet data for.


# Configuration
    Branches and slots are defined in branches_config

    Add new branches by including the branch ID, name, and slot mappings.

    Each slot has a time and a corresponding slot ID required by the API.

# How It Works

    1. Sends POST requests to the Barbeque Nation API for each branch and slot.

    2. Extracts buffet data from the JSON response.

    3. Expands the remark field into individual slot rows (dashboard.py).

    4. Compares the current fetch with the last fetch to highlight changes.

    5. Displays data interactively in Streamlit, highlighting price updates.

# License

    MIT License © [Divyanshu Anand]
# Configuration
    - Branches and slots are defined in branches_config
    
