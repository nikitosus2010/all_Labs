def z1():
    import random
    numbers = []
    for i in range(5):
        numbers.append(random.randint(-10, 10))
    print (numbers)
    number= int(input('Введите число из списка:='))
    print (number)
    if number not in numbers:
        print(number, ' нет в списке')
    else:
        print(number,' есть в списке')

z1()

def z3():

    nums =[1,2,3,4,2]
    v = set()
    d = [x for x in nums if x in v or (v.add(x) or False)  ]
    print (d)

z3()

def z2():
    s = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
    d = int(input("сколько выходных?"))
    for i in s:
        print("Рабочие", *s[:-d])
        print("Выходные", *s[-d:])
        break

def z4():
    import random
    s1 =("Й","Ц","У","К","Е","Н","Г","Ш","Щ","З")
    s2 = ("Ф", "Ы", "В", "Иванов", "П", "Р", "О", "Л","Д","Ж")
    p1 = random.sample(s1, 5)
    p2 = random.sample(s2, 5)
    p3= tuple(sorted)p2+p1

    print('моя группа:',s2)
    print('другая группа:',s1)
    print('Спортивная команда:',p3)
    p3 = tuple(sorted(p3))
2
z4()

