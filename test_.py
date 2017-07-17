from ilovepdf import ILovePdf
import config
import os
from PyPDF2 import PdfFileReader
import zipfile
import shutil
import glob


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
    os.remove("out.pdf")


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
    os.remove("out.pdf")


def test_split():
    i = ILovePdf(config.PUBLIC_KEY, config.SECRET_KEY)
    i.new_task("split")
    i.add_file("test.pdf")
    i.execute(ranges="1-2,5-8")
    i.download()
    zip_ref = zipfile.ZipFile("out.zip", "r")
    zip_ref.extractall("test_split")
    zip_ref.close()
    assert len(glob.glob("test_split/*.pdf")) == 2
    output_file1 = PdfFileReader(open("test_split/test-1-2.pdf", "rb"))
    output_file2 = PdfFileReader(open("test_split/test-5-8.pdf", "rb"))
    assert output_file1.getNumPages() == 2
    assert output_file2.getNumPages() == 4
    os.remove("out.zip")
    shutil.rmtree("test_split")


def test_pdfjpg():
    i = ILovePdf(config.PUBLIC_KEY, config.SECRET_KEY)
    i.new_task("pdfjpg")
    i.add_file("test.pdf")
    i.execute()
    i.download()
    zip_ref = zipfile.ZipFile("out.zip", "r")
    zip_ref.extractall("test_pdfjpg")
    zip_ref.close()
    input_file = PdfFileReader(open("test.pdf", "rb"))
    assert len(glob.glob("test_pdfjpg/*.jpg")) == input_file.getNumPages()
    os.remove("out.zip")
    shutil.rmtree("test_pdfjpg")
