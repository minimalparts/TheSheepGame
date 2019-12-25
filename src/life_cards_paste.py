from PIL import Image, ImageDraw
import sys
from os import listdir
from os.path import isfile, join

lifepath="img/life/"
life_files = [join(lifepath,f) for f in listdir(lifepath) if isfile(join(lifepath, f))]

combi = []
i0 = Image.open(life_files[0])
x, y = i0.size

for i in range(len(life_files)):
    combi.append(life_files[i])

    if i % 9 == 0 and i != 0:
        im = Image.new("RGB", (3*x,3*y), "white")
        draw = ImageDraw.Draw(im)

        start = i - 9
        for j1 in range(1,4):
            for j2 in range(1,4):
                img = Image.open(life_files[start + (j1-1)*3 + j2 - 1])
                x, y = img.size
                im.paste(img, (x*j2-x,y*j1-y,x*j2,y*j1))
        im.save("printing/Life"+str(i-9)+"-"+str(i)+".png")
        del combi[:]
