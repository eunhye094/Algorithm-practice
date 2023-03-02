select ingredient_type, sum(total_order) total_order
from first_half A, icecream_info B
where A.flavor=B.flavor
group by ingredient_type
order by total_order