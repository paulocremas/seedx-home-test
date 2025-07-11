-- 1: Daily Total Cost per Client and Platform
SELECT
  date,
  platform,
  SUM(cost_usd) AS daily_spend
FROM
  `project.dataset.daily_campaign_stats`
WHERE
  client_id = 'client_ABC'
GROUP BY
  date,
  platform
ORDER BY
  date DESC, platform;