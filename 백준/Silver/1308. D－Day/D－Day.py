# 오늘이 y년 m월 d일이고, D-Day가 y+1000년 m월 d일과 같거나 늦다면 "gg" 출력
# date.fromordinal(ordinal) => 1년1월1일 이후로 누적된 날짜로부터 date 객체 반환

from datetime import *

today = list(map(int, input().split()))
d_day = list(map(int, input().split()))

if today[0] + 1000 < d_day[0]:
    print("gg")

elif today[0] + 1000 == d_day[0] and today[1] <= d_day[1] and today[2] <= d_day[2]:
    print("gg")

else:
    today = date(*today)
    d_day = date(*d_day)
    print("D-"+str(d_day.toordinal() - today.toordinal()))