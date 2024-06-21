# 파이썬 내장 함수 이용 -> pow(a,b,c)
import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

print(pow(a,b,c))
