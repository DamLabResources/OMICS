#!/usr/bin/env python3
"""Count how many times protopacer shows up"""
# print(f'NAME: {__name__}')

from os.path import join
from glob import glob


def main():
    dir_x20 = "/home/jupyter-sb4476/projects/sbCRISPRSCREEN/02.reads_20nt/"
    files_x20 = glob(join(dir_x20, 'SRR*_20nt.fasta'))
    print(files_x20)

if __name__ == '__main__':
    main()
