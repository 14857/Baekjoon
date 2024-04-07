-- 보호소에 들어올 당시에는 중성화1되지 않았지만, 
-- 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회
SELECT animal_ins.ANIMAL_ID,animal_ins.ANIMAL_TYPE,animal_ins.NAME
from animal_ins, animal_outs
where animal_ins.ANIMAL_ID = animal_outs.ANIMAL_ID
    AND animal_ins.SEX_UPON_INTAKE LIKE "Intact%"
    and (animal_outs.SEX_UPON_OUTCOME like "Neutered%"
        or animal_outs.SEX_UPON_OUTCOME like "Spayed%")

;