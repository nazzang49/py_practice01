a = input('숫자 입력 : ')
a = int(a)

sum=0
if(a%2==0):
    for i in range(0, a+1):
        if(i%2==0):
            sum+=i
else:
    for i in range(0, a+1):
        if(i%2==1):
            sum+=i

print(sum)