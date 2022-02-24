import pefile
from pathlib import Path
import datetime
from os.path import exists
import sys
import argparse
from collections import OrderedDict

peTimeStamps = {}

def main():
    parser = argparse.ArgumentParser(description="Parsing timestamp of PE file",epilog="Usage: ParserTimeStampPE.py -f <folder>")
    parser.add_argument("-f","--folder",help="Folder where are PE files")
    args = parser.parse_args()
    folder = args.folder

    if not exists(folder):
        print("Folder {} doesnt exist".format(folder))
        return 0
    w = open(folder + "\\" + "TimeStamp.txt", 'w')
    
    for fn in Path(folder).glob("*.*"):
        try:
            pe = pefile.PE(fn)
            #print(fn,datetime.datetime.fromtimestamp(pe.FILE_HEADER.TimeDateStamp))
            #w.write("{} {} \n".format(fn,datetime.datetime.fromtimestamp(pe.FILE_HEADER.TimeDateStamp)))
            peTimeStamps[Path(fn).name] = datetime.datetime.fromtimestamp(pe.FILE_HEADER.TimeDateStamp)
        except pefile.PEFormatError as err:
            print ("{} in file {}".format(err, fn))
            continue
    s = sorted(peTimeStamps,key = lambda x:peTimeStamps[x])
    for i in s:
       w.write("{}:{}\n".format(i,peTimeStamps[i]))
    w.close()
if __name__ == "__main__":
    main()