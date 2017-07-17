"""iLovePDF

Usage:
    ipdf.py compress [-o FILE] [--verbose] [--overwrite] INPUT...
    ipdf.py merge [-o FILE] [--verbose] INPUT...
    ipdf.py split [-o FILE] [--verbose] --ranges=RANGES INPUT...

Options:
    -h --help       Show this screen
    -o FILE         Specify output file. If no file is provided, output file
                    will be overwritten
    INPUT           Specify input file
    -v --verbose    Show messages
    --overwrite     Overwrite the input file as output file. If it is set, the
                    option '-o FILE' is ignored
    --ranges=RANGES Page ranges to split the files. Every range will be saved
                    as different PDF file.
                    Example format: 1,5,10-14
"""

from docopt import docopt
from ilovepdf import ILovePdf
from ilovepdf import TASKS
import config
import logging
import logging.config

logging.config.fileConfig("logging.cfg")
logger = logging.getLogger()


def get_task(arguments):
    for task in TASKS:
        if arguments.get(task):
            return task


arguments = docopt(__doc__, version="iLovePDF 1.0")
i = ILovePdf(config.PUBLIC_KEY, config.SECRET_KEY, arguments["--verbose"])
task = get_task(arguments)
i.new_task(task)
for input_file in arguments["INPUT"]:
    i.add_file(input_file)
i.execute(ranges=arguments["--ranges"])
i.download(arguments["-o"], arguments["--overwrite"])
