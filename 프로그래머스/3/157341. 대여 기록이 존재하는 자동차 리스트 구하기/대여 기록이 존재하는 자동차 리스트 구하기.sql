select distinct(c.CAR_ID)
from CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_RENTAL_HISTORY h
on c.car_id = h.car_id
where c.car_type='세단'
and month(h.start_date) =10
order by 1 desc