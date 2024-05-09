n = int(input())
company = set()

for i in range(n):
    name,record = input().split()
    
    if record == 'enter':
        company.add(name)
    
    elif record == 'leave':
        company.remove(name)
   
company = sorted(company, reverse = True)

for i in company:
    print(i)