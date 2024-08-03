#3차 제출
# 추가 반례에서 오답
# 고려 사항 -> 같은 자리수가 더 큰 수가 되도록 -> 해결완료(인덱스로 반복문)
# 추가 고려사항 -> 자릿수가 크다고 해서 항상 큰 수로 해당하는 것이 틀릴 수 있다.
# 자릿수 값에 따른 가중치 고려하기
import sys
from collections import defaultdict

n = int(input())
ans = 0
count = 9
#maxlength = 0

s = [] #단어 저장
w = defaultdict(int)  # 알파벳에 따른 숫자 정보 저장
dic = {}

for _ in range(n):   
    word = list(input())
    s.append(word)
    for i in range(len(word)-1,-1,-1):
        w[word[i]] += 10**(len(word)-i)

# 가중치에 따라 역순 정렬
w = sorted(w.items(),key = lambda x : x[1], reverse = True)

# ---------------------------------------
for i,j in w:
    dic[i] = str(count)
    count -= 1    
#----------------------------------------
#최종 계산
for i in s:
    nums = ''
    
    for j in range(len(i)):
        nums += str(dic[i[j]])
        
    #print(nums)
    ans += int(nums)
            
print(ans)