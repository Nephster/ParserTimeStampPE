from pefile import *
from pathlib import Path
import datetime
import time
from os.path import exists
import sys


def main(folder):
    if not exists(folder):
        print("Folder {} doesnt exist".format(folder))
        return 0
    for fn in Path(folder).glob("*.*"):
        try:
            pe = PE(fn)
            print(fn,datetime.datetime.fromtimestamp(pe.FILE_HEADER.TimeDateStamp))
        except PEFormatError as err:
            print ("{} in file {}".format(err, fn))
            continue

if __name__ == "__main__":
    main(sys.argv[1])