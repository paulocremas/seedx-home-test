from config import DATA_TO_INSERT, GoogleBigQuery


def load():
    if not len(DATA_TO_INSERT.DATA) == 0:
        BIGQUERY_CONFIG = GoogleBigQuery()

        job = BIGQUERY_CONFIG.CLIENT.load_table_from_dataframe(
            DATA_TO_INSERT.DATA, BIGQUERY_CONFIG.TABLE_ID
        )
        job.result()
        print("Loaded DataFrame into BigQuery table.")
