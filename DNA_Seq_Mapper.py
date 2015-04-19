import argparse
from collections import defaultdict
import re
import sys

__author__ = 'srajpx'

diction = defaultdict()
list = []

def readargs():
    parser = argparse.ArgumentParser(description="Readfile Python")
    parser.add_argument("-i", "--ifile", help="input file")
    args = parser.parse_args()
    file_path = args.ifile
    #print(file_path)
    return file_path


def readfile(fname):
    file = open(fname, 'r')
    for line in file.readlines():
        line = re.sub(r'\s+', ' ', line)
        line_cleaned = line.strip().split(' ')
        diction[line_cleaned[0]] = line_cleaned[1]
        #for e in line_cleaned:
         #   list.append(e)


def main():
    if len(sys.argv) < 1:
        print("Usage: ReadFile.py <path>")
        sys.exit(0)
    else:
        fpath = readargs()
        cleanline = readfile(fpath)  # readfile('DNA_File.txt')
        fo = open('DNA_Seq_Output.txt', 'w+')
        for e in diction.items():
            list.append(e)
            str = "%s\t%s\n" % (e[0], e[1])
            fo.write(str)
        fo.close()
        print(list)


if __name__ == "__main__":
    main()