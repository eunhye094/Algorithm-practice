select mcdp_cd "진료과 코드", count(*) "5월예약건수"
from appointment
where to_char(apnt_ymd,'yyyymm')='202205'
group by mcdp_cd
order by "5월예약건수", "진료과 코드"