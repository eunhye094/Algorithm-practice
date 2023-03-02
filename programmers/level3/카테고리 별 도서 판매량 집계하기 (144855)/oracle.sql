select category, sum(sales) total_sales
from book A, book_sales B
where A.book_id=B.book_id and to_char(sales_date, 'yyyy-mm')='2022-01'
group by category
order by category