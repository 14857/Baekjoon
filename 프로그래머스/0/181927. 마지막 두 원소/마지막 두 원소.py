def solution(num_list):
    answer = []
    answer = num_list
    
    if (num_list[-1] > num_list[-2]): # 마지막 원소가 더 큰 경우
        answer.append(num_list[-1] - num_list[-2])
    else:
        answer.append(num_list[-1]*2)
    return answer