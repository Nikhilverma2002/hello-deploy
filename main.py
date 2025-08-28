# from core.request_handler import fetch_slots
# from core.parser import parse_slots
# from core.change_tracker import has_changed, store_data

# def main():
#     # Test with one restaurant for now
#     restaurant_id = 12
#     date = "2025-07-30"
#     reservation_time = "12:00:00"
#     slot_id = 45

#     raw_data = fetch_slots(restaurant_id, reservation_time,date)
#     # raw_data = fetch_slots(restaurant_id, date, dinner_type="LUNCH")

#     parsed_data = parse_slots(raw_data, date)

#     if has_changed(parsed_data):
#         print(" Slot data has changed!")
#         store_data(parsed_data)
#     else:
#         print("No change in data.")

# if __name__ == "__main__":
#     main()

# Below Code snippet working successfully
# import requests
# from core.parser import parse_slots  # Ensure correct relative path if running main.py directly

# url = "https://www.barbequenation.com/api/v1/menu-buffet-price"

# headers = {
#     "Content-Type": "application/json",
#     "User-Agent": "Mozilla/5.0"
# }

# payload = {
#     "branch_id": "12",  # Make sure this is a valid branch ID
#     "reservation_date": "2025-07-30",
#     "reservation_time": "12:00:00",
#     "slot_id": 45
# }

# response = requests.post(url, json=payload, headers=headers)

# if response.status_code == 200:
#     print("Success")
#     data = response.json()
#     slots = parse_slots(data, date=payload["reservation_date"])
#     for slot in slots:
#         print(slot)
# else:
#     print(f"Error {response.status_code}")
#     print(response.text)

# Till here only 

# import json
# from datetime import datetime
# from core.branch_tracker import fetch_all_branches
# from core.request_handler import post_buffet_data
# from core.parser import parse_slots

# OUTPUT_FILE = "output/current_data.json"

# def main():
#     date = datetime.now().strftime("%Y-%m-%d")
#     time = "12:00:00"
#     slot_id = 45  # Can be made dynamic later

#     branches = fetch_all_branches()
#     all_buffet_data = []

#     for branch in branches:
#         print(f"Fetching for {branch['name']} ({branch['city']})...")
#         result = post_buffet_data(branch["branch_id"], date, time, slot_id)

#         if result:
#             parsed = parse_slots(result, date)
#             for entry in parsed:
#                 entry["branch_name"] = branch["name"]
#                 entry["city"] = branch["city"]
#                 all_buffet_data.append(entry)

#     with open(OUTPUT_FILE, "w") as f:
#         json.dump(all_buffet_data, f, indent=2)

#     print(f"\n Scraping complete. {len(all_buffet_data)} entries saved to {OUTPUT_FILE}")

# if __name__ == "__main__":
#     main()


# from core.request_handler import get_all_branches, get_slots, get_deals
# import json
# import os

# OUTPUT_PATH = "output/current_data.json"

# def main():
#     branches = get_all_branches()
#     all_data = []

#     for branch in branches:
#         branch_id = branch.get("id")
#         branch_name = branch.get("name")
#         city = branch.get("city_name")

#         print(f"Processing: {branch_name} ({city}) [ID: {branch_id}]")

#         slots = get_slots(branch_id)
#         deals = get_deals(branch_id)

#         all_data.append({
#             "branch_id": branch_id,
#             "branch_name": branch_name,
#             "city": city,
#             "slots": slots,
#             "deals": deals
#         })

#     os.makedirs("output", exist_ok=True)
#     with open(OUTPUT_PATH, "w") as f:
#         json.dump(all_data, f, indent=2)

#     print(f"\n Done. {len(all_data)} branches saved to {OUTPUT_PATH}")

# if __name__ == "__main__":
#     main()



# from core.branch_finder import find_valid_branches
# import json
# import os

# if __name__ == "__main__":
#     branches = find_valid_branches(start=1, end=100, delay=0.8)

#     output_path = "output/current_data.json"
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)

#     with open(output_path, "w") as f:
#         json.dump(branches, f, indent=2)

#     print(f"\nDone. {len(branches)} valid branches saved to {output_path}")



# import requests
# import json
# import pandas as pd
# from core.parser import parse_slots  # Ensure this is implemented and correctly imports

# url = "https://www.barbequenation.com/api/v1/menu-buffet-price"

# headers = {
#     "Content-Type": "application/json",
#     "User-Agent": "Mozilla/5.0"
# }

# payload = {
#     "branch_id": "12",  # We have to Make sure this is a valid branch ID
#     "reservation_date": "2025-07-30",
#     "reservation_time": "12:00:00",
#     "slot_id": 45
# }

# response = requests.post(url, json=payload, headers=headers)

# if response.status_code == 200:
#     print("Success")

#     data = response.json()

#     # Save raw JSON
#     with open("output/buffet_data.json", "w") as f:
#         json.dump(data, f, indent=2)
#         print("Raw JSON saved to output/buffet_data.json")

#     # Parse slots
#     slots = parse_slots(data, date=payload["reservation_date"])

#     # Save to Excel
#     if slots:
#         df = pd.DataFrame(slots)
#         df.to_excel("output/buffet_slots.xlsx", index=False)
#         print("Parsed slots saved to output/buffet_slots.xlsx")
#     else:
#         print("No slots parsed from response.")
# else:
#     print(f"Error {response.status_code}")
#     print(response.text)




# import requests
# import json
# import pandas as pd
# from datetime import datetime, timedelta
# from core.parser import parse_slots  # Ensure this is implemented and correctly imports

# url = "https://www.barbequenation.com/api/v1/menu-buffet-price"

# headers = {
#     "Content-Type": "application/json",
#     "User-Agent": "Mozilla/5.0"
# }

# # Get user input for start date
# start_date_str = input("Enter start date (YYYY-MM-DD): ")
# start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

# all_slots = []

# for i in range(30):  # Loop through 30 days
#     current_date = start_date + timedelta(days=i)
#     current_date_str = current_date.strftime("%Y-%m-%d")

#     payload = {
#         "branch_id": "12",  # Ensure this is a valid branch ID
#         "reservation_date": current_date_str,
#         "reservation_time": "12:00:00",
#         "slot_id": 45
#     }

#     response = requests.post(url, json=payload, headers=headers)

#     if response.status_code == 200:
#         print(f" Data fetched for {current_date_str}")

#         data = response.json()

#         # Save raw JSON (optional: can be saved per day if needed)
#         with open("output/buffet_data.json", "w") as f:
#             json.dump(data, f, indent=2)

#         # Parse and append slots
#         slots = parse_slots(data, date=current_date_str)
#         if slots:
#             all_slots.extend(slots)
#         else:
#             print(f" No slots for {current_date_str}")
#     else:
#         print(f" Error {response.status_code} for {current_date_str}")

# # Save all collected slots to Excel
# if all_slots:
#     df = pd.DataFrame(all_slots)
#     df.to_excel("output/buffet_slots.xlsx", index=False)
#     print(" All parsed slots saved to output/buffet_slots.xlsx")
# else:
#     print(" No slot data was parsed in the entire range.")


# import requests
# import json
# import pandas as pd
# from datetime import datetime, timedelta
# from core.parser import parse_slots  # Ensure this exists

# url = "https://www.barbequenation.com/api/v1/menu-buffet-price"

# headers = {
#     "Content-Type": "application/json",
#     "User-Agent": "Mozilla/5.0"
# }

# # Input start date
# start_date_str = input("Enter start date (YYYY-MM-DD): ")
# try:
#     start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
# except ValueError:
#     print(" Invalid date format. Use YYYY-MM-DD.")
#     exit()

# # Time slots (12:00 PM to 10:30 PM, every 30 minutes)
# time_slots = [
#     f"{hour:02d}:{minute:02d}:00"
#     for hour in range(12, 23)
#     for minute in (0, 30)
# ]

# all_slots = []

# for day_offset in range(30):  # Loop over 30 days
#     current_date = start_date + timedelta(days=day_offset)
#     date_str = current_date.strftime("%Y-%m-%d")

#     for time_str in time_slots:
#         payload = {
#             "branch_id": "12",  #  Branch id to be worked later on making it dynamic
#             "reservation_date": date_str,
#             "reservation_time": time_str,
#             "slot_id": 45  # Adjustment needed after 30 days 
#         }

#         try:
#             response = requests.post(url, json=payload, headers=headers)
#             if response.status_code == 200:
#                 data = response.json()
#                 slots = parse_slots(data, date=date_str)

#                 if slots:
#                     for slot in slots:
#                         slot["reservation_time"] = time_str
#                     all_slots.extend(slots)
#                     print(f" Fetched for {date_str} {time_str}")
#                 else:
#                     print(f" No slots found for {date_str} {time_str}")
#             else:
#                 print(f" Error {response.status_code} for {date_str} {time_str}")
#         except Exception as e:
#             print(f" Exception for {date_str} {time_str}: {e}")

# # Save final result
# if all_slots:
#     df = pd.DataFrame(all_slots)
#     df.to_excel("output/buffet_slots.xlsx", index=False)
#     print(" All parsed slots saved to output/buffet_slots.xlsx")
# else:
#     print(" No valid slot data collected.")


# ============================ Code to bring the data ============================================================================
import requests
import json
import pandas as pd
from datetime import datetime, timedelta
from core.parser import parse_slots

# URL & headers
url = "https://www.barbequenation.com/api/v1/menu-buffet-price"
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

# Slot ID mapping by time
time_slot_id_map = {
    "12:00:00": 1105, "12:30:00": 1105, "13:00:00": 1105, "13:30:00": 1105,
    "14:00:00": 1105, "14:30:00": 1106, "15:00:00": 1106, "15:30:00": 1106,
    "16:00:00": 1106, "16:30:00": 1106, "17:00:00": 1106, "17:30:00": 1106,
    "18:00:00": 1106, "18:30:00": 1107, "19:00:00": 1107, "19:30:00": 1107,
    "20:00:00": 1107, "20:30:00": 1107, "21:00:00": 1108, "21:30:00": 1108,
    "22:00:00": 1108, "22:30:00": 1108
}

# Input start date
start_date_str = input("Enter start date (YYYY-MM-DD): ")
try:
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
except ValueError:
    print("Invalid date format. Use YYYY-MM-DD.")
    exit()

# Time slots
time_slots = list(time_slot_id_map.keys())

# Collect data
all_slots = []

for day_offset in range(1):  # Can increase this for more days
    current_date = start_date + timedelta(days=day_offset)
    date_str = current_date.strftime("%Y-%m-%d")

    for time_str in time_slots:
        slot_id = time_slot_id_map.get(time_str)
        payload = {
            "branch_id": "171",
            "reservation_date": date_str,
            "reservation_time": time_str,
            "slot_id": slot_id
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                slots = parse_slots(data, date=date_str)

                if slots:
                    for slot in slots:
                        slot["reservation_time"] = time_str
                    all_slots.extend(slots)
                    print(f"Fetched for {date_str} {time_str}")
                else:
                    print(f"No slots found for {date_str} {time_str}")
            else:
                print(f"Error {response.status_code} for {date_str} {time_str}")
        except Exception as e:
            print(f"Exception for {date_str} {time_str}: {e}")

# Save results
if all_slots:
    df = pd.DataFrame(all_slots)
    df.to_excel("output/buffet_slots.xlsx", index=False)
    print("All parsed slots saved to output/buffet_slots.xlsx")
else:
    print("No valid slot data collected.")


# ================ Intelligence to bring the data and then every time crross check it ==========================================
# import requests
# import json
# import pandas as pd
# import time
# from datetime import datetime, timedelta
# from core.parser import parse_slots

# # URL & headers
# url = "https://www.barbequenation.com/api/v1/menu-buffet-price"
# headers = {
#     "Content-Type": "application/json",
#     "User-Agent": "Mozilla/5.0"
# }

# # Slot ID mapping by time
# time_slot_id_map = {
#     "12:00:00": 1105, "12:30:00": 1105, "13:00:00": 1105, "13:30:00": 1105,
#     "14:00:00": 1105, "14:30:00": 1106, "15:00:00": 1106, "15:30:00": 1106,
#     "16:00:00": 1106, "16:30:00": 1106, "17:00:00": 1106, "17:30:00": 1106,
#     "18:00:00": 1106, "18:30:00": 1107, "19:00:00": 1107, "19:30:00": 1107,
#     "20:00:00": 1107, "20:30:00": 1107, "21:00:00": 1108, "21:30:00": 1108,
#     "22:00:00": 1108, "22:30:00": 1108
# }

# # Input start date
# start_date_str = input("Enter start date (YYYY-MM-DD): ")
# try:
#     start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
# except ValueError:
#     print("Invalid date format. Use YYYY-MM-DD.")
#     exit()

# # Time slots
# time_slots = list(time_slot_id_map.keys())

# # Function to fetch slot data
# def fetch_slots(date_str):
#     all_slots = []
#     for time_str in time_slots:
#         slot_id = time_slot_id_map.get(time_str)
#         payload = {
#             "branch_id": "171",
#             "reservation_date": date_str,
#             "reservation_time": time_str,
#             "slot_id": slot_id
#         }

#         try:
#             response = requests.post(url, json=payload, headers=headers)
#             if response.status_code == 200:
#                 data = response.json()
#                 slots = parse_slots(data, date=date_str)

#                 if slots:
#                     for slot in slots:
#                         slot["reservation_time"] = time_str
#                     all_slots.extend(slots)
#             else:
#                 print(f"Error {response.status_code} for {date_str} {time_str}")
#         except Exception as e:
#             print(f"Exception for {date_str} {time_str}: {e}")
#     return pd.DataFrame(all_slots) if all_slots else pd.DataFrame()

# # Monitoring loop
# previous_df = pd.DataFrame()
# date_str = start_date.strftime("%Y-%m-%d")

# print("Starting continuous monitoring... (Ctrl+C to stop)")
# while True:
#     current_df = fetch_slots(date_str)

#     if not current_df.empty:
#         if previous_df.empty:
#             print("Initial data fetched.")
#             previous_df = current_df
#             current_df.to_excel("output/buffet_slots.xlsx", index=False)

#         else:
#             # Compare with previous
#             if not current_df.equals(previous_df):
#                 print(f"Change detected at {datetime.now().strftime('%H:%M:%S')}!")

#                 # Find differences
#                 diff = pd.concat([previous_df, current_df]).drop_duplicates(keep=False)

#                 print("Changes:")
#                 print(diff)

#                 # Save updated data
#                 current_df.to_excel("output/buffet_slots.xlsx", index=False)

#                 previous_df = current_df
#             else:
#                 print(f"No change at {datetime.now().strftime('%H:%M:%S')}")

#     else:
#         print("No valid slot data found.")

#     time.sleep(60)  # check every 60 sec


# =================== Code with INTELLIGENCE AND MULTIPLE city targeting feature harcoded turned into software later. ===================================
#  ================================ This code sucks===================================================
# """
# Multi-Branch Buffet Slot Monitor
# Author: Divyanshu Anand
# Description:
#     - Reads branch/slot config
#     - Polls API for all branches/slots
#     - Saves initial snapshot to Excel (with baseAmount & totalAmount)
#     - Continuously monitors & logs changes
# """

# import os
# import time
# import json
# import requests
# import pandas as pd
# from datetime import datetime, timedelta

# # ===============================
# # CONFIGURATION
# # ===============================
# branches_config = {
#     "171": {
#         "name": "Koramangala",
#         "slots": {
#             "12:00:00": 1105, "12:30:00": 1105, "13:00:00": 1105,
#             "13:30:00": 1105, "14:00:00": 1105, "14:30:00": 1106,
#             "15:00:00": 1106, "15:30:00": 1106, "16:00:00": 1106,
#             "16:30:00": 1106, "17:00:00": 1106, "17:30:00": 1106,
#             "18:00:00": 1106, "18:30:00": 1107, "19:00:00": 1107,
#             "19:30:00": 1107, "20:00:00": 1107, "20:30:00": 1107,
#             "21:00:00": 1108, "21:30:00": 1108, "22:00:00": 1108,
#             "22:30:00": 1108
#         }
#     },
#     "133": {
#         "name": "Rukmani Colony AS Rao Nagar Hyderabad",
#         "slots": {
#             "12:00:00": 740, "12:30:00": 740, "13:00:00": 740,
#             "13:30:00": 740, "14:00:00": 740, "14:30:00": 741,
#             "15:00:00": 741, "15:30:00": 741, "16:00:00": 741,
#             "16:30:00": 741, "17:00:00": 741, "17:30:00": 741,
#             "18:00:00": 741, "18:30:00": 742, "19:00:00": 742,
#             "19:30:00": 742, "20:00:00": 742, "20:30:00": 742,
#             "21:00:00": 743, "21:30:00": 743, "22:00:00": 743,
#             "22:30:00": 743
#         }
#     }
#     # ...will add the rest after the test
# }

# URL = "https://www.barbequenation.com/api/v1/menu-buffet-price"
# HEADERS = {
#     "Content-Type": "application/json",
#     "User-Agent": "Mozilla/5.0"
# }

# OUTPUT_DIR = "output"
# SNAPSHOT_FILE = os.path.join(OUTPUT_DIR, "buffet_snapshot.xlsx")
# CHANGELOG_FILE = os.path.join(OUTPUT_DIR, "buffet_changelog.csv")

# POLL_INTERVAL = 60  # seconds
# DAYS_TO_CHECK = 1   # how many future days

# os.makedirs(OUTPUT_DIR, exist_ok=True)

# # ===============================
# # FUNCTIONS
# # ===============================
# def fetch_branch_slots(branch_id, branch_cfg, date_str):
#     rows = []
#     for time_str, slot_id in branch_cfg["slots"].items():
#         payload = {
#             "branch_id": branch_id,
#             "reservation_date": date_str,
#             "reservation_time": time_str,
#             "slot_id": slot_id,
#         }
#         try:
#             r = requests.post(URL, json=payload, headers=HEADERS, timeout=15)
#             if r.status_code == 200:
#                 data = r.json()
#                 price_data = data.get("data", {}).get("price", [])

#                 # Ensuring it's always iterable
#                 if isinstance(price_data, dict):
#                     price_data = [price_data]

#                 for p in price_data:
#                     rows.append({
#                         "Location": branch_cfg["name"],
#                         "Date": date_str,
#                         "Time": time_str,
#                         "Customer Type": p.get("customerType"),
#                         "Food Type": p.get("foodType"),
#                         "Base Amount (₹)": p.get("baseAmount"),
#                         "Total Amount (₹)": p.get("totalAmount"),
#                         "Branch ID": branch_id,
#                         "Slot ID": slot_id,
#                         "Logged At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                     })
#             else:
#                 print(f"[{branch_id}] HTTP {r.status_code} for {date_str} {time_str}")
#         except Exception as e:
#             print(f"[{branch_id}] ERROR {date_str} {time_str}: {e}")
#     return rows


# def fetch_all(date_str):
#     all_rows = []
#     for branch_id, cfg in branches_config.items():
#         rows = fetch_branch_slots(branch_id, cfg, date_str)
#         all_rows.extend(rows)
#     return pd.DataFrame(all_rows)


# def build_snapshot(start_date, days):
#     dfs = []
#     for offset in range(days):
#         d = (start_date + timedelta(days=offset)).strftime("%Y-%m-%d")
#         df = fetch_all(d)
#         if not df.empty:
#             dfs.append(df)
#     return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()


# def diff_snapshots(prev_df, curr_df):
#     if prev_df.empty and curr_df.empty:
#         return pd.DataFrame()

#     prev = prev_df.fillna("")
#     curr = curr_df.fillna("")

#     key_cols = ["Branch ID", "Date", "Time", "Slot ID", "Customer Type", "Food Type"]

#     merged = prev.merge(curr, on=key_cols, how="outer", suffixes=("_prev", "_curr"), indicator=True)
#     changes = []

#     for _, row in merged.iterrows():
#         entry = {k: row[k] for k in key_cols}
#         entry["Location"] = row.get("Location_curr") or row.get("Location_prev")
#         entry["Base Amount Before"] = row.get("Base Amount (₹)_prev")
#         entry["Base Amount After"] = row.get("Base Amount (₹)_curr")
#         entry["Total Amount Before"] = row.get("Total Amount (₹)_prev")
#         entry["Total Amount After"] = row.get("Total Amount (₹)_curr")
#         entry["Change Type"] = row["_merge"]
#         entry["Detected At"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         changes.append(entry)

#     return pd.DataFrame(changes)


# def append_changelog(diff_df):
#     if diff_df.empty:
#         return
#     file_exists = os.path.isfile(CHANGELOG_FILE)
#     diff_df.to_csv(CHANGELOG_FILE, mode="a", header=not file_exists, index=False, encoding="utf-8")
#     print(f"[LOG] {len(diff_df)} change(s) saved.")


# # ===============================
# # MAIN LOOP
# # ===============================
# def main():
#     start_date_str = input("Enter start date (YYYY-MM-DD): ").strip()
#     start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

#     print("Building initial snapshot...")
#     prev_snapshot = build_snapshot(start_date, DAYS_TO_CHECK)
#     if not prev_snapshot.empty:
#         prev_snapshot.to_excel(SNAPSHOT_FILE, index=False)
#         print(f"Initial snapshot saved: {SNAPSHOT_FILE}")

#     while True:
#         try:
#             curr_snapshot = build_snapshot(start_date, DAYS_TO_CHECK)
#             if curr_snapshot.equals(prev_snapshot):
#                 print(f"[{datetime.now().strftime('%H:%M:%S')}] No changes.")
#             else:
#                 diff_df = diff_snapshots(prev_snapshot, curr_snapshot)
#                 if not diff_df.empty:
#                     append_changelog(diff_df)
#                     print(f"[{datetime.now().strftime('%H:%M:%S')}] Changes detected.")
#                 curr_snapshot.to_excel(SNAPSHOT_FILE, index=False)
#                 prev_snapshot = curr_snapshot
#         except KeyboardInterrupt:
#             print("Stopped by user.")
#             break
#         except Exception as e:
#             print("Loop error:", e)

#         time.sleep(POLL_INTERVAL)


# if __name__ == "__main__":
#     main()



#  =============================== Code with dashboard as well as excel to work on =========================================================================
# """
# Multi-Branch Buffet Slot Monitor — FIXED
# Author: Divyanshu Anand (+ ChatGPT)

# What this does
# --------------
# 1) Reads branch/slot config (city/mall names + slot IDs)
# 2) Polls the official API for each branch/slot across N upcoming days
# 3) Writes a clean Excel snapshot (baseAmount, cgst, sgst, discount, totalAmount)
# 4) Detects changes and appends them to a CSV changelog (only when values actually change)
# 5) Safe against empty API responses; won’t overwrite Excel with empty frames

# How to run
# ----------
# 1) pip install -U requests pandas openpyxl
# 2) python monitor.py  (press Enter for today, or type YYYY-MM-DD)

# Optional: Open the Streamlit dashboard (see dashboard.py below)
# 3) pip install streamlit
# 4) streamlit run dashboard.py
# """

# import os
# import time
# import json
# import requests
# import pandas as pd
# from datetime import datetime, timedelta
# from typing import List, Dict

# # ===============================
# # CONFIGURATION
# # ===============================
# branches_config: Dict[str, Dict] = {
#     "171": {
#         "name": "Koramangala",
#         "slots": {
#             "12:00:00": 1105, "12:30:00": 1105, "13:00:00": 1105,
#             "13:30:00": 1105, "14:00:00": 1105, "14:30:00": 1106,
#             "15:00:00": 1106, "15:30:00": 1106, "16:00:00": 1106,
#             "16:30:00": 1106, "17:00:00": 1106, "17:30:00": 1106,
#             "18:00:00": 1106, "18:30:00": 1107, "19:00:00": 1107,
#             "19:30:00": 1107, "20:00:00": 1107, "20:30:00": 1107,
#             "21:00:00": 1108, "21:30:00": 1108, "22:00:00": 1108,
#             "22:30:00": 1108
#         }
#     },
#     "133": {
#         "name": "Rukmani Colony AS Rao Nagar Hyderabad",
#         "slots": {
#             "12:00:00": 740, "12:30:00": 740, "13:00:00": 740,
#             "13:30:00": 740, "14:00:00": 740, "14:30:00": 741,
#             "15:00:00": 741, "15:30:00": 741, "16:00:00": 741,
#             "16:30:00": 741, "17:00:00": 741, "17:30:00": 741,
#             "18:00:00": 741, "18:30:00": 742, "19:00:00": 742,
#             "19:30:00": 742, "20:00:00": 742, "20:30:00": 742,
#             "21:00:00": 743, "21:30:00": 743, "22:00:00": 743,
#             "22:30:00": 743
#         }
#     }
#     # ... add more branches as needed
# }

# URL = "https://www.barbequenation.com/api/v1/menu-buffet-price"
# HEADERS = {
#     "Content-Type": "application/json",
#     "User-Agent": "Mozilla/5.0"
# }

# OUTPUT_DIR = "output"
# SNAPSHOT_FILE = os.path.join(OUTPUT_DIR, "buffet_snapshot.xlsx")
# CHANGELOG_FILE = os.path.join(OUTPUT_DIR, "buffet_changelog.csv")

# POLL_INTERVAL = 60  # seconds between polling cycles
# DAYS_TO_CHECK = 1   # how many future days to include (starting from start_date)
# TIMEOUT_SECS = 15

# # Ensure output folder exists
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# # Columns we care about when comparing snapshots (ignore Logged At)
# SNAPSHOT_COLUMNS: List[str] = [
#     "Location", "Branch ID", "Slot ID", "Date", "Time",
#     "Customer Type", "Food Type",
#     "Base Amount (₹)", "CGST (₹)", "SGST (₹)", "Discount (₹)", "Total Amount (₹)"
# ]

# KEY_COLS: List[str] = [
#     "Branch ID", "Date", "Time", "Slot ID", "Customer Type", "Food Type"
# ]

# AMOUNT_COLS: List[str] = [
#     "Base Amount (₹)", "CGST (₹)", "SGST (₹)", "Discount (₹)", "Total Amount (₹)"
# ]

# # ===============================
# # HELPERS
# # ===============================

# def save_snapshot(df: pd.DataFrame, filename: str) -> None:
#     if df.empty:
#         print("⚠ No data to save in snapshot (empty DataFrame). Skipping Excel write.")
#         return
#     # Keep consistent column order
#     for col in SNAPSHOT_COLUMNS + ["Logged At"]:
#         if col not in df.columns:
#             df[col] = None
#     ordered = df[SNAPSHOT_COLUMNS + ["Logged At"]].copy()
#     try:
#         ordered.to_excel(filename, index=False, engine="openpyxl")
#         print(f"✅ Snapshot saved: {filename}")
#     except Exception as e:
#         print(f"❌ Failed to save snapshot Excel: {e}")


# def fetch_branch_slots(branch_id: str, branch_cfg: Dict, date_str: str) -> List[Dict]:
#     rows: List[Dict] = []
#     for time_str, slot_id in branch_cfg["slots"].items():
#         payload = {
#             "branch_id": branch_id,
#             "reservation_date": date_str,
#             "reservation_time": time_str,
#             "slot_id": slot_id,
#         }
#         try:
#             r = requests.post(URL, json=payload, headers=HEADERS, timeout=TIMEOUT_SECS)
#             if r.status_code != 200:
#                 print(f"[{branch_id}] HTTP {r.status_code} for {date_str} {time_str}")
#                 continue

#             data = r.json() if r.content else {}
#             price_data = (data.get("data", {}) or {}).get("price", [])

#             # Normalize to list
#             if isinstance(price_data, dict):
#                 price_data = [price_data]
#             if not isinstance(price_data, list):
#                 price_data = []

#             for p in price_data:
#                 base = p.get("baseAmount")
#                 cgst = p.get("cgst")
#                 sgst = p.get("sgst")
#                 discount = p.get("discount")
#                 total = p.get("totalAmount")

#                 # Fallback: if total is missing but we have base/taxes/discount
#                 try:
#                     if total in (None, "") and base is not None:
#                         base_v = float(base)
#                         cgst_v = float(cgst or 0)
#                         sgst_v = float(sgst or 0)
#                         disc_v = float(discount or 0)
#                         total = round(base_v + cgst_v + sgst_v - disc_v, 2)
#                 except Exception:
#                     pass

#                 rows.append({
#                     "Location": branch_cfg["name"],
#                     "Date": date_str,
#                     "Time": time_str,
#                     "Customer Type": p.get("customerType"),
#                     "Food Type": p.get("foodType"),
#                     "Base Amount (₹)": base,
#                     "CGST (₹)": cgst,
#                     "SGST (₹)": sgst,
#                     "Discount (₹)": discount,
#                     "Total Amount (₹)": total,
#                     "Branch ID": branch_id,
#                     "Slot ID": slot_id,
#                     "Logged At": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 })
#         except Exception as e:
#             print(f"[{branch_id}] ERROR {date_str} {time_str}: {e}")
#     return rows


# def fetch_all(date_str: str) -> pd.DataFrame:
#     all_rows: List[Dict] = []
#     for branch_id, cfg in branches_config.items():
#         all_rows.extend(fetch_branch_slots(branch_id, cfg, date_str))
#     df = pd.DataFrame(all_rows)
#     if df.empty:
#         return df
#     # Ensure consistent columns & order
#     for col in SNAPSHOT_COLUMNS + ["Logged At"]:
#         if col not in df.columns:
#             df[col] = None
#     df = df[SNAPSHOT_COLUMNS + ["Logged At"]]
#     # Drop duplicates, keep last logged
#     df = df.sort_values("Logged At").drop_duplicates(subset=KEY_COLS, keep="last")
#     return df.reset_index(drop=True)


# def build_snapshot(start_date: datetime, days: int) -> pd.DataFrame:
#     dfs = []
#     for offset in range(days):
#         d = (start_date + timedelta(days=offset)).strftime("%Y-%m-%d")
#         df = fetch_all(d)
#         if not df.empty:
#             dfs.append(df)
#     if not dfs:
#         return pd.DataFrame(columns=SNAPSHOT_COLUMNS + ["Logged At"])  # empty but with schema
#     combined = pd.concat(dfs, ignore_index=True)
#     # Ensure one row per KEY_COLS (latest Logged At wins)
#     combined = combined.sort_values("Logged At").drop_duplicates(subset=KEY_COLS, keep="last")
#     # Order columns
#     combined = combined[SNAPSHOT_COLUMNS + ["Logged At"]]
#     return combined.reset_index(drop=True)


# def snapshots_equal(prev_df: pd.DataFrame, curr_df: pd.DataFrame) -> bool:
#     prev = (prev_df or pd.DataFrame()).copy()
#     curr = (curr_df or pd.DataFrame()).copy()
#     prev = prev.reindex(columns=SNAPSHOT_COLUMNS).fillna("").sort_values(KEY_COLS).reset_index(drop=True)
#     curr = curr.reindex(columns=SNAPSHOT_COLUMNS).fillna("").sort_values(KEY_COLS).reset_index(drop=True)
#     try:
#         return prev.equals(curr)
#     except Exception:
#         return False


# def diff_snapshots(prev_df: pd.DataFrame, curr_df: pd.DataFrame) -> pd.DataFrame:
#     if (prev_df is None or prev_df.empty) and (curr_df is None or curr_df.empty):
#         return pd.DataFrame()

#     prev = prev_df.reindex(columns=SNAPSHOT_COLUMNS).fillna("")
#     curr = curr_df.reindex(columns=SNAPSHOT_COLUMNS).fillna("")

#     merged = prev.merge(curr, on=KEY_COLS, how="outer", suffixes=("_prev", "_curr"), indicator=True)

#     changes = []
#     now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     for _, row in merged.iterrows():
#         state = row["_merge"]
#         location = row.get("Location_curr") or row.get("Location_prev")

#         # Added rows
#         if state == "right_only":
#             entry = {k: row[k] for k in KEY_COLS}
#             entry.update({
#                 "Location": location,
#                 "Change Type": "added",
#                 "Base Amount Before": None,
#                 "Base Amount After": row.get("Base Amount (₹)_curr"),
#                 "Total Amount Before": None,
#                 "Total Amount After": row.get("Total Amount (₹)_curr"),
#                 "CGST Before": None,
#                 "CGST After": row.get("CGST (₹)_curr"),
#                 "SGST Before": None,
#                 "SGST After": row.get("SGST (₹)_curr"),
#                 "Discount Before": None,
#                 "Discount After": row.get("Discount (₹)_curr"),
#                 "Detected At": now_str,
#             })
#             changes.append(entry)
#             continue

#         # Removed rows
#         if state == "left_only":
#             entry = {k: row[k] for k in KEY_COLS}
#             entry.update({
#                 "Location": location,
#                 "Change Type": "removed",
#                 "Base Amount Before": row.get("Base Amount (₹)_prev"),
#                 "Base Amount After": None,
#                 "Total Amount Before": row.get("Total Amount (₹)_prev"),
#                 "Total Amount After": None,
#                 "CGST Before": row.get("CGST (₹)_prev"),
#                 "CGST After": None,
#                 "SGST Before": row.get("SGST (₹)_prev"),
#                 "SGST After": None,
#                 "Discount Before": row.get("Discount (₹)_prev"),
#                 "Discount After": None,
#                 "Detected At": now_str,
#             })
#             changes.append(entry)
#             continue

#         # Present in both — check value diffs only
#         diffs = {}
#         for col in AMOUNT_COLS:
#             a = row.get(f"{col}_prev")
#             b = row.get(f"{col}_curr")
#             if str(a) != str(b):
#                 diffs[col] = (a, b)
#         if diffs:
#             entry = {k: row[k] for k in KEY_COLS}
#             entry.update({
#                 "Location": location,
#                 "Change Type": "updated",
#                 "Base Amount Before": row.get("Base Amount (₹)_prev"),
#                 "Base Amount After": row.get("Base Amount (₹)_curr"),
#                 "Total Amount Before": row.get("Total Amount (₹)_prev"),
#                 "Total Amount After": row.get("Total Amount (₹)_curr"),
#                 "CGST Before": row.get("CGST (₹)_prev"),
#                 "CGST After": row.get("CGST (₹)_curr"),
#                 "SGST Before": row.get("SGST (₹)_prev"),
#                 "SGST After": row.get("SGST (₹)_curr"),
#                 "Discount Before": row.get("Discount (₹)_prev"),
#                 "Discount After": row.get("Discount (₹)_curr"),
#                 "Detected At": now_str,
#             })
#             changes.append(entry)

#     return pd.DataFrame(changes)


# def append_changelog(diff_df: pd.DataFrame) -> None:
#     if diff_df is None or diff_df.empty:
#         return
#     file_exists = os.path.isfile(CHANGELOG_FILE)
#     try:
#         diff_df.to_csv(CHANGELOG_FILE, mode="a", header=not file_exists, index=False, encoding="utf-8")
#         print(f"📝 Logged {len(diff_df)} change(s) → {CHANGELOG_FILE}")
#     except Exception as e:
#         print(f"❌ Failed to append changelog: {e}")


# # ===============================
# # MAIN LOOP
# # ===============================

# def main():
#     try:
#         start_date_str = input("Enter start date (YYYY-MM-DD) [blank = today]: ").strip()
#     except Exception:
#         start_date_str = ""

#     if not start_date_str:
#         start_date = datetime.now()
#     else:
#         start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

#     print("\nBuilding initial snapshot…")
#     prev_snapshot = build_snapshot(start_date, DAYS_TO_CHECK)
#     if not prev_snapshot.empty:
#         save_snapshot(prev_snapshot, SNAPSHOT_FILE)
#     else:
#         print("⚠ Initial snapshot is empty. Will still monitor and save when data appears.")

#     while True:
#         try:
#             curr_snapshot = build_snapshot(start_date, DAYS_TO_CHECK)

#             if snapshots_equal(prev_snapshot, curr_snapshot):
#                 print(f"[{datetime.now().strftime('%H:%M:%S')}] No changes.")
#             else:
#                 diff_df = diff_snapshots(prev_snapshot, curr_snapshot)
#                 if not diff_df.empty:
#                     append_changelog(diff_df)
#                     print(f"[{datetime.now().strftime('%H:%M:%S')}] Changes detected and logged.")
#                 save_snapshot(curr_snapshot, SNAPSHOT_FILE)
#                 prev_snapshot = curr_snapshot
#         except KeyboardInterrupt:
#             print("\nStopped by user.")
#             break
#         except Exception as e:
#             print("Loop error:", e)

#         time.sleep(POLL_INTERVAL)


# if __name__ == "__main__":
#     main()
