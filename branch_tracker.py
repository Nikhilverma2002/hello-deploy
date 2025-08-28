import requests
import json

def fetch_all_branches(save_to='data/branches.json'):
    url = "https://www.barbequenation.com/api/v1/get-active-deals/12"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json().get("results", [])
        branches = []

        for branch in data:
            branches.append({
                "branch_id": branch.get("branch_id"),
                "name": branch.get("branch_name"),
                "city": branch.get("city"),
                "state": branch.get("state")
            })

        # Save to file
        with open(save_to, "w") as f:
            json.dump(branches, f, indent=2)

        print(f"{len(branches)} branches fetched and saved to {save_to}")
        return branches

    except Exception as e:
        print("Error fetching branches:", str(e))
        return []
