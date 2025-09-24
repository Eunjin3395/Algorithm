select MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH,'%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where date_format(DATE_OF_BIRTH,'%m')='03' and gender='W' and tlno is not null
order by member_id asc