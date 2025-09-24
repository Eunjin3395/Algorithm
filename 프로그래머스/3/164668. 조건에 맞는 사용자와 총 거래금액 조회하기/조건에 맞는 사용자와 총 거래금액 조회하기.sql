select USER_ID, NICKNAME, sum(price) TOTAL_SALES
from USED_GOODS_USER u
join USED_GOODS_BOARD b
on u.user_id = b.writer_id
where b.status = 'DONE'
group by u.user_id
having sum(price)>= 700000
order by 3 asc