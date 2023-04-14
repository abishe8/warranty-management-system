import sqlite3
import io
import pytesseract
from PIL import Image
import imghdr
import re

# Connect to the database
conn = sqlite3.connect('C:/Users/R.Adhithiyaram/invoice.db')
cursor = conn.cursor()

# Select the invoice document from the database
cursor.execute(
    "SELECT document FROM Invoice WHERE invoice_no = ?", ('001',))
row = cursor.fetchone()
invoice_document = row[0]

# Convert the invoice document from binary to image
img_bytes = io.BytesIO(invoice_document)
img_bytes.seek(0)  # Helps to refresh the pointer location

#Identify the image format and display the format
format = imghdr.what(None, h=img_bytes.read(32))
if format:
    print(f"Image format: {format}")
else:
    print("Unknown image format")

img = Image.open(img_bytes)

# Use Tesseract OCR to extract the invoice number from the image
text = pytesseract.image_to_string(img)
print(text)  # whole image text

# Define regular expressions for the invoice number and date and match it in the text
invoice_number_regex = re.compile(r'Invoice Number: \s*([A-Za-z0-9-]+)', re.IGNORECASE)
invoice_number_match = invoice_number_regex.search(text)
if invoice_number_match:
    invoice_number = invoice_number_match.group(1)
    print("Invoice number:", invoice_number)
else:
    print("Invoice number not found.")
    print("Enter the Invoice No manually")
     # map the corresponding fields from html site

text = str(text) #to avoid bitwise & error in invoice_date_match as types of 'str' and 'int'
invoice_date_regex = re.compile(r'Invoice Date: \s*(\d{2}.\d{2}.\d{4})')
invoice_date_match = invoice_date_regex.search(text)
if invoice_date_match:
    invoice_date = invoice_date_match.group(1)
    print("Invoice date:", invoice_date)
else:
    print("Invoice date not found.")
    print("Enter the Invoice Date manually")
    # map the corresponding fields from html site


# Print the invoice number and date
'''print('Invoice Number:', invoice_number)
\s*(\w+-\d{6})
print('Invoice Date:', invoice_date)'''
