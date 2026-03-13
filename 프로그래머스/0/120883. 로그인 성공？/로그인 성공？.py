def solution(id_pw, db):
    answer = ''
    
    id_db = []
    pw_db = []
    
    for i in db:
        id_db.append(i[0]) 
        pw_db.append(i[1]) 
        
    if(id_pw[0] in id_db):
        if(pw_db[id_db.index(id_pw[0])] == id_pw[1]):
            answer = "login"
        else:
            answer = "wrong pw"
    else:
        answer = "fail"
            
    return answer