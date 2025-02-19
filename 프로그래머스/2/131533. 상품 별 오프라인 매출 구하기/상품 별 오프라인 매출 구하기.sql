-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(p.price * coalesce(s.sales_amount,0)) as SALES
from PRODUCT p
left join OFFLINE_SALE s
on p.product_id = s.product_id
group by 1
order by 2 desc, 1