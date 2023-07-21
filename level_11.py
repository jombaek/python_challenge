import requests
from io import BytesIO
from PIL import Image

us = 'huge'
pw = 'file'

session = requests.Session()
session.auth = (us, pw)

img = Image.open(BytesIO(session.get('http://www.pythonchallenge.com/pc/return/cave.jpg').content))
w, h = img.width, img.height

even = Image.new('RGB', (w // 2, h // 2))
odd = Image.new('RGB', (w // 2, h // 2))

for i in range(w):
    for j in range(h):
        p = img.getpixel((i, j))
        if (i + j) % 2 == 0:
            even.putpixel((i // 2, j // 2), p)
        else:
            odd.putpixel((i // 2, j // 2), p)

even.show()
odd.show()