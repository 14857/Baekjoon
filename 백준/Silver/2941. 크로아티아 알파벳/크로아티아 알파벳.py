lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']

s = input()

for i in lst:
    s = s.replace(i,'*')
    
ans = len(s)
print(ans)