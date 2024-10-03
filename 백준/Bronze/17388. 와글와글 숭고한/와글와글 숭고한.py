# 숭실대학교의 참여도, 고려대학교의 참여도, 한양대학교의 참여도를 의미하는 세 자연수 S, K, H

s,k,h = map(int,input().split())

if s+k+h >= 100:
    print("OK")
else:
    if min(s,k,h) ==s:
        print("Soongsil")
    elif min(s,k,h) ==k:
        print("Korea")
    else:
        print("Hanyang")