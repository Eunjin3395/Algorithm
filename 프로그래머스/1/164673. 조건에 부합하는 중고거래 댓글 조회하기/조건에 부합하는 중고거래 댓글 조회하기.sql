-- 코드를 입력하세요
SELECT b.TITLE, 
    b.BOARD_ID, 
    r.REPLY_ID, 
    r.WRITER_ID,
    r.CONTENTS,
    date_format(r.CREATED_DATE,'%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD b
INNER JOIN USED_GOODS_REPLY r
ON b.board_id = r.board_id
where date_format(b.created_date,'%Y-%m')='2022-10'
order by r.created_date, b.title
