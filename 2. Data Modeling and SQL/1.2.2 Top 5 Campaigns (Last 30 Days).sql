-- 2: Top 5 Campaigns (Last 30 Days)
WITH recent AS (
SELECT
    campaign_id,
    campaign_name,
    platform,
    SUM(cost_usd)     AS total_cost,
    SUM(conversions)  AS total_conversions
FROM
    `project.dataset.daily_campaign_stats`
WHERE
    date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) AND CURRENT_DATE()
GROUP BY
    campaign_id,
    campaign_name,
    platform
    ),
    cpc AS (
    SELECT
        campaign_id,
        campaign_name,
        platform,
        total_cost,
        total_conversions,
        SAFE_DIVIDE(total_cost, total_conversions) AS cost_per_conversion
    FROM
        recent
    )
SELECT
    campaign_id,
    campaign_name,
    platform,
    total_cost,
    total_conversions,
    cost_per_conversion
FROM
    cpc
WHERE
    total_conversions > 0
ORDER BY
    cost_per_conversion DESC
LIMIT 5;
