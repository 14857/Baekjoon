import sys; input = sys.stdin.readline

# N을 B진법으로 변환. 뒤집지 않고 반환한다.
def change(N, B):
    res = []
    while N:
        N, r = divmod(N, B)
        res.append(r)
    return res

def NimSum(B, X, Y):
    if X < Y: # X에 Y를 더하기 위해 길이가 X가 Y보다 같거나 길게 한다.
        X, Y = Y, X
    X = change(X, B)
    Y = change(Y, B)

    for i in range(len(Y)): # Y의 길이만큼 각 자리마다 계산
        X[i] = (X[i] + Y[i]) % B

    res = 0; b = 1 # 결과를 10진수 변환
    for i in range(len(X)):
        res += X[i] * b
        b *= B
    return res

for _ in range(int(input())):
    B, X, Y = map(int, input().split())
    print(NimSum(B, X, Y))