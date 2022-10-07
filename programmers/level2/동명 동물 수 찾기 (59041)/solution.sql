SELECT
    name,
    count(animal_id) as count
from animal_ins
where name is not null
group by name
having count(animal_id) >=2
order by name