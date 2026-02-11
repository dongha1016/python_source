month = int(input('월 : '))

if month % 10 == 1 or month % 10 == 2:
    print('winter')
elif month // 3 == 1:
    print('spring')
elif month // 6 == 1:
    print('summer')
elif month // 9 == 1:
    print('fall')