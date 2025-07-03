--  2021년도에 잡은 물고기 수를 출력
select count(ID) as FISH_COUNT
from FISH_INFO
where year(TIME) = 2021



