SELECT product_code, P.price*sum(O.sales_amount) as sales
from product P left join offline_sale O on P.product_id=O.product_id
group by product_code
order by sales desc, product_code asc

-- SELECT product_code, P.price*O.sales_amount as sales
-- from product P left join (select product_id, sum(sales_amount) as sales_amount from offline_sale group by product_id) O on P.product_id=O.product_id
-- order by sales desc, product_code asc