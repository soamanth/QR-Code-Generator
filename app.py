import os
import qrcode

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

text = input("Enter text or URL: ")

img = qrcode.make(text)

img.save("output/qr.png")

print("✅ QR Code generated successfully!")
print("📁 Saved as: output/qr.png")