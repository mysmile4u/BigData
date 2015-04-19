from collections import defaultdict
from itertools import groupby
from operator import itemgetter
import sys

__author__ = 'srajpx'

new_list = []
nlist = []
separator = '\t'
fnl_diction = defaultdict(str)

def add_2_lst(nline):
    new_list.append(nline)


def read_data(fname):
    ofile = open(fname, 'r')
    for line in ofile:
        add_2_lst(line.rstrip().split('\t'))


def main():
    read_data(sys.argv[1])
    sorted_lst = sorted(new_list, key=itemgetter(1))
    for c, g in groupby(sorted_lst, key=itemgetter(1)):
        for e in g:
            nlist.append(e)
        for e in nlist:
            s = e[0]
            fnl_diction[e[1]] += ''.join(s)+"  "
        nlist.clear()
    for e in fnl_diction.items():
        str = "%s\t%s\n" % (e[0],e[1])
        print(str)

if __name__ == "__main__":
    main()