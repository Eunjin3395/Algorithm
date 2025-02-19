-- 코드를 입력하세요
with subquery as (
select distinct(car_id)
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where date(end_date) >= date('2022-10-16')
    and date(start_date) <= date('2022-10-16')
)
    
select car_id,
    case
        when car_id in (select * from subquery) then '대여중'
        else '대여 가능'
        end as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by 1 desc