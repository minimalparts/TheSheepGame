from PIL import Image, ImageDraw, ImageFont
import sys
import textwrap

font = ImageFont.truetype("AnnabelScript.ttf", 72)
font2 = ImageFont.truetype("Raleway-Regular.ttf", 30)
cardtitle="Life"

life_file = open("lists/lifecards.txt", "r")
life_cards = life_file.read().splitlines()
life_file.close()

card_number = 0
for i in range(len(life_cards)):
    card_text = life_cards[i]
    if card_text == "" or card_text[0] == '#':
        continue
    card_number+=1
    print(card_number,card_text)
    filename="img/life/life"+str(card_number)+".png"

    im = Image.new("RGB", (700,423), "white")
    box = im.getbbox()
    draw=ImageDraw.Draw(im)
    draw.rectangle((2, 2, 698, 421), fill="white", outline="black")
    draw.text((box[2]-470,box[1]+20), cardtitle, fill=0, font=font)

    fromtop=150
    for toprint in textwrap.wrap(card_text, width=40):
        draw.text((box[2]-650,box[1]+fromtop), toprint, fill=0,font=font2)
        fromtop=fromtop+40
	
    del draw 
    im.save(filename)


