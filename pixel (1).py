# run pip install pillow to install
import sys
from PIL import Image

def main(filter1, compressor):
    image = Image.open('jump2.jpeg')
    image.show()
    n=1
    if compressor == 1:
        n=2
    width, height = image.size
    wid =width/n
    hgt = height/n
    new_image_size =  (int(wid), int(hgt))
    new_image = Image.new("RGB", (new_image_size), "White")
    if compressor == 1:
        shrink(image, compressor, width, height, new_image)
    if compressor == 0:
        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                filterblocks(new_image, filter1,x,y,r,g,b)
        new_image.save("new_image.jpeg")
    if compressor == 2:
        hide(image, new_image, width, height)
    if compressor == 3:
        show(image, new_image, width, height)

def filterblocks(new_image,filter1,x,y,r,g,b):
    if filter1 == 1:
        new_image.putpixel((flip(x),y),(grayscale(r,g,b)))
    if filter1 == 2:
        new_image.putpixel((flip(x),y),(redshift(r,g,b)))
    if filter1 == 3:
        new_image.putpixel((flip(x),y),(invert(r,g,b)))

def grayscale(r,g,b):
    avg = (int(r)+int(g)+int(b))/3
    new_r = int(avg)
    new_g = int(avg)
    new_b = int(avg)
    return new_r, new_g, new_b

def flip(x):
    if flipper == 1:
        return -x
    else:
        return x

def hide(image, new_image, width, height):
    a = 0
    mess = input("Secret Message:")
    messy_string = str_to_binary(mess)
    print(messy_string)
    for i in range(8*(width*height)):
        messy_string += str(0)
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            stringr = ""
            stringg = ""
            modr = r - r%16
            modg = g - g%16
            stringr = str(format(modr,'#010b'))
            stringg = str(format(modg,'#010b'))
            stringr = stringr[2:]
            stringg = stringg[2:]
            propr = ""
            propr += str("0b")
            propr += stringr
            propr = propr[:6]
            propg = ""
            propg += str("0b")
            propg += stringg
            propg = propg[:6]
            propr += messy_string[a]
            propr += messy_string[a+1]
            propr += messy_string[a+2]
            propr += messy_string[a+3]
            propg += messy_string[a+4]
            propg += messy_string[a+5]
            propg += messy_string[a+6]
            propg += messy_string[a+7]
            actr=int(propr, 2)
            actg=int(propg, 2)
            new_image.putpixel((x,y),(actr,actg,b))
            a = a + 8
    new_image.save("new_image.jpeg")

def show(image, new_image, width, height):
    for x in range(1):
        for y in range(10):
            r, g, b = image.getpixel((x, y))
            print(r,g)
            rawr = ""
            rawr = str(bin(r))
            rawg = ""
            rawg = str(bin(g))
            full_bit = ""
            full_bit += rawr[6:]
            full_bit += rawg[2:6]
            print(full_bit)
            print(chr(int(full_bit,2)))



def redshift(r,g,b):
    avg = (int(g)+int(b))/2
    new_r = r
    new_g = int(avg)-10
    new_b = int(avg)-10
    return new_r, new_g, new_b

def shrink(image, compressor, width, height, new_image):
    w=0
    z=0
    if compressor == 1:
        for x in range(0,width-1,2):
            z=0
            for y in range(0,height-1,2):
                r1, g1, b1 = image.getpixel((x, y))
                r2, g2, b2 = image.getpixel((x+1, y))
                r3, g3, b3 = image.getpixel((x+1, y+1))
                r4, g4, b4 = image.getpixel((x, y+1))
                compr=(r1+r2+r3+r4)/4
                compg=(g1+g2+g3+g4)/4
                compb=(b1+b2+b3+b4)/4
                try:
                    filterblocks(new_image, filter1,w,z, int(compr),int(compg),int(compb))
                except(IndexError):
                    pass
                z=z+1
            w=w+1
        new_image.save("new_image.jpeg")

def invert(r,g,b):
    avg = (int(g)+int(b))/2
    new_r = 255-r
    new_g = 255-g
    new_b = 255-b
    return new_r, new_g, new_b

def str_to_binary(string):
    binary_list = []
    for char in string:
        binary_list.append(bin(ord(char))[2:].zfill(8))
    return ''.join(binary_list)

if __name__ == "__main__":
    filter1 = int(sys.argv[1])
    flipper = int(sys.argv[2])
    compressor = int(sys.argv[3])
    main(filter1, compressor)
