select book_id, author_name, date_format(published_date, "%Y-%m-%d") as published_date
from book a join author b on a.author_id=b.author_id
where a.category='경제'
order by a.published_date;