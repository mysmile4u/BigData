from collections import defaultdict
from operator import itemgetter
import sys

__author__ = 'srajpx'

new_list = []
one_dict = defaultdict()
one_list = []


def add_2_lst(nline):
    new_list.append(nline)


def read_data(fname):
    ofile = open(fname, 'r')
    for line in ofile:
        add_2_lst(line.rstrip().split('\t'))


def main():
    read_data("Voting_Output.txt")
    fo = open("Voting_Output_1.txt", 'w+')
    for e in new_list:
        str = e[1]
        str_split = str.split(',')
        val = str_split[0]
        j = 1
        while 0 < j < len(str_split):
            one_dict[str_split[j]] = val
            j += 1
        one_dict[e[0]] = 0
        for f in one_dict.items():
            one_list.append(f)
        one_dict.clear()
    print(one_list)
    for e in sorted(one_list, key=itemgetter(0)):
        str = "%s\t%s\n" % (e[0], e[1])
        fo.write(str)
    fo.close()


if __name__ == "__main__":
    main()
