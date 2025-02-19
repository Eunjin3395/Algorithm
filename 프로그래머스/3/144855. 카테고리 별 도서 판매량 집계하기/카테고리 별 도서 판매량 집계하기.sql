-- 코드를 입력하세요
SELECT b.CATEGORY, sum(s.sales) as TOTAL_SALES
from book as b
left join BOOK_SALES as s
on b.book_id = s.book_id
where date_format(s.sales_date,'%Y-%m') = '2022-01'
group by b.category
order by 1