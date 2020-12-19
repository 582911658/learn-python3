print('请输入一个数字判断是否为偶数')
number = input('>')
if int(number) % 2 == 0:
    print('\nThe number '+str(number)+' is even.')
else:
    print('\n The number '+str(number)+' is odd.')
