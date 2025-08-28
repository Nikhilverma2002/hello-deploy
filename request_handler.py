# import requests
# from datetime import datetime

# API_URL = "https://www.barbequenation.com/api/v1/menu-buffet-price"

# def fetch_slots(restaurant_id,  reservation_time, date=None):
#     if not date:
#         date = datetime.now().strftime("%Y-%m-%d")

#     headers = {
#         "Content-Type": "application/json",
#         "Referer": "https://www.barbequenation.com/",
#         "Origin": "https://www.barbequenation.com",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
#     }

#     payload = {
#         "reservation_date": date,
#         "branch_id": str(restaurant_id),  # Send as string for safety
#         "dinner_type": "LUNCH",  # Required field
#         "reservation_time": str(reservation_time),
#         "slot_id": 45
#     }

#     response = requests.post(API_URL, json=payload, headers=headers)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error: {response.status_code}")
#         print(response.text)
#         return None


# Updated code of fetchingthe slot
# import requests
# from datetime import datetime

# BASE_URL = "https://www.barbequenation.com/api/v1"

# HEADERS = {
#     "Content-Type": "application/json",
#     "Referer": "https://www.barbequenation.com/",
#     "Origin": "https://www.barbequenation.com",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
# }

# def get_available_slots(branch_id, date):
#     url = f"{BASE_URL}/time-slot"
#     payload = {
#         "reservation_date": date,
#         "branch_id": str(branch_id),
#         "dinner_type": "LUNCH"
#     }

#     response = requests.post(url, json=payload, headers=HEADERS)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"[Error] {response.status_code} while getting slots")
#         print(response.text)
#         return None

# def fetch_slot_price(branch_id, reservation_time, slot_id, date):
#     url = f"{BASE_URL}/menu-buffet-price"
#     payload = {
#         "reservation_date": date,
#         "branch_id": str(branch_id),
#         "dinner_type": "LUNCH",
#         "reservation_time": reservation_time,
#         "slot_id": slot_id
#     }

#     response = requests.post(url, json=payload, headers=HEADERS)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"[Error] {response.status_code} while fetching price")
#         print(response.text)
#         return None



# import requests

# HEADERS = {
#     "Content-Type": "application/json",
#     "User-Agent": "Mozilla/5.0"
# }

# def post_buffet_data(branch_id, date, time, slot_id):
#     url = "https://www.barbequenation.com/api/v1/menu-buffet-price"
#     payload = {
#         "branch_id": str(branch_id),
#         "reservation_date": date,
#         "reservation_time": time,
#         "slot_id": slot_id
#     }

#     response = requests.post(url, json=payload, headers=HEADERS)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Failed for branch_id={branch_id} (status {response.status_code})")
#         return None


import requests
from datetime import date

def get_all_branches():
    url = "https://api.barbequenation.com/api/v2/outlet/outlet-list"
    try:
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        res.raise_for_status()
        return res.json().get("data", [])
    except Exception as e:
        print(f"Error getting branches: {e}")
        return []

def get_slots(branch_id):
    url = "https://www.barbequenation.com/api/v1/slots"
    payload = {
        "branch_id": str(branch_id),
        "reservation_date": str(date.today())
    }
    try:
        res = requests.post(url, json=payload, headers={"User-Agent": "Mozilla/5.0"})
        res.raise_for_status()
        return res.json().get("data", [])
    except Exception as e:
        print(f"Error getting slots for branch {branch_id}: {e}")
        return []

def get_deals(branch_id):
    url = f"https://www.barbequenation.com/api/v1/get-active-deals/{branch_id}"
    try:
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        res.raise_for_status()
        return res.json().get("data", [])
    except Exception as e:
        print(f"Error getting deals for branch {branch_id}: {e}")
        return []
