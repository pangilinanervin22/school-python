# import webbrowser

# import pyqrcode


# def makeSomething():
#     print("start")
#     qr = pyqrcode.create("https://www.youtube.com/")
#     qr.png("sample.png", scale=8)
#     webbrowser.open("sample.png")

#     print("done")

import qrcode

text = "https://www.example.com"

# Generate a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the text to the QR code
qr.add_data(text)
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
file_path = "wew.png"
qr_image.save(file_path)
