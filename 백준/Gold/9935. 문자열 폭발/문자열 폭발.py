# stack 이용
# stack에 글자 하나씩 넣으면서 b와 맞나 확인하기

stack = []

a = input()
b = input()

for i in a:
    stack.append(i)
    
    if stack[len(stack)-len(b)::] == list(b):
        for _ in range(len(b)):
            stack.pop()

if stack:
    print(*stack,sep='')
else:
    print("FRULA")
