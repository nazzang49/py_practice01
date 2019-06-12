# 키보드로 입력 받기

# input으로 입력 시 자동으로 String 클래스로 바인딩 됨
import sys

a = input('수 입력 : ')
a = int(a)

if(type(a)!=int):
    print('정수 아님')
    sys.exit(0)

if(a%3==0):
    print('3의 배수임')
else:
    print('3의 배수 아님')



