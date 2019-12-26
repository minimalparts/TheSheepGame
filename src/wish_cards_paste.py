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

    if i % 30 == 0 and i != 0:
        im = Image.new("RGB", (6*x,5*y), "white")
        draw = ImageDraw.Draw(im)

        start = i - 30
        for j1 in range(1,6):
            for j2 in range(1,7):
                img = Image.open(wish_files[start + (j1-1)*5 + j2 - 1])
                x, y = img.size
                im.paste(img, (x*j2-x,y*j1-y,x*j2,y*j1))
        im.save("printing/Wish"+str(i-30)+"-"+str(i)+".png")
        del combi[:]
