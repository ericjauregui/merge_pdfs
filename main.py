from PyPDF2 import PdfMerger
from os import listdir, path

# cwd = os.path.dirname(os.path.abspath(__file__))

pdfs = [i for i in listdir("input/") if i.endswith(".pdf")]
print("pdfs to merge:\n", pdfs)

merger = PdfMerger()

mapped = [merger.append(path.join("input", pdf)) for pdf in pdfs]

merger.write("output/merged_pdf.pdf")
print("\n merged_pdf.pdf created in output/ !")
merger.close()