select PRODUCT_CODE, sum(p.price * s.sales_amount) as SALES
from PRODUCT p
join OFFLINE_SALE s
where p.product_id = s.product_id
group by p.product_id
order by 2 desc, 1