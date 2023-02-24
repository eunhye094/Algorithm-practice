SELECT member_id, member_name, gender, date_of_birth
from member_profile
where date_of_birth like '%-03-%' and gender = 'W' and tlno is not null
order by member_id