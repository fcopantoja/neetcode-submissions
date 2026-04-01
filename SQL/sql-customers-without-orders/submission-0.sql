-- Write your query below
SELECT customers.name 
from customers 
LEFT JOIN orders
on orders.customer_id = customers.id
WHERE orders.id is NULL;
