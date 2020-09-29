grn = int(input('введите гривны: '))
kop=int(input('введите копейки: '))
if grn >999 or grn < 0 or kop < 0 or kop > 99:
    print('вы ввели недопустимое число')
elif grn == 0:
    if kop == 0:
        print('вы ввели сумму равную 0. Верно?')
    elif 4 < kop < 21 or 4 < kop % 10 < 10 or kop % 10 == 0:
        print(kop, 'копеек')
    elif kop % 10 == 1:
        print(kop, 'копейка')
    elif 1 < kop % 10 < 5:
        print(kop, 'копейки')
elif 4 < grn < 21 or 4 < grn % 10 < 10 or grn % 10 == 0:
    if kop == 0:
        print(grn, 'гривен')
    elif 4 < kop < 21 or 4 < kop % 10 < 10 or kop % 10 == 0:
        print(grn, 'гривен,', kop, 'копеек')
    elif kop % 10 == 1:
        print(grn, 'гривен,', kop, 'копейка')
    elif 1 < kop % 10 < 5:
        print(grn, 'гривен,', kop, 'копейки')
elif grn % 10 == 1:
    if kop == 0:
        print(grn, 'гривна')
    elif 4 < kop < 21 or 4 < kop % 10 < 10 or kop % 10 == 0:
        print(grn, 'гривна,', kop, 'копеек')
    elif kop % 10 == 1:
        print(grn, 'гривна,', kop, 'копейка')
    elif 1 < kop % 10 < 5:
        print(grn, 'гривна,', kop, 'копейки')
elif 1 < grn % 10 < 5:
    if kop == 0:
        print(grn, 'гривны')
    elif 4 < kop < 21 or 4 < kop % 10 < 10 or kop % 10 == 0:
        print(grn, 'гривны,', kop, 'копеек')
    elif kop % 10 == 1:
        print(grn, 'гривны,', kop, 'копейка')
    elif 1 < kop % 10 < 5:
        print(grn, 'гривны,', kop, 'копейки')


...










