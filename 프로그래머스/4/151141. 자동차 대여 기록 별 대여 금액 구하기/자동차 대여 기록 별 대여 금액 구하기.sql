with TRUCK_TBL as (
    select h.HISTORY_ID,c.DAILY_FEE,c.car_type , datediff(end_date,start_date)+1 as duration
    from CAR_RENTAL_COMPANY_CAR c
    join CAR_RENTAL_COMPANY_RENTAL_HISTORY h
    on c.car_id = h.car_id
    where c.car_type ='트럭'
),
WITH_DISCOUNT as(
    select t.HISTORY_ID, t.DAILY_FEE, t.duration, t.car_type,
    case
        when t.duration >= 90 then '90일 이상'
        when t.duration >= 30 then '30일 이상'
        when t.duration >= 7 then '7일 이상'
        else null
    end as duration_type
    from TRUCK_TBL t
)

select HISTORY_ID, 
    case
        when discount_rate is null then daily_fee * duration
        else round(daily_fee * (100-discount_rate)/100 * duration,0)
    end as FEE
from with_discount d
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
on (d.duration_type = p.duration_type and d.car_type = p.car_type)
order by 2 desc, 1 desc
 
