SELECT
    order_id,
    product_id,
    out_date,
    case
        when out_date is null then '출고미정'
        when out_date <='2022-05-01' then '출고완료'
        when out_date >'2022-05-01' then '출고대기'
    end as '출고여부'
from food_order
order by order_id