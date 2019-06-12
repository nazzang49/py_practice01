menu = input('메뉴 : ')

dic = {};
if(menu=='어묵'):
    dic={'price':500}
elif(menu=='순대'):
    dic={'price':1000}
elif(menu=='김밥'):
    dic={'price':5000}
else:
    dic = {'price': 0}

print('가격 : {price}'.format(price=dic['price']))