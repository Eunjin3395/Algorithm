WITH skill_mapping AS (
SELECT 
    SUM(CASE WHEN CATEGORY = 'Front End' THEN CODE ELSE 0 END) AS FE,
    SUM(CASE WHEN NAME = 'Python' THEN CODE ELSE 0 END) AS PY,
    SUM(CASE WHEN NAME = 'C#' THEN CODE ELSE 0 END) AS CS
FROM SKILLCODES
)

select 
    case
        when d.skill_code & s.fe > 0 and d.skill_code & s.py > 0 
        then 'A'
        when d.skill_code & s.cs > 0
        then 'B'
        else 'C'
        end as GRADE,
        ID, 
        EMAIL
from DEVELOPERS d
cross join skill_mapping s
where (d.skill_code & s.fe > 0 and d.skill_code & s.py > 0)
    or d.skill_code & s.cs > 0
    or d.skill_code & s.fe > 0
order by grade, id