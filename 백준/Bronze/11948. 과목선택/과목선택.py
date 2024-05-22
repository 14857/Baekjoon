a = []
b = []

a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))

b.append(int(input()))
b.append(int(input()))

a = sorted(a)
b = sorted(b)

print(a[-1] + a[-2] + a[-3]+ b[-1])