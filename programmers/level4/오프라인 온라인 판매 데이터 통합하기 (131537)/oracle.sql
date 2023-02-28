select *
from(
    select to_char(sales_date, 'yyyy-mm-dd') sales_date, product_id, user_id, sales_amount from online_sale
        union all
    select to_char(sales_date, 'yyyy-mm-dd') sales_date, product_id, null as user_id, sales_amount from offline_sale
)
where sales_date like '2022-03%'
order by sales_date, product_id, user_id