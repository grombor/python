""" main"""

from logging import log
from os import write
from typing_extensions import ParamSpec
from PyPDF2 import PdfFileReader
from pathlib import Path
from PyPDF2.pdf import DocumentInformation, PdfFileWriter
from pdf_splitter import *


# path to my .pdf file
input_path = (
    Path.home() / "git" / "python" / "pdf_challenge" / "document.pdf"
)

# set breakpoint at page ...
breakpoint = 4

ps = pdf_splitter(input_path)
ps.split(4)
