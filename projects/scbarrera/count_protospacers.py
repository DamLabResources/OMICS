#!/usr/bin/env python3
"""Count how many times protopacer shows up"""
# print(f'NAME: {__name__}')

__copyright__ = 'Copyright (C) 2024, DVK PhD and SCB. All Right Reserved'
__author__ = 'DVK PhD and SCB'
__license__ = 'GNU AGPL'

from os.path import join
from os.path import basename
from collections import Counter
from glob import glob
from umi_tools import UMIClusterer


def main():
    """Count how many times protopacer shows up"""
    #glob = get list of file names containing extracted 20nt protospacer  
    x20_pat = "/home/jupyter-sb4476/projects/sbCRISPRSCREEN/02.reads_20nt/SRR*_20nt.fasta"
    # files_x20 = glob(join(x20_pat, 'SRR*_20nt.fasta'))
    files_x20 = glob(x20_pat)
    assert files_x20, f'NO FILES FOUND IN: {x20_pat}'

    #Reading sequences from each file and putting them into dictionary
    # collect all lines from all files
    # fin means files in- defined below
    # the {} is dictionary 	
    name2seqs = {}
    for fin in files_x20:
        seqs = _readseqs(fin)
        print(f'{len(seqs)} READ:', basename(fin))
        name2seqs[fin] = _readseqs(fin)
    assert name2seqs, 'NO LINES/ SEQUENCES FOUND'

    #Count the sequences from each file
    # most_common(#) = print this many on screen
    # threshold=# = the threshold for clustering so 1 will give back all that have appeared 1 time or more
    #name = file being read in that has the extracted 20nt
    #seqs = sequences
    #items = both name and sequence, file is being used as a dictionary key
    clusterer = UMIClusterer(cluster_method="directional")
    for name,seqs in name2seqs.items():
        print(name)
        ctr = Counter(seqs)
        for val, qty in ctr.most_common(5):
            print(f'{qty:6,} {val}', end='')
        seq2count = {s.encode('utf8'):n for s,n in ctr.items()}
        clustered_umis = clusterer(seq2count, threshold=1)
        print(clustered_umis)


# loop variable  = loop fin into read function
def _readseqs(fin):
    """Open file and read each line"""
    with open(fin, encoding='utf8') as ifstream:
        return ifstream.readlines()

if __name__ == '__main__':
    main()

# Copyright (C) 2024, DVK PhD and SCB. All Right Reserved
