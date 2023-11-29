import qrcode

# Replace 'https://your-username.github.io/your-repo' with the URL of your hosted HTML file
url = 'https://your-username.github.io/your-repo'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')

print('QR Code generated successfully!')
