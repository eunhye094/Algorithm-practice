select car_type, count(*) cars
from car_rental_company_car
where regexp_like(options, '통풍시트|열선시트|가죽시트')
group by car_type
order by car_type