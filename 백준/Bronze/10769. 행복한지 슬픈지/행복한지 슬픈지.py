import sys
input = sys.stdin.readline

s = input()

if s.count(":-)") + s.count(":-(") == 0:
     ans = "none"
elif s.count(":-)") == s.count(":-("):
     ans = "unsure"
elif s.count(":-)") > s.count(":-("):
    ans = "happy"
elif s.count(":-)") < s.count(":-("):
    ans = "sad"
    
print(ans)
