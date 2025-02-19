# -- 코드를 입력하세요
# with subquery as(
#     select car_id
#     from CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     where start_date >= date('2022-08-01') 
#     group by car_id
#     having count(*)>=5
# )

# select month(start_date) as MONTH, CAR_ID, count(*) as RECORDS
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where car_id IN (SELECT car_id FROM subquery)
# group by month(start_date), car_id
# having count(*)>0
# order by 1, 2 desc

WITH subquery AS (
    SELECT car_id
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE start_date >= DATE('2022-08-01') 
        AND start_date <= DATE('2022-10-31')
    GROUP BY car_id
    HAVING COUNT(*) >= 5
)

SELECT EXTRACT(MONTH FROM start_date) AS MONTH, 
       car_id, 
       COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE car_id IN (SELECT car_id FROM subquery)
    AND start_date >= DATE('2022-08-01') 
    AND start_date <= DATE('2022-10-31')
GROUP BY EXTRACT(MONTH FROM start_date), car_id
HAVING COUNT(*) > 0
ORDER BY MONTH, CAR_ID DESC;
