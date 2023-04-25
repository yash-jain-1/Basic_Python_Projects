# Simple Image to PDF  coverter using predefined package
import img2pdf
image = input("Enter the name of the file:")
with open(image, 'rb'):
  img = f.read()
pdf_bytes = img2pdf.convert(img)
with open('output.pdf', 'wb' ):
  f.write(pdf_bytes)
