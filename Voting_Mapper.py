import argparse
from collections import defaultdict
from itertools import groupby
from operator import itemgetter
import sys

__author__ = 'srajpx'

new_list = []
merge_list = []
new_dict = defaultdict()
n_list = []


def add_2_lst(nline):
    new_list.append(nline)


def read_data(fname):
    ofile = open(fname, 'r')
    for line in ofile:
        add_2_lst(line.rstrip().split('\t'))


def readargs():
    parser = argparse.ArgumentParser(description="Readfile Python")
    parser.add_argument("-v", "--vfile", help="Voter Votee file")
    parser.add_argument("-w", "--wfile", help="Voter Worth file")
    args = parser.parse_args()
    # file_path = args.ifile
    #print(file_path)
    return args


def main():
    if len(sys.argv) < 1:
        print("Usage: ReadFile.py <path>")
        sys.exit(0)
    else:
        args = readargs()
        read_data(args.vfile)
        del new_list[0]
        for e in new_list:
            n_list.append(e)
        new_list.clear()
        read_data(args.wfile)
        del new_list[0]
        merge_list = n_list + new_list
        sorted_lst = sorted(merge_list, key=itemgetter(0))
        fo = open('Voting_Output.txt', 'w+')
        for c, g in groupby(sorted_lst, key=itemgetter(0)):
            vals = (set(a for c, a in g))
            vals = ','.join(sorted(vals))
            new_dict[c] = vals
        for e in sorted(new_dict.items()):
            str = "%s\t%s\n" % (e[0], e[1])
            print(str)
            fo.write(str)
        fo.close()


if __name__ == "__main__":
    main()