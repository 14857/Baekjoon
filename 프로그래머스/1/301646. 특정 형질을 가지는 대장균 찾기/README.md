특정 형질을 가지는 대장균 찾기 - 301646

🧩 문제 링크

https://school.programmers.co.kr/learn/courses/30/lessons/301646

---

📝 문제 설명

특정 형질 조건을 만족하는 대장균의 개수를 조회하는 SQL 문제.

조건:

- 2번 형질이 없는 개체
- 1번 또는 3번 형질을 가진 개체

---

💻 풀이 SQL

SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0
  AND (
        (GENOTYPE & 1) != 0
        OR
        (GENOTYPE & 4) != 0
      );

---

📌 비트마스크 정리

형질| 값
1번| 1
2번| 2
3번| 4
4번| 8
