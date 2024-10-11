# 3-동전수열 종류 8가지 -> 딕셔너리 사용
# 동전을 40번 던진 결과 +  3-동전수열 -> 반복문 범위 0~38

p = int(input())

for _ in range(p):
    dic = {"TTT": 0, "TTH": 0, "THT": 0, "THH": 0, "HTT": 0, "HTH": 0, "HHT": 0, "HHH": 0}
    
    s = input()
    
    for i in range(38):
        
        dic[s[i:i+3]] += 1
    
    for t, n in dic.items():
        print(n, end=' ')
    
    print()
