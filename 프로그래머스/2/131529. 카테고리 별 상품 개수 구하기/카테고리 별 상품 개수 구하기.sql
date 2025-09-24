select substring(PRODUCT_CODE,1,2) as CATEGORY, count(*) as PRODUCTS
from product
group by substring(PRODUCT_CODE,1,2)
order by 1