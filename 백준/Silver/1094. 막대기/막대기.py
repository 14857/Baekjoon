sticks = [64]
ans = 0
x= int(input())

while sum(sticks) > x:
    sticks.sort()
    if sum(sticks) - (min(sticks)//2) > x:
        sticks[0] = sticks[0]//2
        
    
    else:
        sticks.append(sticks[0]//2)
        sticks[0] = sticks[0]//2
        
for _ in sticks:
    if 0 in sticks:
        sticks.remove(0)

print(len(sticks))