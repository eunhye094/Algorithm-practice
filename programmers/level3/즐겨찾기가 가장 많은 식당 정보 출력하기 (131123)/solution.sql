/*
서브 쿼리에서 max(favorites)만 가져와서 비교하면, rest_id는 다르지만 같은 favorites을 가진 row가 모두 추출된다.
지금은 group by 한 번 더 사용해서 중복을 어영부영 막아놓은 상황이다.
더 좋은 방법이 없을까?
*/

select food_type, rest_id, rest_name, favorites
from rest_info
where favorites in (select max(favorites) from rest_info group by food_type)
group by food_type
order by food_type desc;