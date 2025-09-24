select a.APNT_NO, p.PT_NAME, p.PT_NO, d.MCDP_CD, d.DR_NAME, a.APNT_YMD
from APPOINTMENT a
join DOCTOR d
on a.MDDR_ID = d.DR_ID
join PATIENT p 
on a.PT_NO = p.PT_NO
where a.MCDP_CD='CS' and date_format(a.APNT_YMD,"%Y-%m-%d") = '2022-04-13' and a.APNT_CNCL_YN = 'N'
order by 6