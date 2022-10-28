SELECT mcdp_cd as '진료과 코드', count(mcdp_cd) as '5월예약건수'
from appointment
WHERE apnt_ymd like '%2022-05%'
group by mcdp_cd
order by count(mcdp_cd), mcdp_cd