-- Benchmark CPC Comparison

SELECT
    cp.platform,

    ROUND(
        SUM(cp.cost) * 1.0 /
        SUM(cp.clicks),
        2
    ) AS actual_cpc,

    cr.avg_cpc AS benchmark_cpc,

    ROUND(
        (
            (
                SUM(cp.cost) * 1.0 /
                SUM(cp.clicks)
            ) - cr.avg_cpc
        ),
        2
    ) AS cpc_difference,

    CASE
        WHEN (
            SUM(cp.cost) * 1.0 /
            SUM(cp.clicks)
        ) > cr.avg_cpc
        THEN 'Above Benchmark'

        ELSE 'Below Benchmark'
    END AS performance

FROM campaign_performance cp

JOIN channel_rates cr
    ON cp.platform = cr.channel

GROUP BY
    cp.platform,
    cr.avg_cpc

ORDER BY cpc_difference DESC;