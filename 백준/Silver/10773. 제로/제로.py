num_list = []

k = int(input())


for _ in range(k):
    
    num = int(input())
    
    if num == 0:
        del num_list[len(num_list)-1]
        
    else:
        num_list.append(num)

print(sum(num_list))