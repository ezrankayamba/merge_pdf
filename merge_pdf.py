#!/usr/bin/env python
import os
import sys
from PyPDF2 import PdfFileMerger


def run():
    folder = "."
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    print("Folder: ", folder)
    os.chdir(folder)
    x = [a for a in os.listdir() if a.endswith(".pdf")]
    merger = PdfFileMerger()
    for pdf in x:
        merger.append(open(pdf, 'rb'))
    res_file = "result.pdf"
    with open(res_file, "wb") as fout:
        merger.write(fout)
    print(f"Successfully merged all PDF files in {folder} to {res_file}")
