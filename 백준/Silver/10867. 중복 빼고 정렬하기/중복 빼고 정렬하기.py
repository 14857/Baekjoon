n = int(input())
n_lst = list(map(int,input().split()))

n_lst = set(n_lst)
n_lst = sorted(n_lst)

print(*n_lst)