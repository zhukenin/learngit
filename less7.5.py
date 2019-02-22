# -*- coding: utf-8 -*-
print('请输入小明的身高h ,体重w ')
hi = float(input('hi: '))
wi = float(input('wi: '))
bmi = int(wi/(hi**2))
print('bmi=  %.2f' % bmi)
if bmi < 18.5:
    print('过轻')
elif bmi >=18.5<=25:
    print('正常')
elif bmi >=25<=28:
    print('过重')
elif bmi >=28<=32:
    print('肥胖')
else:
    print('严重肥胖')
