# 이중 for문 사용 -> 메모리 초과 발생 -> 배열 할당으로 해결 불가
# n의 루트값과 연관있는 규칙 발견 (11122222333-)

import math

n = int(input())

ans = math.floor(n**0.5)
print(ans)