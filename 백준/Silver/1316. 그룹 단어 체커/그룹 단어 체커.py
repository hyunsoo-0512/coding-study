입력값 = int(input())
갯수 = 0

for _ in range(입력값):
    단어 = input().strip()
    본거 = set()
    봤던_글자 = ''
    그룹여부 = True
    
    for 글자 in 단어:
        if 글자 != 봤던_글자:
            if 글자 in 본거:
                그룹여부 = False
                break
            본거.add(글자)
            봤던_글자 = 글자
    
    if 그룹여부:
        갯수 += 1

print(갯수)