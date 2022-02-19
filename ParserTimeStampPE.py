import pefile
from pathlib import Path
import datetime
from os.path import exists
import sys
import argparse

def main(folder):
    parser = argparse.ArgumentParser(description="Parsing timestamp of PE file",epilog="Usage: ParserTimeStampPE.py -f <folder>")
    parser.add_argument("folder",help="Parsing timestamp of PE file")
    parser.add_argument("-f","--folder",help="Folder where are PE files")
    args = parser.parse_args()
    folder = args.folder

    if not exists(folder):
        print("Folder {} doesnt exist".format(folder))
        return 0

    for fn in Path(folder).glob("*.*"):
        try:
            pe = pefile.PE(fn)
            print(fn,datetime.datetime.fromtimestamp(pe.FILE_HEADER.TimeDateStamp))
        except pefile.PEFormatError as err:
            print ("{} in file {}".format(err, fn))
            continue

if __name__ == "__main__":
    main()