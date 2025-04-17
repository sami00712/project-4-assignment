import qrcode

data = 'Qr CODE '
image = qrcode.make(data)
image.save('C:/Project 4 Assignments/Assignments 01/project 3, QR generator/my QR code.png')