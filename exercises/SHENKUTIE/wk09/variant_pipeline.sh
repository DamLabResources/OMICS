#!/bin/bash

# Script for aligning and variant calling yeast sequence data
# variant_call path/to/sample.sorted.bam path/to/variants.bcf

# Define some constants
FILTER='DP>=10&&QUAL>20'

# Useful to full paths in scripts so they run anywhere.
REF=/data/share/refs/SGD/saccharomyces_cerevisiae.fa


(bcftools mpileup -Ou -f $REF $1 |
  bcftools call -m |         
  bcftools filter -Ob -i $FILTER > $2)
