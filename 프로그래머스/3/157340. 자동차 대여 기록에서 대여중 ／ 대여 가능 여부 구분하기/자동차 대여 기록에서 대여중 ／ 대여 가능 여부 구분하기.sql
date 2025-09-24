# 각 history마다 2022-10-16일자가 포함되는 구간인지 여부
with SUB_TBL as(
    select car_id, 
        case 
            when '2022-10-16' between start_date and end_date then 1
            else 0
        end as valid
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
)

select CAR_ID, 
    case
        when sum(valid) >0 then '대여중'
        else '대여 가능'
    end as AVAILABILITY
from SUB_TBL
group by CAR_ID
order by 1 desc