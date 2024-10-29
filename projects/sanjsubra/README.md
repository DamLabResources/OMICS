# Project Ideas 

### 1. Analyzing RNA sequencing data from neuron-glia co-cultures cultivated from mouse hippocampus/cortex.
#### - Cultures are cultivated from WT animals or transgenic animals with a constitutive global knockin mutation affecting GluN2B C-terminus at E1479 or S1480. 
#### - Based on our previous work, the cultures cultivated from transgenic animals are hypothesized to influentially alter NMDAR sublocalization (synaptic vs extrasynaptic).
#### - Based on the specific mutation, we hypothesize that we will observe upregulation of synaptically-linked pathways with the E1479Q mutation, and extrasynaptically-linked pathwaus with the S1480E mutation.


# Introduction

# Literature Review

# Methodology

# Results

# Discussion

# Conclusion

# References


## Workflow

##### Packing up files 
 - I have 6 .fastq files: SRR...71_1, 71_2, 73_1, 73_2, 77_1, 77_2 
 
 - I used the following commands to compress the fastq files:
$ seqkit seq ~/share/ss5393/SRR23169371_1.fastq -o ~/share/ss5393/SRR23169371_1.fastq.gz
$ seqkit seq ~/share/ss5393/SRR23169371_2.fastq -o ~/share/ss5393/SRR23169371_2.fastq.gz
$ seqkit seq ~/share/ss5393/SRR23169373_1.fastq -o ~/share/ss5393/SRR23169373_1.fastq.gz
$ seqkit seq ~/share/ss5393/SRR23169373_2.fastq -o ~/share/ss5393/SRR23169373_2.fastq.gz
$ seqkit seq ~/share/ss5393/SRR23169377_1.fastq -o ~/share/ss5393/SRR23169377_1.fastq.gz
$ seqkit seq ~/share/ss5393/SRR23169377_2.fastq -o ~/share/ss5393/SRR23169377_2.fastq.gz

- I confirmed that the fastq.gz files were compressed before deleting the larger fastq files: 

$ du -h ~/share/ss5393/*

7.4G    /home/jupyter-ss5393/share/ss5393/SRR23169371_1.fastq
1.2G    /home/jupyter-ss5393/share/ss5393/SRR23169371_1.fastq.gz
7.4G    /home/jupyter-ss5393/share/ss5393/SRR23169371_2.fastq
1.3G    /home/jupyter-ss5393/share/ss5393/SRR23169371_2.fastq.gz
5.9G    /home/jupyter-ss5393/share/ss5393/SRR23169373_1.fastq
916M    /home/jupyter-ss5393/share/ss5393/SRR23169373_1.fastq.gz
5.9G    /home/jupyter-ss5393/share/ss5393/SRR23169373_2.fastq
1015M   /home/jupyter-ss5393/share/ss5393/SRR23169373_2.fastq.gz
4.8G    /home/jupyter-ss5393/share/ss5393/SRR23169377_1.fastq
736M    /home/jupyter-ss5393/share/ss5393/SRR23169377_1.fastq.gz
4.8G    /home/jupyter-ss5393/share/ss5393/SRR23169377_2.fastq
788M    /home/jupyter-ss5393/share/ss5393/SRR23169377_2.fastq.gz


- Aligning reads
$ bwa mem refs/Mus_musculus.GRCm39.dna_sm.primary_assembly.fa.gz reads/SRR23169371_1.fastq.gz reads/SRR23169371_2.fastq.gz  > aligns/het.sam
$ bwa mem refs/Mus_musculus.GRCm39.dna_sm.primary_assembly.fa.gz reads/SRR23169373_1.fastq.gz reads/SRR23169373_2.fastq.gz  > aligns/mut.sam
$ bwa mem refs/Mus_musculus.GRCm39.dna_sm.primary_assembly.fa.gz reads/SRR23169377_1.fastq.gz reads/SRR23169377_2.fastq.gz > aligns/wt.sam

