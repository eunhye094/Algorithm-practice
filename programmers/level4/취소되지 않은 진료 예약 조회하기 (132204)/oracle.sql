select A.apnt_no, B.pt_name, B.pt_no, C.mcdp_cd, C.dr_name, A.apnt_ymd
from appointment A, patient B, doctor C
where A.pt_no=B.pt_no and A.mddr_id=C.dr_id
    and to_char(A.apnt_ymd, 'yyyy-mm-dd')='2022-04-13' and A.apnt_cncl_yn='N' and A.mcdp_cd='CS'
order by A.apnt_ymd