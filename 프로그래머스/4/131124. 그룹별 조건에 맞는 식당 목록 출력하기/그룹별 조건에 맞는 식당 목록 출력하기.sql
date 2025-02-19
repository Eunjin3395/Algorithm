-- 코드를 입력하세요
with cnt_cte as(
    select member_id, count(*) as cnt
    from REST_REVIEW
    group by member_id
    order by cnt desc
),
max_cte as(
    select member_id, cnt
    from cnt_cte
    where cnt = (select max(cnt) from cnt_cte)
)

select p.MEMBER_NAME, r.REVIEW_TEXT, date_format(r.REVIEW_DATE,'%Y-%m-%d') as REVIEW_DATE
from REST_REVIEW r
join max_cte m
on r.member_id = m.member_id
join MEMBER_PROFILE p
on p.member_id = r.member_id
order by r.review_date, r.review_text
