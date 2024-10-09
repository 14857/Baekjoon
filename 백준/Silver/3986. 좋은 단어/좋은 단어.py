# 만약 선끼리 교차하지 않으면서
# 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면
# 그 단어는 '좋은 단어'
# 좋은 단어의 수를 출력하는 프로그램

n = int(input())
ans = 0

for _ in range(n):
    stack = []
    word = list(input())
    
    for i in word:
        if not len(stack):
            stack.append(i)
        
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)
            
    if not len(stack) :
        ans += 1

print(ans)
