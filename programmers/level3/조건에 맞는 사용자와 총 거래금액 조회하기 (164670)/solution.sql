-- select user_id,
--        nickname,
--        concat(city, ' ', street_address1, ' ', street_address2) "전체주소",
--        concat(left(tlno,3),'-', mid(tlno,4,4) ,'-', right(tlno, 4)) "전화번호"
-- from used_goods_user
-- where user_id in (select writer_id from used_goods_board group by writer_id having count(*)>=3)
-- order by user_id desc

select user_id,
       nickname,
       concat(city, ' ', street_address1, ' ', street_address2) "전체주소",
       concat(left(tlno,3),'-', mid(tlno,4,4) ,'-', right(tlno, 4)) "전화번호"
from used_goods_board A join used_goods_user B
     on A.writer_id = B.user_id
group by writer_id
having count(*)>=3
order by user_id desc