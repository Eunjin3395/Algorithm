-- 코드를 작성해주세요
with rate_cte as(
select emp_no, 
    case
        when avg(score) >= 96 then 0.2
        when avg(score) >= 90 then 0.15
        when avg(score) >= 80 then 0.1
        else 0
    end as rate,
    case
        when avg(score) >= 96 then 'S'
        when avg(score) >= 90 then 'A'
        when avg(score) >= 80 then 'B'
        else 'C'
    end as grade
from HR_GRADE
group by emp_no
)

select e.EMP_NO, e.EMP_NAME, r.GRADE, e.sal * r.rate as BONUS
from HR_EMPLOYEES e
join rate_cte r
on e.emp_no = r.emp_no
order by 1