# 테스트 케이스의 개수 T(1 ≤ T ≤ 100) / 두 정수 A, B(-2^31 ≤ A, B ≤ 2^31-1)
# 1을 더하거나 뺄 수 있기 떄문에 모든 경우에서 가능

for _ in range(int(input())):
    a, b = map(int, input().split())

    print("yes")
