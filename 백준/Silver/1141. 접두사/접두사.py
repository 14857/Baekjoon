# 접두사X 집합이란 집합의 어떤 한 단어가, 다른 단어의 접두어가 되지 않는 집합
# 단어 N개로 이루어진 집합이 주어질 때, 접두사X 집합인 부분집합 최대 크기 출력

n = int(input())
words = []
ans = 0

for _ in range(n):
    s = input()
    words.append(s)

words.sort(key = len)

for i in range(n):
    check = True
    for j in range(i+1,n):       
        
        if words[j].startswith(words[i]):
            check = False
        
    if check:
        ans += 1

print(ans)