# pip install qrcode
# pip install image

import qrcode    
import image
qr = qrcode.QRCode(
    version = 15,   # version of qrcode
    box_size = 10,  # size of the box where qrcode will be displayed 
    border = 5 ,    # it is the white part of the image -- border in all 4 sides with white colour 
)

data = "https://github.com/shubham-bhoite164"  # path of my github account 

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_colour = "white")
img.save("test.png")