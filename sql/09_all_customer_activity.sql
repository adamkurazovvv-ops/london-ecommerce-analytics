WITH customer_orders AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY customer_id
)
SELECT
    COUNT(*) AS all_customers,
    COUNT(*) FILTER (
        WHERE COALESCE(co.total_orders, 0) = 0
    ) AS customers_without_orders,
    COUNT(*) FILTER (
        WHERE co.total_orders = 1
    ) AS one_time_customers,
    COUNT(*) FILTER (
        WHERE co.total_orders > 1
    ) AS repeat_customers,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE co.total_orders > 1
        ) / COUNT(*),
        2
    ) AS repeat_customer_pct
FROM customers AS c
LEFT JOIN customer_orders AS co
    ON c.customer_id = co.customer_id;