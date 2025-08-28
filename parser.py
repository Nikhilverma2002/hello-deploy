# def parse_slots(response_data, date):
#     if not response_data or "data" not in response_data:
#         return []

#     slots = response_data["data"].get("time_slots", [])
#     parsed = []

#     for slot in slots:
#         parsed.append({
#             "date": date,
#             "start_time": slot.get("start_time"),
#             "end_time": slot.get("end_time"),
#             "cost": slot.get("price"),
#             "status": slot.get("status")
#         })

#     return parsed


# def parse_slots(response_data, date=None):
#     buffet_data = response_data.get("results", {}).get("buffets", {}).get("buffet_data", [])
#     parsed = []

#     for item in buffet_data:
#         parsed.append({
#             "branch_id": item.get("branchId"),
#             "day": item.get("weekDays", {}).get("day"),
#             "period": item.get("period", {}).get("periodName"),
#             "customer_type": item.get("customerType"),
#             "food_type": item.get("foodType"),
#             "price": item.get("totalAmount"),
#             "from_time": item.get("slotTimingFrom"),
#             "to_time": item.get("slotTimingTo"),
#             "from_date": item.get("fromDate"),
#             "to_date": item.get("toDate"),
#             "display_name": item.get("displayName")
#         })

#     return parsed


# core/parser.py

# def parse_slots(data, date):
#     """
#     Parses slot data from the BBQ Nation API response.
    
#     Parameters:
#         data (dict): JSON response from the API.
#         date (str): The reservation date for the slot (YYYY-MM-DD).
    
#     Returns:
#         List[dict]: A list of parsed slot information.
#     """
#     parsed = []

#     try:
#         if not data.get("data"):
#             return []

#         for item in data["data"]:
#             slot_info = {
#                 "reservation_date": date,
#                 "slot_id": item.get("slot_id"),
#                 "slot_time": item.get("slot_time"),
#                 "price": item.get("price"),
#                 "branch_id": item.get("branch_id"),
#                 "availability": item.get("available"),
#                 "meal_type": item.get("meal_type"),  # e.g., lunch/dinner
#                 "menu_type": item.get("menu_type"),  # e.g., veg/non-veg
#                 "person_count": item.get("person_count", None)
#             }
#             parsed.append(slot_info)
#     except Exception as e:
#         print(f"Parsing error: {e}")
    
#     return parsed


# core/parser.py

# def parse_slots(data, date=None):
#     if not data or not isinstance(data, dict):
#         return []

#     result = []

#     try:
#         for item in data.get("data", []):
#             result.append({
#                 "date": date,
#                 "name": item.get("name"),
#                 "price": item.get("price"),
#                 "slot_id": item.get("slot_id"),
#                 "start_time": item.get("start_time"),
#                 "end_time": item.get("end_time"),
#             })
#     except Exception as e:
#         print(f"Error parsing slots: {e}")

#     return result



# import requests

# def get_slot_ids(branch_id, date, time):
#     """
#     Fetch available slot IDs for a given branch, date, and time.
#     """
#     url = "https://www.barbequenation.com/api/v1/slot-availability"

#     payload = {
#         "branch_id": branch_id,
#         "reservation_date": date,
#         "reservation_time": time
#     }

#     headers = {
#         "Content-Type": "application/json",
#         "User-Agent": "Mozilla/5.0"
#     }

#     try:
#         response = requests.post(url, json=payload, headers=headers)
#         if response.status_code == 200:
#             data = response.json()
#             return [slot["id"] for slot in data.get("data", []) if "id" in slot]
#         else:
#             print(f"  get_slot_ids() failed with status {response.status_code} for {date} {time}")
#             return []
#     except Exception as e:
#         print(f"Exception in get_slot_ids(): {e}")
#         return []



# parser.py

# def parse_slots(data, date=None):
#     result = []

#     # Assuming 'data' contains keys like: 'adult_price', 'child_price', etc.
#     # Modify based on actual API response structure
#     try:
#         if "data" in data and isinstance(data["data"], dict):
#             entry = data["data"]

#             parsed = {
#                 "date": date,
#                 "adult_price": entry.get("adult_price"),
#                 "child_price": entry.get("child_price"),
#                 "veg_price": entry.get("veg_price"),
#                 "nonveg_price": entry.get("nonveg_price"),
#                 "discount": entry.get("discount"),
#                 "branch_id": entry.get("branch_id"),
#                 "remarks": entry.get("remarks")
#             }

#             result.append(parsed)
#     except Exception as e:
#         print(f" Parsing error: {e}")

#     return result




# parser.py

def parse_slots(data, date=None):
    result = []

    try:
        buffet_items = data.get("results", {}).get("buffets", {}).get("buffet_data", [])

        for item in buffet_items:
            result.append({
                "date": date,
                "branch_id": item.get("branchId"),
                "food_type": item.get("foodType"),
                "customer_type": item.get("customerType"),
                "base_amount": item.get("baseAmount"),
                "total_amount": item.get("totalAmount"),
                "discount": item.get("discount"),
                "slot_from": item.get("slotTimingFrom"),
                "slot_to": item.get("slotTimingTo"),
                "available_timings": item.get("remark"),  # Pipe-separated available times
                "price_type": item.get("priceType"),
                "display_name": item.get("displayName"),
                "reservation_type": item.get("reservationType", {}).get("reservationTypeDesc")
            })
    except Exception as e:
        print(f"⚠️ Error parsing data: {e}")

    return result
