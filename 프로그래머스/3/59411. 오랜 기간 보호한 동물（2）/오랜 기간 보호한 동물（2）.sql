-- 코드를 입력하세요
WITH MAX_TABLE AS (
    SELECT i.ANIMAL_ID, TIMESTAMPDIFF(SECOND,i.DATETIME,o.DATETIME) AS DIFF
    FROM ANIMAL_INS as i
    JOIN ANIMAL_OUTS as o
    ON i.ANIMAL_ID = o.ANIMAL_ID
    ORDER BY DIFF DESC
    LIMIT 2
    
)

SELECT o.ANIMAL_ID, o.NAME
FROM ANIMAL_OUTS as o
JOIN MAX_TABLE as mt
ON o.ANIMAL_ID = mt.ANIMAL_ID
ORDER BY mt.DIFF DESC