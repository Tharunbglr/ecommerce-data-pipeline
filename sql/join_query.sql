SELECT
    u.name AS user_name,
    o.order_id,
    o.order_date,
    p.name AS product_name,
    oi.quantity,
    (oi.quantity * oi.unit_price) AS total_value
FROM orders o
JOIN users u ON o.user_id = u.user_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
ORDER BY o.order_date DESC;
SELECT
    u.name AS user_name,
    o.order_id,
    o.order_date,
    p.name AS product_name,
    oi.quantity,
    (oi.quantity * oi.unit_price) AS total_value
FROM orders o
JOIN users u ON o.user_id = u.user_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
ORDER BY o.order_date DESC;
