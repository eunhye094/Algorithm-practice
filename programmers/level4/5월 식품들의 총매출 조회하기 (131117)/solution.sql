select A.product_id, A.product_name, sum(A.price*B.amount) as total_sales 
from food_product A join food_order B on A.product_id=B.product_id
where B.produce_date like '%2022-05%'
group by A.product_id
order by total_sales desc, A.product_id asc;