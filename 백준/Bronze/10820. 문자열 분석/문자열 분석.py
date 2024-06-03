while True:
    try:
        s = input()
    
    except EOFError:
        break

    a,b,c,d = 0,0,0,0
        
    for i in s:
        if i.islower():
            a += 1
        elif i.isupper():
            b += 1
        elif i.isdigit():
            c += 1
        elif i == " ":
            d += 1
        
    print(a,b,c,d)
