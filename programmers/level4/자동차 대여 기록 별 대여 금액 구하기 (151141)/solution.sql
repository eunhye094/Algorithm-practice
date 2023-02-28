select B.history_id, round(A.daily_fee*(datediff(B.end_date, B.start_date)+1)*
        (case
            when datediff(B.end_date, B.start_date)+1>=90 then (select 1-discount_rate*0.01 from car_rental_company_discount_plan where car_type='트럭' and duration_type='90일 이상')
            when datediff(B.end_date, B.start_date)+1>=30 then (select 1-discount_rate*0.01 from car_rental_company_discount_plan where car_type='트럭' and duration_type='30일 이상')
            when datediff(B.end_date, B.start_date)+1>=7 then (select 1-discount_rate*0.01 from car_rental_company_discount_plan where car_type='트럭' and duration_type='7일 이상')
            else 1
        end)) as fee
from car_rental_company_car A, car_rental_company_rental_history B
where A.car_id=B.car_id and A.car_type='트럭'
order by fee desc, history_id desc