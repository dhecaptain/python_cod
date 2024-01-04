import pyqrcode
import png as pn
link="https://instagram.com/david_dhe_captain?igshid=MzMyNGUyNmU2YQ=="
qr_code=pyqrcode.create(link)
qr_code.pn("instagram.pn",scale=5)
