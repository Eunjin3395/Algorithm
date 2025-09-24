select BOOK_ID, date_format(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE
from BOOK
where category = '인문' and date_format(published_date,'%Y')='2021'
order by published_date asc