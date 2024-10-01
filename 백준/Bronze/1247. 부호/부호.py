# N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램
import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    total = 0

    for _ in range(n):
        total += int(input())


    if total == 0:
        print("0")

    elif total>0:
        print("+")

    else:
        print("-")