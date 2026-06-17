-- Campaign Ranking by Revenue

SELECT
    campaign_name,
    platform,

    SUM(revenue) AS total_revenue,

    RANK() OVER(
        ORDER BY SUM(revenue) DESC
    ) AS revenue_rank

FROM campaign_performance

GROUP BY
    campaign_name,
    platform;