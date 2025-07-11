# Python Data Extraction and Processing

### Modules 
### Config
This module has 4 classes

1. API: stores endpoints, parameters (e.g. for pagination), and extraction range (e.g. number of days).

2. Sale: defines the attributes required to ensure schema compatibility and allows definitive information to be inserted with each sale (e.g. self.crm_id = 1).

3. DataToInsert: used to create a singleton-like object that contains a pandas DataFrame which will store all data to be loaded into Google BigQuery.

4. GoogleBigQuery: stores table ID, credentials, and initializes the BigQuery client.

---
 
### Extract
This module has 3 functions


### Transform
### Load
