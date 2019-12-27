from PIL import Image, ImageDraw
import sys
from os import listdir
from os.path import isfile, join

moneypath="../img/money/"
money_files = [join(moneypath,f) for f in listdir(moneypath) if isfile(join(moneypath, f)) and f != ".gitignore"]

combi = []
i0 = Image.open(money_files[0])
x, y = i0.size

for i in range(len(money_files)):
    img = Image.open(money_files[i])
    im = Image.new("RGB", (4*x,4*y), "white")
    draw = ImageDraw.Draw(im)

    for j1 in range(1,5):
        for j2 in range(1,5):
            im.paste(img, (x*j2-x,y*j1-y,x*j2,y*j1))
    im.save("printing/Money"+str(i)+".png")
