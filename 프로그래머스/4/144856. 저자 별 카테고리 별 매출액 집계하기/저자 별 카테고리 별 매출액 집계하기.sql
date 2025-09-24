select a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(price*s.sales) TOTAL_SALES
from BOOK b 
join AUTHOR a
on b.author_id = a.author_id
join BOOK_SALES s
on b.book_id = s.book_id
where date_format(s.sales_date,'%Y-%m') = '2022-01'
group by a.author_id, b.category
order by a.author_id, b.category desc