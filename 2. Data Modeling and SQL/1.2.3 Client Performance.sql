-- 3: Client Performance
WITH periods AS (
    SELECT
        PARSE_DATE('%Y-%m', '2025-05') AS target_month,
        PARSE_DATE('%Y-%m', '2025-04') AS previous_month,
        PARSE_DATE('%Y-%m', '2024-05') AS previous_year_month
    ),
agg AS (
    SELECT
        DATE_TRUNC(date, MONTH) AS month,
        SUM(impressions)   AS impressions,
        SUM(clicks)        AS clicks,
        SUM(cost_usd)      AS cost,
        SUM(conversions)   AS conversions
    FROM
        `project.dataset.daily_campaign_stats`
    WHERE
        client_id = 'client_ABC'
        AND DATE_TRUNC(date, MONTH) IN (
        (SELECT target_month FROM periods),
        (SELECT previous_month FROM periods),
        (SELECT previous_year_month FROM periods)
        )
    GROUP BY
        month
    )
SELECT
  month,
    impressions,
    clicks,
    cost,
    conversions,
    SAFE_DIVIDE(cost, conversions) AS cost_per_conversion
FROM
    agg
ORDER BY
    month;
