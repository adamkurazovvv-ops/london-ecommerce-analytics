SELECT
    ROUND(SUM(order_amount), 2) AS total_revenue,
    COUNT(*) AS total_orders,
    ROUND(AVG(order_amount), 2) AS average_order_value
FROM orders;
