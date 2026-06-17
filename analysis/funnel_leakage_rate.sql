-- Funnel Leakage Analysis

WITH funnel AS (

    SELECT
        SUM(impressions) AS impressions,
        SUM(clicks) AS clicks,
        SUM(leads) AS leads,
        SUM(applications) AS applications,
        SUM(enrollments) AS enrollments

    FROM campaign_performance

)

SELECT
    impressions,
    clicks,
    leads,
    applications,
    enrollments,

    ROUND(
        (impressions - clicks) * 100.0 / impressions,
        2
    ) AS impression_to_click_drop,

    ROUND(
        (clicks - leads) * 100.0 / clicks,
        2
    ) AS click_to_lead_drop,

    ROUND(
        (leads - applications) * 100.0 / leads,
        2
    ) AS lead_to_application_drop,

    ROUND(
        (applications - enrollments) * 100.0 / applications,
        2
    ) AS application_to_enrollment_drop

FROM funnel;