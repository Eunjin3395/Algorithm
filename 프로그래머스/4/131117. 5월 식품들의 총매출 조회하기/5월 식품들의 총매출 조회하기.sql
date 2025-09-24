select p.PRODUCT_ID, p.PRODUCT_NAME, sum(p.price * o.amount) as TOTAL_SALES
from FOOD_PRODUCT p
join FOOD_ORDER o
on p.product_id = o.product_id
where date_format(o.PRODUCE_DATE,"%Y-%m") ='2022-05'
group by p.PRODUCT_ID
order by 3 desc, 1