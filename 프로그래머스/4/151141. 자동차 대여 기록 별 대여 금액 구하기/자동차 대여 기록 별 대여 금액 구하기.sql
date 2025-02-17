# -- 코드를 입력하세요
# SELECT h.HISTORY_ID,
# CASE
#     WHEN DATEDIFF(h.END_DATE,h.START_DATE)+1 >= 90 THEN 
#         ROUND(c.DAILY_FEE*(DATEDIFF(h.END_DATE,h.START_DATE)+1)*(1-(
#             SELECT p.DISCOUNT_RATE
#             FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
#             WHERE p.CAR_TYPE = c.CAR_TYPE
#             AND p.DURATION_TYPE = '90일 이상')/100),0)
#     WHEN DATEDIFF(h.END_DATE,h.START_DATE)+1 >= 30 THEN 
#         ROUND(c.DAILY_FEE*(DATEDIFF(h.END_DATE,h.START_DATE)+1)*(1-(
#             SELECT p.DISCOUNT_RATE
#             FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
#             WHERE p.CAR_TYPE = c.CAR_TYPE
#             AND p.DURATION_TYPE = '30일 이상')/100),0)
#     WHEN DATEDIFF(h.END_DATE,h.START_DATE)+1 >= 7 THEN 
#         ROUND(c.DAILY_FEE*(DATEDIFF(h.END_DATE,h.START_DATE)+1)*(1-(
#             SELECT p.DISCOUNT_RATE
#             FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
#             WHERE p.CAR_TYPE = c.CAR_TYPE
#             AND p.DURATION_TYPE = '7일 이상')/100),0)
#     ELSE
#         c.DAILY_FEE*(DATEDIFF(h.END_DATE,h.START_DATE)+1)
#     END AS FEE 
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
# JOIN CAR_RENTAL_COMPANY_CAR as c
# ON h.CAR_ID = c.CAR_ID
# WHERE c.CAR_TYPE='트럭'
# ORDER BY FEE DESC, HISTORY_ID DESC

WITH RENTAL_INFO AS (
    -- 1. 트럭의 대여 정보와 대여 기간 계산
    SELECT 
        h.HISTORY_ID,
        c.CAR_ID,
        c.DAILY_FEE,
        DATEDIFF(h.END_DATE, h.START_DATE) + 1 AS RENTAL_DAYS
    FROM CAR_RENTAL_COMPANY_CAR c
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h
    ON c.CAR_ID = h.CAR_ID
    WHERE c.CAR_TYPE = '트럭'
), DISCOUNT_INFO AS (
    -- 2. 할인율을 대여 기간에 맞게 매핑
    SELECT 
        d.CAR_TYPE,
        d.DURATION_TYPE,
        d.DISCOUNT_RATE,
        CASE 
            WHEN d.DURATION_TYPE = '7일 이상' THEN 7
            WHEN d.DURATION_TYPE = '30일 이상' THEN 30
            WHEN d.DURATION_TYPE = '90일 이상' THEN 90
        END AS MIN_DAYS
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
    WHERE d.CAR_TYPE = '트럭'
)
-- 3. 최종 대여 금액 계산 및 정렬
SELECT 
    r.HISTORY_ID,
    FLOOR(
        r.DAILY_FEE * r.RENTAL_DAYS * 
        (1 - COALESCE(
            (SELECT d.DISCOUNT_RATE / 100 
             FROM DISCOUNT_INFO d 
             WHERE r.RENTAL_DAYS >= d.MIN_DAYS 
             ORDER BY d.MIN_DAYS DESC 
             LIMIT 1), 
            0)
        )
    ) AS FEE
FROM RENTAL_INFO r
ORDER BY FEE DESC, HISTORY_ID DESC;
