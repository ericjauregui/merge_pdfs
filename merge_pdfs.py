from PyPDF2 import PdfMerger
import os

cwd = os.path.dirname(os.path.abspath(__file__))

os.chdir(cwd.split('Projects')[0] + r'Downloads\Merge')
new_cwd = os.path.abspath(os.curdir)

pdfs = os.listdir()

merger = PdfMerger()

mapped = [merger.append(pdf) for pdf in pdfs]

merger.write('California Earrings Catalog July 2023.pdf')
merger.close()