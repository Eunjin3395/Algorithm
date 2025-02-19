-- 코드를 입력하세요
WITH available_cars AS (
    -- 1. 2022년 11월 1일~30일 동안 대여 가능한 차량 필터링
    SELECT c.CAR_ID, c.CAR_TYPE, c.DAILY_FEE
    FROM CAR_RENTAL_COMPANY_CAR c
    LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY r 
        ON c.CAR_ID = r.CAR_ID 
        AND (r.START_DATE <= '2022-11-30' AND r.END_DATE >= '2022-11-01')
    WHERE c.CAR_TYPE IN ('세단', 'SUV')
    GROUP BY c.CAR_ID, c.CAR_TYPE, c.DAILY_FEE
    HAVING COUNT(r.CAR_ID) = 0 -- 대여 기록이 없으면 해당 기간 동안 대여 가능
)

SELECT 
    a.CAR_ID, 
    a.CAR_TYPE, 
    FLOOR(a.DAILY_FEE * 30 * (1 - d.discount_rate / 100)) AS FEE
FROM available_cars a
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN d 
    ON a.CAR_TYPE = d.CAR_TYPE AND d.DURATION_TYPE = '30일 이상'
WHERE 
    FLOOR(a.DAILY_FEE * 30 * (1 - d.DISCOUNT_RATE / 100)) BETWEEN 500000 AND 1999999
ORDER BY 
    FEE DESC, 
    a.CAR_TYPE ASC, 
    a.CAR_ID DESC;