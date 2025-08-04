"""
python tool
1.accepts pdf
2.extracts data(invoice number,date,amounts,tax)
3.validates keys(total=subtotal+tax)
4.output in format json
files passed through OCR
folder of pdfs(3-5)
"""
# %%
#imports
import PyPDF2
import pytesseract
import pandas as pd
# %%  
# %%
# convert pdf to image
# extract text from image
import pymupdf
# %%
# we have only one page/ pdf
def extract_text_from_pdf(path):
    images = pymupdf.open(path)
    for i, image in enumerate(images):
        text= image.get_text()
    return text
# %%
extract_text_from_pdf("invoice_template_2.pdf")
# %%
# 'INVOICE\n
# From: Design Studio, 789 Creative Blvd, Art City\n
# To: Jane Smith, 321 Client Ave, Project Town\n
# Date: 2025-07-09\n
# Invoice #: INV-1002\n
# Item\n
# Quantity
# \n
# Unit Price
# \n
# Total\nLogo Design\n1\n$500.00\n$500.00\nBrand Guidelines\n1\n$350.00\n$350.00\nTotal\n$850.00\n'

# extract invoice number,date,quantity,tax
import json 
import re
def extract_invoices(text):
    if "INV-" in text: #format of invoice:Inv-1002
        invoice_number = text[text.find("INV-"):text.find("INV-")+8]
    else:
        invoice_number = "Invalid"
    if "2025-" in text:
        date =text[text.find("2025-"):text.find("2025-")+10]
    else:
        date='Invalid'
    quantities=''
    l = text.split('\n')
    for i in l:
        if 'Quanntity' in i:
            w = i.split()
            for j in w:
                if(w>='0' and w<='9'):
                    quantities += w
    
    json_result={
        "invoice_number":invoice_number,
        "date":date,
        "quantity":quantities
    }
    with open("result.json","w") as f:
        json.dump(json_result,f)
    return json_result
