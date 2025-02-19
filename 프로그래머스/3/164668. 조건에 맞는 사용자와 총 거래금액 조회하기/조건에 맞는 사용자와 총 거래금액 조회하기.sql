-- 코드를 입력하세요
with subquery as(
SELECT writer_id, sum(price) as total_sales
from USED_GOODS_BOARD
where status = 'DONE'
group by writer_id
having sum(price)>=700000
)

select u.USER_ID, u.NICKNAME, sb.total_sales as TOTAL_SALES
from subquery sb
left join USED_GOODS_USER u
on sb.writer_id = u.user_id
order by 3