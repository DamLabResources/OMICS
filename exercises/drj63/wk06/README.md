# Week 06 Assignment: Exploring capabilities of SAMtools and BWA alignment tools

## Overview
The goal of this assignment is to gain insight to some functionality of the seqkit and samtools utilities and understand how these tools can be applied to create a sequence alignment for bioinformatics analyses.

## Commands used

`seqkit head -n 100000 ~/share/OMICS/wk06/reads/OGstrain_R*.fq.gz > res/wk06/OGstrain_R*_100k.fq.gz`

Purpose: use seqkit toolset to create .fq.gz file subset of first 100k reads in R1 and R2 directions for use in subsequent analyses

`bwa mem ~/OMICS/wk06/refs/saccharomyces_cerevisiae.fa res/wk06/OGstrain_R1_100k.fq.gz res/wk06/OGstrain_R2_100k.fq.gz > res/wk06/OGstrain_100k_aln.sam`

Purpose: create a BWA sequence alignment of the 100k read subset to the saccharomyces_cerevisiae genome FASTA file

`samtools view -b res/wk06/OGstrain_100k_aln.sam | samtools sort > res/wk06/OGstrain_100k_aln_sort.bam`

Purpose: create .bam file based on R1 & R2 OGstrain files and pipe to samtools sort command to created sorted BAM file and store in resources (res) file

`samtools view -c -q 30 res/wk06/OGstrain_100k_aln.bam`

Purpose: Determine number of reads in sequence alignment that have a quality threshold of at least 30

`samtools coverage res/wk06/OGstrain_100k_aln_sort.bam > wk06/OGstrain_100k_coverage.tsv`

Purpose: Determine depth of coverage of the alignment and store in .tsv file

## Results

**Samtools Depth results:**

|Total aligned reads | Q30 reads |
| :---: | :---: |
| 201343 | 182307 |

**Samtool Coverage results:**

| Chr # | Avg Depth |
| :---: | :---:|
| chrI | 2.25518 |
| chrII | 	2.00101|
| chrIII | 2.29566 |
| chrIV | 1.84287 |
| chrV | 2.13249 |
| chrVI | 2.40131 |
| chrVII | 1.91178 |
| chrVIII | 2.09369 |
| chrIX | 2.14843 |
| chrX | 2.06919 |
| chrXI | 2.1039 |
| chrXII | 2.90062 |
| chrXIII | 1.94711 |
| chrXIV | 2.08138 |
| chrXV | 1.92412 |
| chrXIV | 1.92884 |

**IGV view of alignment**


