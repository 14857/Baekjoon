while True:
    a, b, c, d = map(int, input().split())
    count = 0
    if a == b == c == d == 0:
        break

    while not (a == b == c == d):
        a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
        count += 1
    
    print(count)