# Assignment Overview

Using this to keep track of commands and to present the results.

# Using the read files in the ~/share/OMICS/wk06/reads
# Used the four files for aerobic and anaerobic
#mmoved themm to exercise/reads_new

cp share/OMICS/wk06/reads/SF_aer_R1.fq.gz share/ab4822/wk06/exercise/reads_new/
cp share/OMICS/wk06/reads/SF_aer_R2.fq.gz share/ab4822/wk06/exercise/reads_new/
cp share/OMICS/wk06/reads/SF_ann_R1.fq.gz share/ab4822/wk06/exercise/reads_new/
cp share/OMICS/wk06/reads/SF_ann_R1.fq.gz share/ab4822/wk06/exercise/reads_new/


# Sub-sample the first 100K from each set into a new file in your working directory

cd share/ab4822/wk06/exercise/reads_new/
seqkit head -n 100000 SF_aer_R1.fq.gz > SF_aer_R1_subsampled.fq
seqkit head -n 100000 SF_aer_R2.fq.gz > SF_aer_R2_subsampled.fq
seqkit head -n 100000 SF_ann_R1.fq.gz > SF_ann_R1_subsampled.fq
seqkit head -n 100000 SF_ann_R2.fq.gz > SF_ann_R2_subsampled.fq

# Remember to keep track of sample names and R1/R2

## bwa mem is designed for aligning short reads to a reference sequence

refs/saccharomyces_cerevisiae.fa is the reference genome file

reads_new/SF_aer_R1_subsampled.fq: the first input file containing the subsampled reads for the R1 (forward) direction of sequencing. aerobic

reads_new/SF_aer_R2_subsampled.fq: the second input file containing the subsampled reads for the R2 (reverse) direction of sequencing. R1 and R2 files are usually paired-end reads from the same sequencing experiment. aerobic

reads_new/SF_ann_R1_subsampled.fq: another input file containing the subsampled reads for another sample's R1 (forward) direction. anearobic

reads_new/SF_ann_R2_subsampled.fq: the second input file for the additional sample, containing the subsampled reads for R2 (reverse) direction. anearobic


## moved all the files inside refs to references directory inside my home directory

mkdir references
cp ~/share/refs/SGD/* references
du -h references/*
bwa index references/saccharomyces_cerevisiae.fa

bwa mem references/saccharomyces_cerevisiae.fa reads_new/SF_aer_R1_subsampled.fq reads_new/SF_aer_R2_subsampled.fq > alignment/SF_aer_aligned.sam

## For SF_aer
samtools view -q 30 -c alignment/SF_aer_aligned.sam

## storing as a bam file
samtools view -b 30 -c alignment/SF_aer_aligned.sam > alignment/SF_aer_aligned_filtered.bam
samtools view -b 30 -c alignment/SF_ann_aligned.sam > alignment/SF_ann_aligned_filtered.bam

-b : specifies that the output should be in BAM format


## Example Table format for README.md

## Alignment Summary

| Sample       | Total Aligned Reads (Q30) |
|--------------|----------------------------|
| SF_aer      | 185103                          |
| SF_ann      | 184978                          |

# Count reads with Q30 for SF_aer
samtools view -q 30 -c SF_aer_aligned.sam

# Count reads with Q30 for SF_ann
samtools view -q 30 -c SF_ann_aligned.sam

-q : filters the reads based on mapping quality 30 and higher

## Checking

samtools view -H alignment/SF_aer_aligned_filtered.bam
samtools view -H alignment/SF_ann_aligned_filtered.bam
samtools view -c alignment/SF_aer_aligned_filtered.bam
samtools view -c alignment/SF_ann_aligned_filtered.bam

## sorting 

samtools sort alignment/SF_aer_aligned_filtered.bam > alignment/SF_aer_aligned_filtered_sorted.bam
samtools sort alignment/SF_ann_aligned_filtered.bam > alignment/SF_ann_aligned_filtered_sorted.bam

## index 
samtools index alignment/SF_aer_aligned_filtered_sorted.bam
samtools index alignment/SF_ann_aligned_filtered_sorted.bam

## Using samtools depth and determine the average depth across each chromosome in each sample.

samtools depth alignment/SF_ann_aligned_filtered_sorted.bam > alignment/SF_ann_depth.txt

##downloaded files and loaded them to IGV
I uploaded them, but I don't know how to add them to README file













