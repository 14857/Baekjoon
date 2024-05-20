n = int(input())
ans = []

for _ in range (n):
    ans.append(int(input()))
    
if ans.count(1) > ans.count(0):
    print("Junhee is cute!")    

else:
    print("Junhee is not cute!")
    
    