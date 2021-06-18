# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 21:44:00 2021

@author: slims
img to word
"""

import pytesseract
from docx import Document
import regex as re
from tkinter import *
from tkinter import filedialog


# def remove_control_characters(html):
#     def str_to_int(s, default, base=10):
#         if int(s, base) < 0x10000:
#             return chr(int(s, base))
#         return default
#     html = re.sub(u"&#(\d+);?", lambda c: str_to_int(c.group(1), c.group(0)), html)
#     html = re.sub(u"&#[xX]([0-9a-fA-F]+);?", lambda c: str_to_int(c.group(1), c.group(0), base=16), html)
#     html = re.sub(u"[\x00-\x08\x0b\x0e-\x1f\x7f]", "", html)
#     return html


# def remove_control_characters(str):
#     return re.sub(r'\p{C}', '', 'my-string')

# text = remove_control_characters(output).strip()



root = Tk()
root.title('I2W')
# root.iconbitmap('C:/Users/slims/Downloads/image/A.png')
root.geometry('300x100')


def file_open():

	from PIL import Image

	root.filename = filedialog.askopenfilename(initialdir='C:/', title ='Select', filetypes=(('png files','*.png'),('all files','*.*')))
    
	pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

	img = Image.open(root.filename)

	output = pytesseract.image_to_string(img)


	text=output.strip()

	print(text)

	document = Document()

	document.add_paragraph(text)

	document.save('scanned.docx')
    




sec_butt = Button(root, text = 'Choose file', command=file_open).pack()










root.mainloop()