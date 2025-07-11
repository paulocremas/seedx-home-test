-- 1. Staging table with unified platform field
CREATE TABLE `project.dataset.daily_campaign_stats` (
  date                DATE NOT NULL,
  client_id           STRING NOT NULL,
  platform            STRING NOT NULL,  -- 'google', 'meta'
  campaign_id         STRING NOT NULL,
  campaign_name       STRING,
  impressions         INT64,
  clicks              INT64,
  cost_usd            NUMERIC,
  conversions         INT64,
  reach               INT64  -- NULL for Google
)
PARTITION BY date -- Helps in time-range queries
CLUSTER BY client_id, platform, campaign_id;
