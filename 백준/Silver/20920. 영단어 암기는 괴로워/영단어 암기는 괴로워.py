# 단어장의 단어순서
# 주 나오는 단어일수록 앞에 배치한다.
# 해당 단어의 길이가 길수록 앞에 배치한다.
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

import sys
input = sys.stdin.readline

dic = {}

n,m = map(int,input().split())

for _ in range(n):
    word = input().strip()
    
    if(len(word)>=m):
    
        if word in dic:
            dic[word] += 1
        
        else:
            dic[word] = 1

dic = sorted(dic.items(), key=lambda item: (-item[1],-len(item[0]),item[0]))

for i in dic:
    print(i[0])