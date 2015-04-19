__author__ = 'srajpx'
import argparse
from collections import defaultdict
import re
import sys


def clean_line(line):
    line = re.sub(r'\W+', '', line)
    return line.lower()


def readfile(fname):
    file = open(fname, 'r')
    for line in file.readlines():
        line_cleaned = clean_line(line)
    return line_cleaned


def readargs():
    parser = argparse.ArgumentParser(description="Readfile Python")
    parser.add_argument("-i", "--ifile", help="input file")
    args = parser.parse_args()
    file_path = args.ifile
    print(file_path)
    return file_path


def main():
    if len(sys.argv) < 1:
        print("Usage: ReadFile.py <path>")
        sys.exit(0)
    else:
        diction = defaultdict(int)
        fpath = readargs()
        cleanline = readfile(fpath)  #readfile('Test.txt')
        for letter in cleanline:
            diction[letter] += 1
    #print(list(diction.items()))
    fo = open("output.txt", 'w+')
    for ln in diction.items():
        str = "%a\t%d\n" % (ln[0], ln[1])
        #print(str)
        fo.write(str)
    fo.close()


if __name__ == "__main__":
    main()


