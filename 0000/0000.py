#!/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

#im = Image.open('penguin.jpg')
#w, h = im.size
#im.thumbnail((w//10, h//10))
#im.save('penguin_new.jpg', 'jpeg')
imn = Image.open('0000.jpg')
w, h = imn.size
font = ImageFont.truetype('/usr/share/fonts/smc/Meera.ttf', 100)
draw = ImageDraw.Draw(imn)
draw.text((w*0.8, 1), "6", font=font, fill=(255, 0, 0))
imn.save('0000_new.jpg', 'jpeg')
