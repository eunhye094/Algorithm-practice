select count(user_id) users
from user_info
where (age between 20 and 29) and to_char(joined, 'yyyy')=2021