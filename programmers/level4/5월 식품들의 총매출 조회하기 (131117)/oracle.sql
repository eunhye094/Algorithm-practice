select A.product_id, A.product_name, sum(A.price*B.amount) as total_sales
from food_product A, food_order B
where A.product_id = B.product_id
and to_char(B.produce_date, 'yyyy-mm') = '2022-05'
group by A.product_id, A.product_name
order by total_sales desc, A.product_id asc;