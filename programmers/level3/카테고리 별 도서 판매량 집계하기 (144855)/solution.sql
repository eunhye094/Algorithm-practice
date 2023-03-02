select category, sum(sales) total_sales
from book A join book_sales B on A.book_id=B.book_id
where sales_date like '%2022-01%'
group by category
order by category