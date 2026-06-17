-- ROI by Platform

SELECT
    platform,
    ROUND(SUM(revenue)/1000000.0,2) AS revenue_million,
    ROUND(SUM(cost)/1000000.0,2) AS cost_million,

    ROUND(
        (SUM(revenue)-SUM(cost))*100.0
        / SUM(cost),
        2
    ) AS roi_percentage

FROM campaign_performance

GROUP BY platform

ORDER BY roi_percentage DESC;