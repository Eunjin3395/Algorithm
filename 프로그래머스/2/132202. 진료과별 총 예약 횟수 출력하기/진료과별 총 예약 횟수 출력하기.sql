select mcdp_cd as '진료과 코드', count(*) as '5월예약건수'
from APPOINTMENT
where date_format(APNT_YMD,'%Y-%m')='2022-05'
group by mcdp_cd
order by 2,1