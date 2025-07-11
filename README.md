1. [Python Data Extraction and Processing](#python)
2. [Data Modeling and SQL](#data)
3. [Interview Questions] (#interview)

<a id="python"></a>
# Python Data Extraction and Processing

### _Modules_
### Config
This module has __4 classes__

1. __API:__ stores endpoints, parameters (e.g. for pagination), and extraction range (e.g. number of days).

2. __Sale:__ defines the attributes required to ensure schema compatibility and allows definitive information to be inserted with each sale (e.g. self.crm_id = 1).

3. __DataToInsert:__ used to create a singleton-like object (DATA_TO_INSERT) that contains a pandas DataFrame which will store all data to be loaded into Google BigQuery.

4. __GoogleBigQuery:__ stores table ID, credentials, and initializes the BigQuery client.
 
### Extract
This module has __3 functions__

1. __extract:__ Iterates over the last N days (from config), resets API pagination per day, fetches sales pages via API calls, skips duplicates using a set of sale IDs, transforms valid sales, and appends them to DATA_TO_INSERT.

2. __get_last_n_days:__ Returns a list of the last N dates (including today) in YYYY-MM-DD format.

3. __get_sales:__ Executes an API request using the current API configuration.

### Transform
This module has __1 function__

1. __transform:__ Converts a raw sale dictionary into a Sale object with defined attributes, then returns its dictionary representation.

### Load
This module has __1 function__

1. __load:__ Checks if there is data to insert; if so, initializes a BigQuery client and loads the DATA_TO_INSERT DataFrame into the configured BigQuery table, waiting for the job to complete.

---

<a id="data"></a>
# Data Modeling and SQL

---
<a id="interview"></a>
# Interview Questions
