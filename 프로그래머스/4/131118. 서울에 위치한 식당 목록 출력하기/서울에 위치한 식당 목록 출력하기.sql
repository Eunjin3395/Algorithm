# 서울에 위치한 식당 먼저 조회
with seoul_rest as (
    select *
    from rest_info
    where address like '서울%'
)

# 해당 식당별 리뷰 join 후 평균 점수 계산
select s.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, round(avg(REVIEW_SCORE),2) as SCORE
from seoul_rest s
join rest_review r
on s.rest_id = r.rest_id
group by s.rest_id
order by score desc, favorites desc