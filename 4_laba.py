def z25():
    try:
        a = int(input('Введите число,которое хотите проверить деление на 3='))
        b =a % 3
    except ValueError:
        print ('введено не число')
    else:
        if b == 0 and a!= 0:
            print('это число делится на 3!')
        elif a == 0:
            print('это ноль')
        else:
            print('число не делится на 3!')
z25()

def z26():
    try:
        a = int(input("введите число:"))
        b= 100/a
    except ZeroDivisionError:
         print('введен 0')
    except ValueError:
        print('введено не число')
    else:
        print('результат деления 100 на это число',b)
z26()


def z27():
    date = input("ведите в формате дд.мм.гггг:" )
    date = date.split('.')
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print ('Дата магическая')
    else:
         print('Дата не является магической')
z27()

def z28():
  ticket = input('введите номер билета:')
  try:
    x = 0
    y = 0
    if len(ticket) % 2 ==0:
        for i in ticket[0:int(len(ticket) / 2)]:
            x=x+int(i)
        for i in ticket[int(len(ticket) / 2):int(len(ticket))+1]:
             y = y + int(i)
        if x == y:
            print('билет счастливый')
        else:
            print('билет несчастливый')
  except:
         print ('что-то не так')
z28()