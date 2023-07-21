data = open(r'D:\Загрузки\evil2.gfx', 'rb').read()

for i in range(5):
    open('%d.jpg' % i, 'wb').write(data[i::5])