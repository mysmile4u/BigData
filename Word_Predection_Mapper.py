import argparse
from collections import defaultdict
import sys
import re

__author__ = 'srajpx'

diction = defaultdict(int)


def clean_line(line):
    line = re.sub(r'\W+', ' ', line)
    return line.lower()


def readfile(fname):
    file = open(fname, 'r')
    for line in file.readlines():
        line_cleaned = clean_line(line)
        nline = (line_cleaned.strip().split(' '))
        j = 0
        while j < len(nline) - 1:
            str = "%s&%s" % (nline[j], nline[j + 1])
            #print(str)
            j += 1
            diction[str] += 1


def readargs():
    parser = argparse.ArgumentParser(description="Readfile Python")
    parser.add_argument("-i", "--ifile", help="input file")
    args = parser.parse_args()
    file_path = args.ifile
    #print(file_path)
    return file_path


def main():
    if len(sys.argv) < 1:
        print("Usage: ReadFile.py <path>")
        sys.exit(0)
    else:
        fpath = readargs()
        readfile(fpath) #readfile('Text_4m_H4.txt')
        fo = open("Word_Predection_Output.txt", 'w+')
        for e in diction.items():
            str = "%s\t%s\n" % (e[0], e[1])
            fo.write(str)
        fo.close()

# print(list(diction.items()))


if __name__ == "__main__":
    main()