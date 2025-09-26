# -- 코드를 작성해주세요
select i.ITEM_ID, i.ITEM_NAME, i.RARITY
from ITEM_INFO as i
join ITEM_TREE as t on i.ITEM_ID = t.ITEM_ID
where PARENT_ITEM_ID in (select ITEM_ID from ITEM_INFO where RARITY = 'RARE')
order by ITEM_ID desc
