# 팰린드롬인지 확인 
def palin(search) :
    for i in range(len(search)//2) :
        if search[i] != search[-(i+1)] :
            return False 
    return True 

# 전부 같은 문자열인지 확인 
def same(search) :
    for i in range(1,len(search)) :
        if search[i] != search[0] : return False 
    return True 

if __name__=="__main__" :
    char = input()
    #  회문일 경우 
    if palin(char) :
        # 모두 같으면 -1  아니면 전체길이에서 -1 
        print(-1 if same(char) else len(char)-1)
    # 회문이 아닐 경우
    else :
        print(len(char))