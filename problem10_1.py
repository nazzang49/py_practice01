a = input('숫자 입력 : ')
a = int(a)

sum=0
# for문 증가폭 설정 가능
if(a%2==0):
    for i in range(0, a + 1, 2):
        sum+=i
else:
    for i in range(1, a + 1, 2):
        sum+=i

print(sum)