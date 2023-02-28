-- SELECT flavor
-- from first_half
-- where total_order>3000
-- and flavor in (select flavor from icecream_info where ingredient_type='fruit_based')
-- order by total_order desc

select A.flavor
from first_half A, icecream_info B
where A.flavor=B.flavor and A.total_order>3000 and B.ingredient_type='fruit_based'
order by A.total_order desc