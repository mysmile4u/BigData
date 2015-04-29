from collections import defaultdict
from itertools import groupby
from operator import itemgetter
import sys

__author__ = 'srajpx'

new_list = []
nlst = []
new_diction = defaultdict()
tlst = []


def add_2_lst(nline):
    new_list.append(nline)


def read_data(fname):
    ofile = open(fname, 'r')
    for line in ofile:
        add_2_lst(line.rstrip().split('\t'))


def main():
    read_data("Word_Predection_Output.txt")
    sorted_lst = sorted(new_list, key=itemgetter(0))
    for e in sorted_lst:
        # print(e)
        lst = e[0]
        cnt = e[1]
        lst_splt = lst.split('&')
        str = "%s&%s" % (cnt, lst_splt[1])
        #print(lst_splt[0],"    ",str)
        new_diction[lst_splt[0]] = str
        for j in new_diction.items():
            nlst.append(j)
        new_diction.clear()
    # print(nlst)
    sorted_lst = sorted(nlst, key=itemgetter(0))
    for c, g in groupby(sorted_lst, key=itemgetter(0)):
        gl = list(g)
        j = 0
        lt = min(5, len(gl))
        while 0 <= j < lt:
            ntup = gl[j][1].split('&')
            tlst.append(ntup[1])
            j += 1
        #print(c, ":         ", ','.join(tlst))
        print ('{0}     :       {1}'.format(c,  ','.join(tlst)))
        tlst.clear()


if __name__ == "__main__":
    main()