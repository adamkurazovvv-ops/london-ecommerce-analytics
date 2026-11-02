SELECT
    borough,
    COUNT(*) AS total_deliveries,
    SUM(
        CASE
            WHEN delivery_status = 'Late' THEN 1
            ELSE 0
        END
    ) AS late_deliveries,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN delivery_status = 'Late' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS late_percentage
FROM deliveries
GROUP BY borough
ORDER BY late_percentage DESC;