SELECT
    DATE_TRUNC('month', order_date)::date AS month,
    ROUND(SUM(order_amount), 2) AS revenue,
    COUNT(*) AS total_orders
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;