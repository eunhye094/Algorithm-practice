-- Oracle join
select a.product_code as product_code, sum(a.price*b.sales_amount) as sales
from product a , offline_sale b
where a.product_id = b.product_id
group by a.product_code
order by sales desc, product_code asc