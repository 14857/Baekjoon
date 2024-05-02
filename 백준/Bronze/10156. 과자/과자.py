#과자 한 개의 가격 K, 사려고 하는 과자의 개수 N, 현재 동수가 가진 돈 M
K,N,M = map(int,input().split())

if M>(K*N):
    print(0)
else:
    print((K*N)-M)