a = [1,2,3,4,5,6,7,8,9]

count = 0
sum = 0

for i in range(0,len(a)):
    if(a[i]%3==0):
        count+=1
        sum+=a[i]

print('주어진 리스트에서 3의 배수의 갯수 : ', count)
print('주어진 리스트에서 3의 배수의 합 : ', sum)