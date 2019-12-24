from PIL import Image, ImageDraw, ImageFont
import sys
import textwrap

font = ImageFont.truetype("AnnabelScript.ttf", 72)
font2 = ImageFont.truetype("NewCenturySchoolbook.ttf", 32)

cardtitle="Life"
filename="img/life/"+sys.argv[1]+".png"

im = Image.new("RGB", (700,423), "white")
box = im.getbbox()
draw=ImageDraw.Draw(im)
draw.rectangle((2, 2, 698, 421), fill="white", outline="black")
draw.text((box[2]-470,box[1]+20), cardtitle, fill=0, font=font)

text = open("msg.txt", "r")
textlines=text.readlines()
text.close()

fromtop=150
for line in textlines:
	for toprint in textwrap.wrap(line, width=40):
		draw.text((box[2]-650,box[1]+fromtop), toprint, fill=0, font=font2)
		fromtop=fromtop+40
	

del draw 
im.save(filename)


