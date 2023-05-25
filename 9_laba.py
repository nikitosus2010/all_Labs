import os
import csv
from PIL import Image
d = r"D:\abadovskiy\8"
if os.path.isdir(r"D:\abadovskiy\8\прикол") == False:
   os.mkdir(r"D:\abadovskiy\8\прикол")
p = os.path.join(d , "прикол")
file_list =os.listdir(d)
for f in file_list:
 fail=os.path.join(r"D:\abadovskiy\8",f)
 if f.endswith('.jpg') or f.endswith('.png'):
     with Image.open(fail) as g:
      bot=g.transpose(Image.FLIP_TOP_BOTTOM)
      bot.save(os.path.join(p,f))
print(file_list)

def z2():
    d = r"D:\abadovskiy\papa.csv"
    with open(d) as f:
        stom=0
        r = csv.reader(f)
        print("Нужно купить:")
        for n in r:
            prod = n[0]
            kol = int(n[1])
            stoim = int(n[2])
            st=kol*stoim
            stom=stom+st
            print(prod, "-", kol,"шт. за",st)
        print("Общая сумма:",stom)
