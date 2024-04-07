-- 코드를 입력하세요
/*
SELECT first_half.flavor,(first_half.TOTAL_ORDER + sum(JULY.TOTAL_ORDER)) as total
from FIRST_HALF, JULY
where FIRST_HALf.shipment_id = JULY.shipment_id
group by first_half.flavor
order by total desc
limit 3;
*/

SELECT first_half.flavor
from FIRST_HALF, JULY
where FIRST_HALf.FLAVOR = JULY.FLAVOR
group by first_half.flavor
order by first_half.TOTAL_ORDER + sum(JULY.TOTAL_ORDER) desc
limit 3
;