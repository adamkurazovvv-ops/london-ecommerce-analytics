SELECT
    p.product_name,
    p.category,
    ROUND(SUM(oi.quantity * p.price), 2) AS revenue,
    SUM(oi.quantity) AS units_sold
FROM order_items AS oi
JOIN products AS p
    ON oi.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY revenue DESC
LIMIT 5;