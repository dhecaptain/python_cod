
from importlib.util import decode_source
import pyzbar 
from PIL import Image
decodeQR= decode_source(Image.open('instagram.png'))
print(decodeQR[0].data.decode('ascii'))