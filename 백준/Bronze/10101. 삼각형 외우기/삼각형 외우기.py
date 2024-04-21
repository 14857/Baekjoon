tri = []

for _ in range(3):
    tri.append(int(input()))

if tri == [60,60,60]:
    print("Equilateral")
    
elif sum(tri) == 180 and (tri[0]==tri[1] or tri[0]==tri[2] or tri[1]==tri[2]):
    print("Isosceles")

elif sum(tri) == 180 and tri[0]!=tri[1]!=tri[2]:
    print("Scalene")

else:
    print("Error")