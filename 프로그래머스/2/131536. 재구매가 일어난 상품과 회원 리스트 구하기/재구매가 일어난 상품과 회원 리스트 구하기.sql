# -- 코드를 입력하세요
# SELECT USER_ID, PRODUCT_ID
# from online_sale
# GROUP BY USER_ID, PRODUCT_ID
# #HAVING COUNT(*) >= 2

# select USER_ID, PRODUCT_ID
select USER_ID, PRODUCT_ID
from ONLINE_SALE
group by USER_ID, PRODUCT_ID
HAVING COUNT(*) >= 2
order by USER_ID, PRODUCT_ID desc
