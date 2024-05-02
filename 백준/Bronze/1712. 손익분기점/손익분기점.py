# a: 고정 비용 / b: 가변비용 / c: 책정된 금액

a,b,c = map(int,input().split())


if b>=c:
    print(-1)
else:
    print(a//(c-b)+1)