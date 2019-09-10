
## Pillow is the Python Imaging Library
## Import pillow
from PIL import Image
from PIL import ImageFilter
import os

#
print(os.getcwd())
os.chdir('./additionals/Images')
print(os.getcwd())

## Open Image
my_image = Image.open('Kitty1.jpg')
my_image.show()

#
# os.mkdir('PNG')
os.chdir('./PNG')
print(os.getcwd())

## Save image
my_image.save('Kitty1.png')

#
print(os.getcwd())
os.chdir('..')
print(os.getcwd())

## Convert all the jpg files into png files
for index, f in enumerate(os.listdir('.'), start=1) :
    if f.endswith('.jpg') :
        i = Image.open(f)
        fname, fextens = os.path.splitext(f)
        i.save(f'PNG/{fname}.png')

#
# os.mkdir('300')
print(os.getcwd())

## Change file size
image_size = (300, 300)

for index, f in enumerate(os.listdir('.'), start=1) :
    if f.endswith('.jpg') :
        i = Image.open(f)
        fname, fextens = os.path.splitext(f)
        i.thumbnail(image_size)
        i.save(f'300/{fname}_300.png')

#
# os.mkdir('700')
print(os.getcwd())

## Change file size
image_size = (700, 700)

for index, f in enumerate(os.listdir('.'), start=1) :
    if f.endswith('.jpg') :
        i = Image.open(f)
        fname, fextens = os.path.splitext(f)
        i.thumbnail(image_size)
        i.save(f'700/{fname}_700.png')

#
# os.mkdir('MOD')
print(os.getcwd())

## Rotating images
my_image = Image.open('Kitty1.jpg')
my_image.rotate(90).save('./MOD/Kitty1_Rotated.jpg')

## Convert the image into white black
my_image = Image.open('Kitty1.jpg')
my_image.convert(mode='L').save('./MOD/Kitty1_WhiteBlack.jpg')

## Blured image
my_image = Image.open('Kitty1.jpg')
my_image.filter(ImageFilter.GaussianBlur()).save('./MOD/Kitty1_Blurred0.jpg')
my_image.filter(ImageFilter.GaussianBlur(15)).save('./MOD/Kitty1_Blurred15.jpg')
