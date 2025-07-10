import os
from pandas import DataFrame
from google.cloud import bigquery


class API:
    def __init__(self):
        self.ENDPOINT = "https://api.crm.com/v1/sales"
        self.HEADERS = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}
        self.DAYS_TO_EXTRACT = 1
        self.PARAMS = {"date": "", "page": 1, "limit": 100}


class Sale:
    def __init__(
        self,
        SALE_ID,
        SALE_DATE,
        CUSTOMER_ID,
        PRODUCT_NAME,
        AMOUNT,
        CURRENCY,
        STATUS,
    ):
        self.sale_id = SALE_ID
        self.sale_date = SALE_DATE
        self.customer_id = CUSTOMER_ID
        self.product_name = PRODUCT_NAME
        self.amount = AMOUNT
        self.currency = CURRENCY
        self.status = STATUS
        self.crm_id = 1


class DataToInsert:
    def __init__(self):
        self.DATA = DataFrame()


DATA_TO_INSERT = DataToInsert()


class GoogleBigQuery:
    def __init__(self):
        self.TABLE_ID = os.environ.get("TABLE_ID")
        self.GOOGLE_APPLICATION_CREDENTIALS = os.environ.get(
            "GOOGLE_APPLICATION_CREDENTIALS"
        )
        self.CLIENT = bigquery.Client()
