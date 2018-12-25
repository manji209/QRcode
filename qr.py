# Import QR Code library
import qrcode
import csv


with open('sku.csv', 'r') as f:
    reader = csv.reader(f)
    item_list = list(reader)


for item in item_list:
    # Create qr code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=2,
    )
    # Add data
    qr.add_data(item[0])
    qr.make(fit=True)
    # Create an image from the QR Code instance
    img = qr.make_image()
    # Save it somewhere, change the extension as needed:
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    img.save("./codes/"+item[0]+".jpg")


'''
# The data that you want to store
data = "The Data that you need to store in the QR Code"


# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save it somewhere, change the extension as needed:
# img.save("image.png")
# img.save("image.bmp")
# img.save("image.jpeg")
img.save("./codes/image.jpg")
'''