from django.test import TestCase
import cv2
import pytesseract
from pdf2image import convert_from_path
import fitz
import docx

img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow('Result', img)
# cv2.waitKey(0)

print(pytesseract.image_to_string(img))
"""--------------------------------------------------------------------------"""
# pages = convert_from_path('321.pdf', 100)
# pages[0].save('out.jpg', 'JPEG')
#
# imgcv = cv2.imread('out.jpg')
# imgcv = cv2.cvtColor(imgcv, cv2.COLOR_BGR2RGB)
#
# print(pytesseract.image_to_string(imgcv))

"""------------------------------------------------------------------------------"""

# file = fitz.open('321.pdf')
#
# doc = docx.Document()
#
# for pageNum, page in enumerate(file.pages(), start=1):
#     text = page.get_text()
#     doc.add_paragraph(text)
#     doc.save('test.docx')
#     if pageNum == 1:
#         break











