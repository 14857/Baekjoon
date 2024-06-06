import sys
input=sys.stdin.readline

n = int(input())
n_lst = list(map(int,input().split()))
x = int(input())

n_lst = sorted(n_lst)

count = 0
start = 0
end = n-1

while start < end:
    if n_lst[start] + n_lst[end] == x:
        count += 1
        start += 1
    elif n_lst[start] + n_lst[end] > x:
        end -= 1
    
    else:
        start += 1        

print(count)