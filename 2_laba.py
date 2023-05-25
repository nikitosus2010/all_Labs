def z1():
 p1 = input("")
 p2 = input("")
 if p1 == p2:
    print("Пароль принят")
 else:
    print("Пароль не принят")
z1()

def z2():
 place = int(input(""))
 if place in range(1, 36):
         if place % 2 == 0:
            print("Верхнее место в купе")
         else:
            print("Нижнее место в купе")
 if place in range(37, 54):
         if place % 2 == 0:
            print("Боковое верхнее")
         else:
            print("Боковое нижнее")
 if place in range(55, 1000):
            print("Ошибка")
z2()

def z3():
    year = int(input(""))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Год високосный")
    else:
        print("Год не високосный")
z3()

def z4():
    color_1 = input("Введите цвет (синий, красный, жёлтый) ")
    color_2 = input("Введите цвет (синий, красный, жёлтый) ")
    if color_1 == "красный" and color_2 == "синий" or color_1 == "синий" and color_2 == "красный":
        print("фиолетовый")
    elif color_1 == "красный" and color_2 == "жёлтый" or color_1 == "жёлтый" and color_2 == "красный" :
        print("оранжевый")
    elif color_1 == "синий" and color_2 == "жёлтый" or color_1 == "жёлтый" and color_ == "синий":
        print("зелёный")
    elif color_1 or color_2 != "красный" or "синий" or "жёлтый":
        print("Неправильный цвет")
z4()