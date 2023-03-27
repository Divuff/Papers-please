from PIL import ImageGrab

arstotzka = (211, 236, 211)

px = ImageGrab.grab().load()
for y in range(1099, 1101):
    for x in range(499, 501):
        color = px[x, y]
        print(color)

if color == arstotzka:
    status = ('GLORY TO ARSTOTZKA')
    print('GLORY TO ARSTOTZKA')
else:
    print('Denied')
    status = ('Denied')