# 두 재료의 고유한 번호를 합쳐서 M(1 ≤ M ≤ 10,000,000)이 되면 갑옷이 만들어진다
# 재료의 개수 N(1 ≤ N ≤ 15,000) /  갑옷을 만드는데 필요한 수 M(1 ≤ M ≤ 10,000,000) 
# N개의 재료들이 가진 고유한 번호들이 공백을 사이에 두고 주어진다
#  갑옷을 만들 수 있는 개수를 출력하는 프로그램

# for문 이용 -> 시간초과 발생
# Two pointers 알고리즘
import sys
input = sys.stdin.readline


n = int(input())
m = int(input())

lst = list(map(int,input().split()))
           
lst.sort()

start, end = 0, n-1
cnt = 0

while start < end:
    
    result = lst[start] + lst[end]
    
    if result > m:
        end -= 1
    
    elif result < m:
        start += 1
    
    else:
        cnt += 1
        start += 1
        end -= 1
        
print(cnt)