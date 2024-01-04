import pyqrcode

link = "https://instagram.com/david_dhe_captain?igshid=MzMyNGUyNmU2YQ=="
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)
