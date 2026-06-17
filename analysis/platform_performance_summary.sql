SELECT
    platform,

    SUM(revenue) AS total_revenue,
    SUM(cost) AS total_cost,
    SUM(enrollments) AS total_enrollments,

    ROUND(
        (SUM(revenue)-SUM(cost))*100.0/
        SUM(cost),
        2
    ) AS roi_percentage,

    ROUND(
        SUM(cost)*1.0/
        SUM(enrollments),
        2
    ) AS cost_per_enrollment

FROM campaign_performance

GROUP BY platform

ORDER BY roi_percentage DESC;