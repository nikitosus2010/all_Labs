from PIL import Image,ImageFilter
image = Image.open(r'D:\abadovskiy\8\dada.jpg')
image.show()
print('Размер изображения:')
print(image.format, image.size, image.mode)


def z2():
  image = Image.open(r'D:\abadovskiy\8\dada.jpg')
  new_image = image.resize((160, 98))
  new_image.save(r'D:\abadovskiy\8\dada2.jpg')
  gor_image = new_image.transpose(Image.FLIP_TOP_BOTTOM)
  gor_image.save(r'D:\abadovskiy\8\dada3.jpg')
  vert_img = new_image.transpose(Image.FLIP_LEFT_RIGHT)
  vert_img.save(r'D:\abadovskiy\8\dada4.jpg')
z2()

def z3():
  image1 = Image.open(r'D:\abadovskiy\8\dada.jpg')
  image2=image1.filter(ImageFilter.CONTOUR)
  image2.save(r'D:\abadovskiy\8\dada5.jpg')
  image3 = Image.open(r'D:\abadovskiy\8\23f.jpg')
  image4 = image3.filter(ImageFilter.DETAIL)
  image4.save(r'D:\abadovskiy\8\dada6.jpg')
  image5 = Image.open(r'D:\abadovskiy\8\8m.jpg')
  image6 = image5.filter(ImageFilter.SHARPEN)
  image6.save(r'D:\abadovskiy\8\dada7.jpg')
  image7 = Image.open(r'D:\abadovskiy\8\dr.jpg')
  image8 = image7.filter(ImageFilter.SMOOTH)
  image8.save(r'D:\abadovskiy\8\dada8.jpg')
  image9 = Image.open(r'D:\abadovskiy\8\postcard.jpg')
  image10 = image9.filter(ImageFilter.EMBOSS)
  image10.save(r'D:\abadovskiy\8\dada9.jpg')
z3()

def z4():
  image1 = Image.open(r'D:\abadovskiy\8\dada.jpg')
  image2 = Image.open(r'D:\abadovskiy\8\23f.jpg')
  image1.putalpha(150)
  image2.paste(image1,(100,100),image1)
  image2.show()
  image2.save(r'D:\abadovskiy\8\dada10.jpg')
z4()
