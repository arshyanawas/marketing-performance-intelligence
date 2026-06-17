-- Regional Performance Ranking

SELECT
    region,

    SUM(revenue) AS total_revenue,

    SUM(cost) AS total_cost,

    ROUND(
        (SUM(revenue) - SUM(cost)) * 100.0 /
        SUM(cost),
        2
    ) AS roi_percentage,

    RANK() OVER(
        ORDER BY SUM(revenue) DESC
    ) AS revenue_rank

FROM campaign_performance

GROUP BY region

ORDER BY revenue_rank;