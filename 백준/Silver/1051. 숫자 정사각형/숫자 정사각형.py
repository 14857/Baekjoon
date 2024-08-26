# N과 M은 50보다 작거나 같은 자연수
# 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램

def correct(s):
    for i in range(n-s+1): 
        for j in range(m-s+1): 
            if nums[i][j] == nums[i][j+s-1] == nums[i+s-1][j] == nums[i+s-1][j+s-1]:
                return True

    return False


n, m = map(int, input().split())
nums = [list(map(int, list(input()))) for _ in range(n)]

# 꼭짓점에 쓰여 있는 수가 큰 경우부터
for k in range(min(n,m), 0, -1):
    # 네 꼭지점의 크기가 같은 정사각형을 찾으면 종료
    if correct(k):
        print(k**2)
        break
