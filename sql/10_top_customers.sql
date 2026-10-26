
SELECT
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders,
    ROUND(SUM(o.order_amount), 2) AS total_spent
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.name
ORDER BY total_spent DESC
LIMIT 10;