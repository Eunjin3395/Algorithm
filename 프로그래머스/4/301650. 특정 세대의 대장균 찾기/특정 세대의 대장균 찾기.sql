-- 코드를 작성해주세요
WITH RECURSIVE RE AS (
    SELECT ID, PARENT_ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT e.ID, e.PARENT_ID, r.GENERATION+1
    FROM ECOLI_DATA as e
    JOIN RE as r
    ON r.ID = e.PARENT_ID
)

SELECT ID
FROM RE 
WHERE GENERATION = 3
ORDER BY ID