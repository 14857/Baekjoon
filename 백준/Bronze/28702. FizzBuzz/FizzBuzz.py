# 연속으로 출력된 세 개의 문자열
# [i + 입력값]이 모두 동일하다

for i in range(3,0,-1): # 연속으로 출력된 세 개의 문자열
    x = input()
    
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x) + i

if (n%3 == 0) and (n%5 == 0):
    ans = 'FizzBuzz'

elif (n%3 == 0):
    ans = 'Fizz'

elif (n%5 == 0):
    ans = 'Buzz'

else:
    ans = n
        
print(ans)