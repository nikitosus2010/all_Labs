
n=int(input("кол-во слов:"))
words=[]
for i in range(n):
    word=input("введите слово:")
    words.append(word)
    print(" ".join(words))

stroka=""
i=""
while "stop"!=i:
    stroka += i+" "
    i=input("Дай слово: \n")
    words.append(stroka)
    print(i+stroka)


strok = ""
i = ""
while "stop" != i:
     strok += i + " "
     i = input("Дай слово: \n")
     words.append(strok)
     if "ф" in i or "Ф" in i:
         print("крутое слово")
     else:
         print("гадкое слово")


import random
prav=0
nprav=0
pop=0
while pop!=3:
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    otvet=int(input(str(a)+"+"+str(b)+"="))
    if otvet==a+b:
        print("Хорош!")
        prav+=1
    else:
        print("пробуй ещё, малыш")
        pop+=1
print("Игра окончена! Количество правильных ответов:",prav)
