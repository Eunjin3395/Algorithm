-- 코드를 입력하세요
select year(s.sales_date) as YEAR, month(s.sales_date) as MONTH, u.GENDER, count(distinct(u.user_id)) as USERS
from ONLINE_SALE s
join USER_INFO u
on u.user_id = s.user_id
where u.gender is not null
group by year(s.sales_date), month(s.sales_date), u.gender
order by 1,2,3