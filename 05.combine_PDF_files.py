#! python3
# Combines all the PDFs in the current working directory into a single PDF.

import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF2.PdfWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    # Loop through all the pages (except the first) and add them.
    for pagenum in range(1, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pagenum]
        pdfWriter.add_page(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

