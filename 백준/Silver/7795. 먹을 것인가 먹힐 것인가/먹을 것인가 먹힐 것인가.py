# 브루트포스 
# A는 자기보다 크기가 작은 먹이만 먹을 수 있다
# 테스트 케이스의 개수 T /  A의 수 N과 B의 수 M (1 ≤ N, M ≤ 20,000 )
# A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A.sort()
    B.sort()

    start = 0
    ans = 0
 
    for i in range(N):
        while True:
            if start == M or A[i] <= B[start]:
                ans += start
                break
            else:   
                start+=1
                
    print(ans)