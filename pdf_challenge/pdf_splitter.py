from logging import debug
from os import path, write
from pathlib import Path
from PyPDF2.pdf import PdfFileReader, PdfFileWriter
from loguru import logger  as log

class pdf_splitter:
    
    def __init__(self, path):
        self.input_path = path

    def __str__(self):
        return print(f"Input path: {str(self.input_path)}")

    def split(self, breakpoint):

        # Open pdf file
        pdf_reader = PdfFileReader(str(self.input_path))
        pdf_writer = PdfFileWriter()

        def writer1():
            # copy all needed pages
            for page in range(0, breakpoint):
                new_page = pdf_reader.getPage(page)
                pdf_writer.addPage(new_page)

            # Open a pdf file to write
            with Path("chapter_1.pdf").open(mode="wb") as output_file:
                pdf_writer.write(output_file)


        def writer2():
            # copy all needed pages
            for page in range(breakpoint, pdf_reader.getNumPages()):
                new_page = pdf_reader.getPage(page)
                pdf_writer.addPage(new_page)

            # Open a pdf file to write
            with Path("chapter_2.pdf").open(mode="wb") as output_file:
                pdf_writer.write(output_file)

        writer1()
        writer2()
