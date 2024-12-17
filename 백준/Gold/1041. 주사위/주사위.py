# 그리디 알고리즘
# 1개의 면만 보이는 주사위 -> 최솟값이기 때문에 무조건 가장 작은 값이 출력
# 2개의 면이 보이는 주사위 -> 다른 쌍이면서 가장 작은 값 두가지를 보이게 한다.
# 3개의 면이 보이는 주사위 -> 세 쌍중 작은 값들만 보이게 한다.

# N과 주사위에 쓰여 있는 수가 주어질 때,
# 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램

N = int(input())
dice = list(map(int,input().split(' ')))

square = N*N*5
answer = 0

if N == 1 :
    dice.sort()
    print(sum(dice[:5]))

else :
    answer = 0
    pair = []
    
    for i in range(3):
        pair.append(min(dice[i],dice[-1-i]))
    pair.sort()

    # 3면이 모두 보이는 경우
    answer += 4*sum(pair)
    square -= 4*3

    # 2면이 모두 보이는 경우
    answer += (8*N-12)*sum(pair[:2])
    square -= (8*N-12)*2
    
    # 1면만 보이는 경우
    answer += square*pair[0]
    print(answer)