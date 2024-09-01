names = []

a = input()
n = int(input())

for _ in range(n):
    name = input()
    
    L = a.count("L") + name.count("L")
    O = a.count("O") + name.count("O")
    V = a.count("V") + name.count("V")
    E = a.count("E") + name.count("E")
    
    
    total = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) %100
    
    names.append([name,total])

names = sorted(names, key=lambda x: (-x[1],x[0]))


print(names[0][0])