# 두 수 중 역순으로 정렬한 수 중 크기가 큰 수 구하기
A, B = input().split()

A = A[::-1]
B = B[::-1]

if (A<B):
    print(B)

else:
    print(A)