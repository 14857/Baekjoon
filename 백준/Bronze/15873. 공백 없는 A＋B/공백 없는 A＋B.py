#b가 10인 경우 / b가 10보다 작은 경우
n= input()


if n[-2] + n[-1] == "10":  
    print( int(n[:-2]) + 10)
else:
    print( int(n[:-1]) + int(n[-1]) )