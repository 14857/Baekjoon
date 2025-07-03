# -- 코드를 작성해주세요
select concat(quarter(DIFFERENTIATION_DATE),'Q') as QUARTER	, count(ID) as ECOLI_COUNT
from ECOLI_DATA
group by quarter
order by quarter