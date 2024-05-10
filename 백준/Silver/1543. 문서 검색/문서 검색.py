document = input()
word = input()
count = 0

while True:
    if word not in document:
        break
    else:
        document = document.replace(word, '@')
        
for i in document:
    if i == "@":
        count += 1

print(count)