SELECT ingredient_type, sum(total_order) as total_order
from first_half f left join icecream_info i on f.flavor=i.flavor
group by ingredient_type
order by total_order