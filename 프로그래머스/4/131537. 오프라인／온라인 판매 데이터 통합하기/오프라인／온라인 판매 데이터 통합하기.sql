-- 코드를 입력하세요
WITH TOTAL_TABLE AS(
SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE DATE_FORMAT(SALES_DATE,'%Y-%m') = '2022-03'

UNION

SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE DATE_FORMAT(SALES_DATE,'%Y-%m') = '2022-03'
    )

SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM TOTAL_TABLE
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC


