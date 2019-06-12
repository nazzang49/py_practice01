s = input('문자 입력 : ')

def reverse(s):
    for i in range(0, len(s)):
        print(s[len(s)-1-i],end='')

reverse(s)