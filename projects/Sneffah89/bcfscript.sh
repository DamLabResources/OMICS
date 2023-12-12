#!/bin/bash

# Script for calling out the SNPs and Indels in HIV provirus found in the Mid Frontal Gyrus (MFG) and Spleen of HIV infected Individuals
# Inputs added to script file on the terminal include path/to/.bam file and path/to/bcf file name

# Defining some in-script variables
Ref=/home/jupyter-sneffah89/common/references/hg38hxb2f.fasta
chrom=HXB2F

(bcftools mpileup -r $chrom -Ou -f $Ref $1 | bcftools call -m --ploidy 1 -Ob > $2)

