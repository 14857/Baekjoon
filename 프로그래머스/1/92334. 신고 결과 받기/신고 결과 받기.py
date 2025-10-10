# 각 유저별로 처리 결과 메일을 받은 횟수
def solution(id_list, report, k):
    answer = [] 
    lst = [] # 신고 당한 ID (중복)
    final = [] # 정지된 ID    
    dic = {}
    
    for i in id_list:
        dic[i] = 0
    #print(dic)
    
    report = list(set(report)) # 중복 제거
    # print(report)
    
    for i in report:
        a,b = i.split(" ")
        lst.append(b)
        #print(lst)
        
    count_dic = {}
    for user in lst:
        count_dic[user] = count_dic.get(user, 0) + 1

    # 정지된 ID 목록
    for user, cnt in count_dic.items():
        if cnt >= k:
            final.append(user)

    # 메일 발송 수 세기
    for r in report:
        a, b = r.split(" ")
        if b in final:
            dic[a] += 1
    
    answer = list(dic.values())
    return answer