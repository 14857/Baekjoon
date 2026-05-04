# 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방
# 유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별

# 형식 :"Enter [유저 아이디] [닉네임]"
def solution(record):
    answer = []
    dic = {}
    
    for i in record:
        tmp = i.split()
        
        if tmp[0] == 'Enter':
            dic[tmp[1]] = tmp[2]
        elif tmp[0] == 'Change':
            dic[tmp[1]] = tmp[2]

    for i in record:
        tmp = i.split()
        
        if tmp[0] == 'Enter':
            answer.append(dic[tmp[1]]+'님이 들어왔습니다.')
        
        elif tmp[0] == 'Leave':
            answer.append(dic[tmp[1]]+'님이 나갔습니다.')

    return answer