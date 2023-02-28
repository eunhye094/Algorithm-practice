select A.rest_id, A.rest_name, A.food_type, A.favorites, A.address, B.score
from rest_info A, (select rest_id, round(avg(review_score),2) score from rest_review group by rest_id) B
where A.rest_id=B.rest_id and A.address like '서울%'
order by B.score desc, A.favorites desc