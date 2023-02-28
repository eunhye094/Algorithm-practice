select A.apnt_no, B.pt_name, B.pt_no, C.mcdp_cd, C.dr_name, A.apnt_ymd
from appointment A join patient B on A.pt_no=B.pt_no
                    join doctor C on A.mddr_id=C.dr_id
where date_format(A.apnt_ymd, '%Y-%m-%d')='2022-04-13' and A.apnt_cncl_yn='N' and A.mcdp_cd='CS'
order by A.apnt_ymd