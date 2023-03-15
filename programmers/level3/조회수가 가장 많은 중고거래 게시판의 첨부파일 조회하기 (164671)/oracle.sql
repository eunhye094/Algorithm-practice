select '/home/grep/src/'||board_id||'/'||file_id||file_name||file_ext as file_path
from used_goods_file
where board_id=(select board_id
                from (select *
                      from used_goods_board
                      order by views desc)
                where rownum=1)
order by file_id desc