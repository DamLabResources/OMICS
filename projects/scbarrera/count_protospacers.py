#!/usr/bin/env python3
"""Count how many times protopacer shows up"""
# print(f'NAME: {__name__}')

from os.path import join
from collections import Counter
from glob import glob


#glob = get list of base names 
def main():
    x20_pat = "/home/jupyter-sb4476/projects/sbCRISPRSCREEN/02.reads_20nt/SRR*_20nt.fasta"
    # files_x20 = glob(join(x20_pat, 'SRR*_20nt.fasta'))
    files_x20 = glob(x20_pat)
    assert files_x20, f'NO FILES FOUND IN: {x20_pat}'

    # collect all lines from all files
    # fin means files in- defined below
    lines = []
    for fin in files_x20:
        lines.extend(_read(fin))
    assert lines, 'NO LINES FOUND'

    # taking top 5
    ctr = Counter(lines)
    for val, qty in ctr.most_common(5):
        print(f'{qty:6,} {val}', end='')


# loop variable  = loop fin into read function
def _read(fin):
    with open(fin, encoding='utf8') as ifstream:
        return ifstream.readlines()

if __name__ == '__main__':
    main()
