import requests
import json
import time

def is_valid_branch(data):
    return "outletName" in data and "city" in data  # adjust based on real API response structure

def find_valid_branches(start=1, end=100, delay=1.0):
    found_branches = []
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for branch_id in range(start, end + 1):
        url = f"https://api.barbequenation.com/api/v2/outlet/outlet-details/{branch_id}"
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if is_valid_branch(data):
                    print(f"[+] Found valid branch: ID {branch_id}")
                    found_branches.append(data)
                else:
                    print(f"[-] Invalid structure at ID {branch_id}")
            else:
                print(f"[-] Branch ID {branch_id} gave status: {response.status_code}")
        except Exception as e:
            print(f"[!] Error on ID {branch_id}: {e}")

        time.sleep(delay)  # Sleep to avoid overwhelming server

    return found_branches
