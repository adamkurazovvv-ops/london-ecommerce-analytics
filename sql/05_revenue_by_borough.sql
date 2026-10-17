SELECT
    c.borough,
    ROUND(SUM(o.order_amount), 2) AS revenue,
    COUNT(o.order_id) AS total_orders
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.borough
ORDER BY revenue DESC;
