qtd_hashtags = int(input())
hashtags = []
flag = False
''.split()
while qtd_hashtags > 0:
    hashtag = input()
    for character in hashtag:
        if ord(character) >= 65 and ord(character) <= 90:
            flag = True
            
    if not flag:
        hashtags.append(hashtag)
        
    flag = False
    
    qtd_hashtags -= 1

for hashtag in hashtags:
    for index in range(len(hashtags)-1):
        if hashtags[index] < hashtags[index+1]:
            hashtags[index], hashtags[index+1] = hashtags[index+1], hashtags[index]

for item in hashtags:
    print(item)