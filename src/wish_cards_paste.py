from PIL import Image, ImageDraw
import sys
from os import listdir
from os.path import isfile, join

wishpath="img/wishes/"
wish_files = [join(wishpath,f) for f in listdir(wishpath) if isfile(join(wishpath, f)) and f != ".gitignore"]

combi = []
i0 = Image.open(wish_files[0])
x, y = i0.size

for i in range(len(wish_files)):
    combi.append(wish_files[i])

    if i % 16 == 0 and i != 0:
        im = Image.new("RGB", (4*x,4*y), "white")
        draw = ImageDraw.Draw(im)

        start = i - 16
        for j1 in range(1,5):
            for j2 in range(1,5):
                img = Image.open(wish_files[start + (j1-1)*4 + j2 - 1])
                x, y = img.size
                im.paste(img, (x*j2-x,y*j1-y,x*j2,y*j1))
        im.save("printing/Wish"+str(i-16)+"-"+str(i)+".png")
        del combi[:]
