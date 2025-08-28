import json
import os

DATA_FILE = "data/previous_data.json"

def has_changed(new_data):
    if not os.path.exists(DATA_FILE):
        return True
    
    with open(DATA_FILE, "r") as f:
        old_data = json.load(f)

    return old_data != new_data

def store_data(new_data):
    with open(DATA_FILE, "w") as f:
        json.dump(new_data, f, indent=2)
