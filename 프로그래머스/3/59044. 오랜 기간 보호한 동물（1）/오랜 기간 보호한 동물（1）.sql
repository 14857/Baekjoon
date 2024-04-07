-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회
SELECT ANIMAL_INS.name, ANIMAL_INS.datetime
from ANIMAL_INS

where ANIMAL_INS.animal_id not in
    (select ANIMAL_INS.animal_id
    from animal_ins, animal_outs
    where ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID  )

order by datetime
limit 3
;