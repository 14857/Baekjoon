# 길이가 짧은 것부터 sort(), 길이가 같으면 사전 순으로 sort(key = len)
# 중복 출력 X -> set

num = int(input())
words = []

for _ in range(num):
    s = input()
    words.append(s)

# 중복 제거
words_set = set(words)
words = list(words_set)

# 정렬
words.sort()
words.sort(key = len)

for i in range(len(words)):
    print(words[i])