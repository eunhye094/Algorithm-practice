select MEMBER_ID, MEMBER_NAME, GENDER, to_char(DATE_OF_BIRTH, 'yyyy-mm-dd') as DATE_OF_BIRTH
from MEMBER_PROFILE
where to_char(DATE_OF_BIRTH, 'mm')='03' and GENDER='W' and TLNO is not null
order by MEMBER_ID asc