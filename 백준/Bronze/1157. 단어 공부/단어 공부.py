word = input().upper()
word_list = list(set(word))
ans = []

for i in word_list:
    count = word.count(i)
    ans.append(count)

if ans.count(max(ans))>= 2:
    print("?")
else:
    print(word_list[ans.index(max(ans))])