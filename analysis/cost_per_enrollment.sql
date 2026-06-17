-- Cost Per Enrollment (CPE) by Platform

SELECT
    platform,

    SUM(cost) AS total_cost,

    SUM(enrollments) AS total_enrollments,

    ROUND(
        SUM(cost) * 1.0 / SUM(enrollments),
        2
    ) AS cost_per_enrollment

FROM campaign_performance

GROUP BY platform

ORDER BY cost_per_enrollment ASC;