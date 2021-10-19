import pyqrcode
import png
from pyqrcode import QRCode

linkqrcode = 'https://github.com/daviwiliam'

url = pyqrcode.create(linkqrcode)

url.png(r'qr.png', scale=8)