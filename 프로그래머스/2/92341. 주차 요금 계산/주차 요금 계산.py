# 2022 KAKAO BLIND RECRUITMENT > 주차 요금 계산
import math
from collections import defaultdict

def cal(total, fees):
    if total <= fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((total - fees[0]) / fees[2]) * fees[3]


def solution(fees, records):
    answer = []
    carIn = []
    total_time = defaultdict(int)  # 차량별 누적 시간

    for record in records:
        lst = record.split(" ")
        
        # 입차
        if lst[-1] == "IN":
            carIn.append([lst[1], lst[0]])  # [차번호, 시간]
        
        # 출차
        else:
            for i in range(len(carIn)):
                if carIn[i][0] == lst[1]:
                    inTime = carIn[i][1]
                    outTime = lst[0]
                    
                    # 시간 계산
                    in_h, in_m = map(int, inTime.split(":"))
                    out_h, out_m = map(int, outTime.split(":"))
                    total = (out_h - in_h) * 60 + (out_m - in_m)
                    
                    total_time[lst[1]] += total
                    
                    carIn.pop(i)  # 제거 (중요!)
                    break

    # 출차 안 된 차량 → 23:59 처리
    for car, inTime in carIn:
        in_h, in_m = map(int, inTime.split(":"))
        out_h, out_m = 23, 59
        total = (out_h - in_h) * 60 + (out_m - in_m)
        
        total_time[car] += total

    # 차량 번호 기준 정렬
    for car in sorted(total_time.keys()):
        answer.append(cal(total_time[car], fees))

    return answer