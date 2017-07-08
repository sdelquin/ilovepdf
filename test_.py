from ilovepdf import ILovePdf
import config
import os


def test_compress():
    i = ILovePdf(config.PUBLIC_KEY, config.SECRET_KEY)
    i.new_task("compress")
    i.add_file("test.pdf")
    i.execute()
    i.download("out.pdf")
    assert os.path.getsize("out.pdf") < os.path.getsize("test.pdf")
