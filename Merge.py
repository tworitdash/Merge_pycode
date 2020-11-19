from PyPDF2 import PdfFileMerger

pdfs = ['tworitdash_20200921_090835.pdf', 'tworitdash_20200921_090816.pdf']
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("Residence_Permit_TD.pdf")
