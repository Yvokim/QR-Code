import qrcode

# Step 1: Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Version of QR code (size)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box (pixel size)
    border=4,  # Border size
)

# Step 2: Add data (URL) to the QR code
qr.add_data('https://www.example.com')

# Step 3: Create the QR code
qr.make(fit=True) # will adjust the version if predefined isnt big enough.

# Step 4: Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Step 5: Save the QR code image
img.save('example_qr.png')
