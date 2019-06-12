money = input('금액 : ')
money = int(money)

a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0

if(money>50000):
    a=money//50000
    money-=a*50000

if(money>10000):
    b=money//10000
    money-=b*10000

if(money>5000):
    c=money//5000
    money-=c*5000

if(money>1000):
    d=money//1000
    money-=d*1000

if(money>500):
    e=money//500
    money-=e*500

if(money>100):
    f=money//100
    money-=f*100

if(money>50):
    g=money//50
    money-=g*50

if(money>10):
    h=money//10
    money-=h*10

if(money>5):
    i=money//5
    money-=i*5

if(money>1):
    j=money//1
    money-=j*1

print('50000원 : ',a,'개')
print('10000원 : ',b,'개')
print('5000원 : ',c,'개')
print('1000원 : ',d,'개')
print('500원 : ',e,'개')
print('100원 : ',f,'개')
print('50원 : ',g,'개')
print('10원 : ',h,'개')
print('5원 : ',i,'개')
print('1원 : ',j,'개')