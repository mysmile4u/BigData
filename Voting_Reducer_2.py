from itertools import groupby
from operator import itemgetter

__author__ = 'srajpx'

new_list = []
separator = '\t'

def add_2_lst(nline):
    new_list.append(nline)

def read_data(fname):
    ofile = open(fname, 'r')
    for line in ofile:
        add_2_lst(line.rstrip().split('\t'))

def main():
    read_data("Voting_Output_1.txt")
    fo = open("Voting_Output_2.txt", 'w+')
    sorted_lst = sorted(new_list, key=itemgetter(0))
    for current_letter, group in groupby(sorted_lst, key=itemgetter(0)):
        gl = list(group)
        tcnt = sum(int(count[1]) for count in gl)
        str = "%s%s%d\n" % (current_letter, separator, tcnt)
        fo.write(str)
        print(str)
    fo.close()

if __name__ == "__main__":
    main()
