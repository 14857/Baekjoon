a,b,v = map(int,input().split())

if (v-b)%(a-b) == 0:
    ans = (v-b)//(a-b)

else:
    ans = (v-b)//(a-b)+1
    
print(int(ans))