def z1():
    from PIL import Image
    img = Image.open(r'Z:\1-MД-20\pythonProject13\dada.jpg')
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img2 = img.crop((0, 0, 250, 120))
    if img.mode != 'RGB':
        img2 = img.convert('RGB')
    img2.save(r'Z:\1-MД-20\pythonProject13\dada2.jpg')
z1()

def z2():
    from PIL import Image
    papa = {"Новый год": "postcard.jpg", "День рождения": "dr.jpg", "8 марта": "8m.jpg", "День защитника": "23f.jpg"}
    p = input("Введите праздник: ")
    if p not in papa:
        print("отсутствует")
    else:
     img = papa.get(p)
     image = Image.open(img)
     image.show()
z2()

def z3():
    from PIL import Image,ImageDraw, ImageFont
    img = Image.open(r'Z:\1-MД-20\pythonProject13\dada.jpg')
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img2 = img.crop((0, 0, 250, 120))
    if img.mode != 'RGB':
        img2 = img.convert('RGB')
    img2.save(r'Z:\1-MД-20\pythonProject13\dada2.jpg')
    n = input("Кого вы хотите поздравить: ")
    tekst1 = str(n)
    tekst2 = " поздравляю!"
    p = ImageDraw.Draw(img2)
    font = ImageFont.truetype("arial_bold.ttf", size=25)
    p.text((50, 50), tekst1, font=font, fill="black",stroke_width=2,stroke_fill="black")
    p.text((38, 75), tekst2, font=font, fill="red",stroke_width=2,stroke_fill="red")
    img2.show()
    img2.save(r'Z:\1-MД-20\pythonProject13\dada3.png')
z3()