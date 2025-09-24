select i.ITEM_ID, i.ITEM_NAME
from ITEM_INFO i
join ITEM_TREE t
on i.item_id = t.item_id
where t.PARENT_ITEM_ID is null
order by 1