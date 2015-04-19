import argparse
from collections import defaultdict
import re
import sys

__author__ = 'srajpx'

diction = defaultdict()
new_diction = defaultdict()
list = []


def readargs():
    parser = argparse.ArgumentParser(description="Readfile Python")
    parser.add_argument("-i", "--ifile", help="input file")
    args = parser.parse_args()
    file_path = args.ifile
    print(file_path)
    return file_path


def clean_line(line):
    line = re.sub(r'\W+', ' ', line)
    return line.lower().split(' ')


def readfile(fname):
    file = open(fname, 'r')
    for line in file.readlines():
        line_cleaned = clean_line(line)
    return line_cleaned


def main():
    if len(sys.argv) < 1:
        print("Usage: ReadFile.py <path>")
        sys.exit(0)
    else:
        fpath = readargs()
        cleanline = readfile(fpath)  # readfile('ana_file.txt')
        for e in cleanline:
            diction[e] = sorted(e)
        for e in diction.items():
            new_diction[e[0]] = ''.join(e[1])
        fo = open("ana_output.txt", 'w+')
        for e in new_diction.items():
            str = "%s\t%s\n" % (e[0], e[1])
            fo.write(str)
        fo.close()


if __name__ == "__main__":
    main()