def z1():
 stran={'Россия':'Москва','Англия':'Лондон','Украина':'Киев','Франция':'Париж'}
 print(stran)
 for strana, stolisa in stran.items():
   print(strana,":",stolisa)
 try:
   strana = input("введите название страны:")
   print(strana,":",stran[strana])
 except KeyError:
     print('Такой страны нет')
 sorted(stran.items())
 s_stran=dict(sorted(stran.items()))
 print(s_stran)
z1()

def z2():
 o = {'а': 1,'в': 1,'е': 1,'и': 1,'н': 1,'о': 1,'р': 1,'с': 1,'т': 1, 'д': 2,'к': 2,'л': 2,'м': 2,'п': 2,'у': 2, 'б': 3,'г': 3,'ё': 3,'ь': 3,'я': 3, 'й': 4,'ы': 4, 'ж': 5,'з': 5,'х': 5,'ц': 5,'ч': 5, 'ш': 8,'э': 8,'ю': 8,'ф': 10,'щ': 10,'ъ': 10}
 name = input('Введите слово():').lower()
 stoim = 0
 try:
  for shislo in name:
     stoim=stoim+o[shislo]
 except KeyError:
     print("Пиши на русском")
 print("Кол-во очков:",name,"равно:",stoim)
z2()

def z3():
 studenti ={'Никита':{'Русский','Китайский','Итальянский'},'Костя':{'Русский','Английский'},'Дмитрий':{'Китайский','Английский'},'Михаил':{'Русский','Китайский','Португальский'}}
 yziki=set()
 kitai = []
 for ychenik, yzik in studenti.items():
     yziki.update(yzik)
     if 'Китайский' in yzik:
         kitai.append(ychenik)
 sorted_yziki = sorted(list(yziki))
 print(kitai)
 print(sorted_yziki)
z3()
