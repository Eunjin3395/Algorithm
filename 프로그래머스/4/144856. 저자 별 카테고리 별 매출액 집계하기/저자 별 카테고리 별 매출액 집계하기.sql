-- 코드를 입력하세요
with filtered_table as(
    SELECT * 
    from book_sales 
    where date_format(sales_date,'%Y-%m') = '2022-01'
)

select a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(b.price*f.sales) as TOTAL_SALES
from BOOK as b
join AUTHOR as a
on b.author_id = a.author_id
join filtered_table as f
on b.book_id = f.book_id
group by a.author_id, b.category
order by 1,3 desc
    
