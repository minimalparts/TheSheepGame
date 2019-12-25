from PIL import Image, ImageDraw, ImageFont
import sys
import textwrap

font = ImageFont.truetype("AnnabelScript.ttf", 72)
font2 = ImageFont.truetype("Raleway-Regular.ttf", 30)
cardtitle='Wish'

wish_file = open("lists/wishes.txt", "r")
wish_cards = wish_file.read().splitlines()
wish_file.close()

card_number = 0
for i in range(len(wish_cards)):
    card_text = wish_cards[i]
    if card_text == "" or card_text[0] == '#':
        continue
    card_number+=1
    print(card_number,card_text)
    filename="img/wishes/wish"+str(card_number)+".png"


    im = Image.new("RGB", (423,600), "white")
    box = im.getbbox()
    draw=ImageDraw.Draw(im)
    draw.rectangle((2, 2, 421, 598), fill="white", outline="black")
    draw.text((box[2]-300,box[1]+50), cardtitle, fill=0, font=font)

    fromtop=220
    for toprint in textwrap.wrap(card_text, width=20):
        draw.text((box[2]-340,box[1]+fromtop), toprint, fill=0, font=font2)
        fromtop=fromtop+60
	
    del draw 
    im.save(filename)


