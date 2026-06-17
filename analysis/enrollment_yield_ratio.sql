-- Enrollment Yield Ratio by Platform

SELECT
    platform,

    SUM(applications) AS total_applications,

    SUM(enrollments) AS total_enrollments,

    ROUND(
        SUM(enrollments) * 100.0 /
        SUM(applications),
        2
    ) AS enrollment_yield_percentage

FROM campaign_performance

GROUP BY platform

ORDER BY enrollment_yield_percentage DESC;