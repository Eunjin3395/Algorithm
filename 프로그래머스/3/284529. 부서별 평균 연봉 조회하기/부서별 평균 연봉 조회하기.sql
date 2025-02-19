-- 코드를 작성해주세요
select d.DEPT_ID, d.DEPT_NAME_EN, round(avg(e.sal),0) as AVG_SAL
from HR_DEPARTMENT as d
join HR_EMPLOYEES as e
on d.dept_id = e.dept_id
group by dept_id
order by 3 desc