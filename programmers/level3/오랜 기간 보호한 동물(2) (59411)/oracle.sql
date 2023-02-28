select *
from (
    select A.animal_id animal_id, A.name name
    from animal_ins A, animal_outs B
    where A.animal_id=B.animal_id
    order by B.datetime-A.datetime+1 desc
)
where rownum<=2