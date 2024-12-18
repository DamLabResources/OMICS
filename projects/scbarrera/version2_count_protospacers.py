#!/usr/bin/env python3
"""Count how many times protopacer shows up"""
# print(f'NAME: {__name__}')

__copyright__ = 'Copyright (C) 2024, WND + DVK PhD + SCB. All Right Reserved'
__author__ = 'WND + DVK PhD + SCB'
__license__ = 'GNU AGPL'

from os.path import join
from os.path import basename
from collections import Counter
from glob import glob
from umi_tools import UMIClusterer
from tqdm import tqdm

import argparse


 # Create the argument parser 
def parse_args():
    parser = argparse.ArgumentParser(description="Cluster UMIs using UMIClusterer.")
    parser.add_argument( 'inpath', type=str, help="Path to the file to be processed" ) # Parse the command-line arguments
    parser.add_argument('rawoutpath', type=str, help="Path to write Raw counts result")
    parser.add_argument('clusteredoutpath', type=str, help="Path to write clustered results")
    parser.add_argument('--cluster_method', type=str, default='directional', help="Clustering method to use.")
    parser.add_argument('--mismatch_threshold', type=int, default=2,
                        help="Allowed number of mismatches.")
    parser.add_argument('--max_items', type=int, default=None,
                        help="Max lines to read for testing")

    
    args = parser.parse_args() # Call the processing function with the provided file path 
    
    return args



def main():
    
    
    args = parse_args()
    
    # read the file into a dictionary
    print('Reading file')
    count_dict = read_file(args.inpath, args.max_items)
    
    
    # cluster dictionary
    print('Clustering barcodes')
    clustered_dict = cluster_counts(count_dict, args.cluster_method,
                                   args.mismatch_threshold)
    
    
    print('Writing files')
    # output fixed items and counts
    write_counts(count_dict, args.rawoutpath)
    
    write_counts(clustered_dict, args.clusteredoutpath)

    
def read_file(path, max_items):
    "Read in a path of sequences and return count dictionary"
    
    count_dict = Counter()
    with open(path) as handle:
        for line in tqdm(handle):
            count_dict[bytes(line.strip(), 'ascii')] += 1
            if (max_items is not None) and (len(count_dict) > max_items):
                break
    return count_dict
            

def cluster_counts(count_dict, cluster_method, threshold):
    "Use UMICluster to group related barcodes and return fixed count_dict"
    
    clusterer = UMIClusterer(cluster_method=cluster_method)
    
    
    clustered_umis = clusterer(count_dict,threshold=threshold)
    
    # [['AAA', 'AAT'], ['CCC'], ['GTC', 'GTT']]
    
    fixed_counts = Counter()
    for cluster in clustered_umis:
        # TODO: Maybe select the UMI with the highest count
        # Assume first item is true barcode
        key = cluster[0]
        
        # Sum original counts into a single key
        for item in cluster:
            fixed_counts[key] += count_dict[item]
    
    return fixed_counts

def write_counts(count_dict, path):
    
    #because the dictionary was written as bytes for UMI clusterer, it needs to be written out as text (ascii) 
    with open(path, 'w') as handle:
        items = [(key.decode('ascii'), count) for key, count in count_dict.items()]
        items = sorted(items, key = lambda item: item[1], reverse=True)
        handle.write('key,count\n')
        for key , count in items:
            handle.write(f'{key},{count}\n')
        
                 
    

if __name__ == '__main__':
    main()

# Copyright (C) 2024, WND + DVK PhD + SCB. All Right Reserved
