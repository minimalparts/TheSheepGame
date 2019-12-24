from PIL import Image, ImageDraw, ImageFont
import sys
import textwrap

font = ImageFont.truetype("AnnabelScript.ttf", 160)
font2 = ImageFont.truetype("Forgotte.ttf", 40)

cardtitle='wish'
filename="img/wish"+sys.argv[0]+".png"

im = Image.new("RGB", (423,700), "white")
box = im.getbbox()
draw=ImageDraw.Draw(im)
draw.rectangle((2, 2, 421, 698), fill="white", outline="black")
draw.text((box[2]-300,box[1]+50), cardtitle, fill=0, font=font)

text = open("msg.txt", "r")
textlines=text.readlines()
text.close()

fromtop=280
for line in textlines:
	for toprint in textwrap.wrap(line, width=21):
		draw.text((box[2]-380,box[1]+fromtop), toprint, fill=0, font=font2)
		fromtop=fromtop+60
	

del draw 
im.save(filename)


