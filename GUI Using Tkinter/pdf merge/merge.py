from PyPDF2 import PdfMerger
merge = PdfMerger()
merge.append("first.pdf")
merge.append("second.pdf")
merge.write("merged.pdf")
merge.close()
print("PDFs merged successfully!")