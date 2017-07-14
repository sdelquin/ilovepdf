from ilovepdf import ILovePdf
import config
import os
from PyPDF2 import PdfFileReader


def test_compress():
    i = ILovePdf(config.PUBLIC_KEY, config.SECRET_KEY)
    i.new_task("compress")
    i.add_file("test.pdf")
    i.execute()
    i.download("out.pdf")
    input_file = PdfFileReader(open("test.pdf", "rb"))
    output_file = PdfFileReader(open("out.pdf", "rb"))
    assert output_file.getNumPages() == input_file.getNumPages()
    assert os.path.getsize("out.pdf") < os.path.getsize("test.pdf")


def test_merge():
    i = ILovePdf(config.PUBLIC_KEY, config.SECRET_KEY)
    i.new_task("merge")
    for _ in range(3):
        i.add_file("test.pdf")
    i.execute()
    i.download("out.pdf")
    input_file = PdfFileReader(open("test.pdf", "rb"))
    output_file = PdfFileReader(open("out.pdf", "rb"))
    assert output_file.getNumPages() == 3 * input_file.getNumPages()
