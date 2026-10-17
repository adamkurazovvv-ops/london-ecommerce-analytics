SELECT
    c.borough,
    COUNT(DISTINCT c.customer_id) AS total_customers,
    ROUND(SUM(o.order_amount), 2) AS total_revenue,
    ROUND(
        SUM(o.order_amount) / COUNT(DISTINCT c.customer_id),
        2
    ) AS revenue_per_customer
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.borough
ORDER BY revenue_per_customer DESC;
