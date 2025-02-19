-- 코드를 작성해주세요
with subquery as(
select fish_type
from fish_info
group by fish_type
having avg(coalesce(length,10))>=33
)

select count(*) as FISH_COUNT, max(length) as MAX_LENGTH, FISH_TYPE
from fish_info
where fish_type in (select fish_type from subquery)
group by fish_type
order by 3
