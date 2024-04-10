# 강의 서쪽에는 N개의 사이트/동쪽에는 M개의 사이트
# 다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수
# 입력의 첫 줄에는 테스트 케이스의 개수 T
# 그 다음 줄부터 각각의 테스트케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 정수
# 각 테스트 케이스에 대해 주어진 조건하에 다리를 지을 수 있는 경우의 수를 출력
import math

T = int(input())

ans = []

for _ in range(T):
    N,M = map(int,input().split())
    ans.append(math.comb(M,N))

for i in range(T):
    print(ans[i])