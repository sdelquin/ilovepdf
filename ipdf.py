"""iLovePDF

Usage:
    ipdf.py TASK [-o FILE] [--verbose] [--overwrite] INPUT...

Options:
    -h --help       Show this screen
    TASK            Task to perform: merge, split, compress, pdfjpg, imagepdf,
                    unlock, pagenumber, watermark, officepdf, repair, rotate,
                    protect, pdfa, validatepdfa, extract
    -o FILE         Specify output file. If no file is provided, output file
                    will be overwritten
    INPUT           Specify input file
    -v --verbose    Show messages
    --overwrite     Overwrite the input file as output file. If it is set, the
                    option '-o FILE' is ignored
"""

from docopt import docopt
from ilovepdf import ILovePdf
import config
import logging
import logging.config

logging.config.fileConfig("logging.cfg")
logger = logging.getLogger()

arguments = docopt(__doc__, version="iLovePDF 1.0")

i = ILovePdf(config.PUBLIC_KEY, config.SECRET_KEY, arguments["--verbose"])
i.new_task(arguments["TASK"])
for input_file in arguments["INPUT"]:
    i.add_file(input_file)
i.execute()
i.download(arguments["-o"], arguments["--overwrite"])
