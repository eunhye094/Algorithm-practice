-- Oracle join
SELECT book_id, author_name, to_char(published_date, 'yyyy-mm-dd') as published_date
from book A, author B
where A.author_id=B.author_id and A.category='경제'
order by published_date asc