import datetime, requests
from pandas import concat, DataFrame
from typing import List

from config import API, DATA_TO_INSERT
from modules.transform import Transform

# Creates an object with all API request information
API = API()


# Requests the API
def get_sales():
    response = requests.get(API.ENDPOINT, headers=API.HEADERS, params=API.PARAMS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return None


# Gets a list of the last N days (set it up on config.py)
def get_last_n_days(n: int) -> List[str]:
    today = datetime.date.today()
    return [(today - datetime.timedelta(days=i)).isoformat() for i in range(n)]


def extract():
    seen_ids = set()
    # Repeats extraction for each day
    for date in get_last_n_days(API.DAYS_TO_EXTRACT):
        API.PARAMS["page"] = 1
        API.PARAMS["date"] = date

        # Repeats the API request for each page
        while True:
            response = get_sales()

            if response.status_code != 200:
                print(
                    f"Failed to fetch data for {date} page {API.PARAMS['page']}: {response.status_code}"
                )
                break

            if not response["data"]:
                break

            sales_data = response["data"]
            pagination = response["pagination"]

            for sale in sales_data:
                sale_id = sale.get("sale_id")
                # Checks if sale was already added
                if sale_id and sale_id not in seen_ids:
                    seen_ids.add(sale_id)

                    # Inserts sale into a dataframe
                    DATA_TO_INSERT.DATA = concat(
                        [
                            DATA_TO_INSERT.DATA,
                            DataFrame([Transform(sale)]),
                        ],
                        ignore_index=True,
                    )

            API.PARAMS["page"] = pagination["current_page"] + 1

            if API.PARAMS["page"] > pagination["total_pages"]:
                break
