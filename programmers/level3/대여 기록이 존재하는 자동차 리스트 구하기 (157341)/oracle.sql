select distinct car_id
from car_rental_company_rental_history
where car_id in (select car_id from car_rental_company_car where car_type='세단')
    and to_char(start_date, 'mm')='10'
order by car_id desc