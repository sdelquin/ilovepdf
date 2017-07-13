"""iLovePDF

Usage:
    ipdf.py TASK [-o FILE] [--verbose] INPUT

Options:
    -h --help       Show this screen
    TASK            Task to perform: merge, split, compress, pdfjpg, imagepdf,
                    unlock, pagenumber, watermark, officepdf, repair, rotate,
                    protect, pdfa, validatepdfa, extract
    -o FILE         Specify output file. If no file is provided, output file
                    will be overwritten
    INPUT           Specify input file
    -v --verbose    Show messages
"""

from docopt import docopt
import sys
from ilovepdf import ILovePdf
import config
import logging
import logging.config

logging.config.fileConfig("logging.cfg")
logger = logging.getLogger()

TASKS = ("merge", "split", "compress", "pdfjpg", "imagepdf", "unlock",
         "pagenumber", "watermark", "officepdf", "repair", "rotate", "protect",
         "pdfa", "validatepdfa", "extract")

IMPLEMENTED_TASKS = ("compress")

arguments = docopt(__doc__, version="iLovePDF 1.0")

task = arguments["TASK"]
if task not in TASKS:
    logger.error("Chosen task '{}' is not available".format(task))
    sys.exit()
if task not in IMPLEMENTED_TASKS:
    logger.error("Chosen task '{}' is not yet implemented".format(task))
    sys.exit()

filename = arguments["INPUT"]
output_filename = arguments["-o"] or filename
i = ILovePdf(config.PUBLIC_KEY, config.SECRET_KEY, arguments["--verbose"])
i.new_task(task)
i.add_file(filename)
i.execute()
i.download(output_filename)
