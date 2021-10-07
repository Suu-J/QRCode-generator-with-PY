import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

#creating QR code

qr = pyqrcode.create(input("Enter text to turn into QR code"))
qr.png("MyCode.png",scale =8)

#reading QR code
d = decode(Image.open("MyCode.png"))
print(d[0].data.decode("ascii"))