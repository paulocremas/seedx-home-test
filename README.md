# SeedX Take Home Test
#### Approach & Reasoning:
For the Python project, __I aimed to make it scalable and robust,__, although I recognize the project’s simple premise doesn’t require such complexity. I implemented a transform function to allow changes to the sales objects, __and designed a load function to insert data into BigQuery__. 

I didn’t follow any specific methodology when structuring the project, the current structure is one I developed on my own. That said, I’m fully open to adapting to the team’s standards and learning as we go.

__Note:__ Logs and error handling were left out given the test nature of the project.

### _Summary_
1. [Python Data Extraction and Processing](#python)
2. [Data Modeling and SQL](#data)
3. [Interview Questions](#interview)

---

<a id="python"></a>
### [_Python Data Extraction and Processing_](https://github.com/paulocremas/seedx-home-test/tree/main/1.%20Python%20Data%20Extraction%20and%20Processing)

### [Config](https://github.com/paulocremas/seedx-home-test/blob/main/1.%20Python%20Data%20Extraction%20and%20Processing/config.py)
This module has __4 classes__

1. __API:__ stores endpoints, parameters (for pagination), and extraction range (number of days).

2. __Sale:__ defines the attributes required to ensure schema compatibility and allows definitive information to be inserted with each sale (e.g. self.crm_id = 1).

3. __DataToInsert:__ used to create a singleton-like object (DATA_TO_INSERT) that contains a pandas DataFrame which will store all data to be loaded into Google BigQuery.

4. __GoogleBigQuery:__ stores table ID, credentials, and initializes the BigQuery client.
 
### [Extract](https://github.com/paulocremas/seedx-home-test/blob/main/1.%20Python%20Data%20Extraction%20and%20Processing/modules/extract.py)
This module has __3 functions__

1. __extract:__ iterates over the last N days (from config), resets API pagination per day, fetches sales pages via API calls, skips duplicates using a set of sale IDs, transforms valid sales, and appends them to DATA_TO_INSERT.

2. __get_last_n_days:__ returns a list of the last N dates (including today) in YYYY-MM-DD format.

3. __get_sales:__ executes an API request using the current API configuration.

### [Transform](https://github.com/paulocremas/seedx-home-test/blob/main/1.%20Python%20Data%20Extraction%20and%20Processing/modules/transform.py)
This module has __1 function__

1. __transform:__ converts a raw sale dictionary into a Sale object with defined attributes, then returns its dictionary representation.

### [Load](https://github.com/paulocremas/seedx-home-test/blob/main/1.%20Python%20Data%20Extraction%20and%20Processing/modules/load.py)
This module has __1 function__

1. __load:__ checks if there is data to insert; if so, initializes a BigQuery client and loads the DATA_TO_INSERT DataFrame into the configured BigQuery table, waiting for the job to complete.
<br>

#### [Dockerfile](https://github.com/paulocremas/seedx-home-test/blob/main/1.%20Python%20Data%20Extraction%20and%20Processing/Dockerfile)

---
<a id="data"></a>
### [_Data Modeling and SQL_](https://github.com/paulocremas/seedx-home-test/tree/main/2.%20Data%20Modeling%20and%20SQL)
### 1.1 [Schema Design](https://github.com/paulocremas/seedx-home-test/blob/main/2.%20Data%20Modeling%20and%20SQL/1.1%20Schema%20Design.sql)
Unified daily campaign data. Partitioned by date, clustered by client_id, platform, campaign_id. reach is Meta-only.

### 1.2.1 [Daily Total Cost per Client and Platform](https://github.com/paulocremas/seedx-home-test/blob/main/2.%20Data%20Modeling%20and%20SQL/1.2.1%20Daily%20Total%20Cost%20per%20Client%20and%20Platform.sql)
Calculates daily spend per platform for client_ABC, summing cost_usd, grouped by date and platform, ordered from newest to oldest.

### 1.2.2 [Top 5 Campaigns (Last 30 Days)](https://github.com/paulocremas/seedx-home-test/blob/main/2.%20Data%20Modeling%20and%20SQL/1.2.2%20Top%205%20Campaigns%20(Last%2030%20Days).sql)
Uses CTEs to break down the query: the first aggregates cost and conversions per campaign in the last 30 days; the second calculates cost per conversion. Finally, it selects the top 5 campaigns by highest cost per conversion.

### 1.2.3 [Client Performance](https://github.com/paulocremas/seedx-home-test/blob/main/2.%20Data%20Modeling%20and%20SQL/1.2.3%20Client%20Performance.sql)
Uses a CTE to set comparison months, then aggregates monthly metrics for client_ABC. Outputs monthly performance with cost per conversion.

---
<a id="interview"></a>
### _Interview Questions_
#### 1. Our dashboards and queries are running slower than expected and we noticed high BigQuery costs. What are some strategies and techniques you would investigate and implement in this case?
A: These are some approachs I would try
* Monitoring and identifing heavy queries
* Query review and optimzation
* Partitioning and clustering
* Cost control by setting up cost alerts and budget tracking

#### 2. We handle data needs of several clients, and each one needs different data sources. Some sources may overlap (for example, many clients need data from Google Ads and Meta Ads), but in other cases we need client-specific sources. How do you envision the database structure we need to make it easily maintainable and scalable?
A: I map all equivalent fields across sources and structure the data using a unified schema for all clients, using a client_id field to differentiate them.

#### 3. Consider the campaign_name in your Google Ads or Meta Ads data. Campaign names can change over time. How would you model this in BigQuery to track the history of campaign names for reporting purposes?
A: I would store multiple records per campaign, each with a validity period defined by start and end dates to indicate when a specific campaign name was active. When the campaign name changes, I would use a query to close the previous record by setting its end date and insert a new record with the updated name.

#### 4. Imagine one of your daily data pipelines (either a Coupler/Airbyte sync or a custom Python Cloud Run Job) fails unexpectedly. This could be due to a source system outage, API changes, or a bug in the code. Describe your process for:
#### A. Detecting the failure.
A: I rely on alerts from Airbyte or Cloud Monitoring (for Cloud Run jobs), check centralized logs, success flags, and data validations in BigQuery.
#### B. Diagnosing the root cause.
A: I review error logs or config changes. For source issues, I check API responses or source system status. For data issues, I compare with previous runs.
#### C. Implementing a fix.
A: I patch the issue, test locally or in staging, then redeploy the job. If needed, I manually backfill the failed data.
#### D. Ensuring the data is eventually consistent and complete in BigQuery.
A: I trigger a backfill for the failed period, validating record counts and key metrics against the source. I also run data quality checks to confirm no duplicates or gaps exist.
#### E. What monitoring and alerting mechanisms would you put in place to prevent or quickly address future failures?
A: Automated failure alerts, retry with backoff and dashboards for health.

 
 
