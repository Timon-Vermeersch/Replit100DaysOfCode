from PyPDF2 import PdfReader
import os

directory = r'C:\Users\timon\documents'
filename = 'Thesis.pdf'
stream = os.path.join(f'{directory}' , f"{filename}")
print(stream)
reader = PdfReader(f'{stream}')

print(len(reader.pages))
doc = ''
for i in range(0, len(reader.pages)-1):
    text = reader.pages[i]
    lmao  = text.extract_text()
    doc += lmao


print(doc)