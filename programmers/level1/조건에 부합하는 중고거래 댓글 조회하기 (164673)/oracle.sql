select A.title, A.board_id, B.reply_id, B.writer_id, B.contents, to_char(B.created_date, 'yyyy-mm-dd') as created_date
from used_goods_board A, used_goods_reply B
where A.board_id=B.board_id
and to_char(A.created_date, 'yyyy-mm')='2022-10'
order by B.created_date, A.title