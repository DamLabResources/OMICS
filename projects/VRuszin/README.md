# Title
```
BCG vaccination stimulates integrated organ immunity by feedback 
of the adaptive immune response to imprint prolonged
innate antiviral resistance
```

# 2024 Nature paper info
```
COL 2        3  4       5 6 7        8  9  10 au[11](authors)
TYP PMID     RP HAMCc   % G YEAR   cit cli ref au[00](authors)
--- -------- -- -----  -- - ----   --- --- -- -----------------
TOP 38036767 R. HA...  -1 i 2024    14  0  75 au[22](Audrey Lee)
```
# Description
For my OMICS project, I will be looking at singe cell RNAseq data obtained from lung ECs and immune cells. This data was used in a paper looking at how BCG vaccination stimulates immunity via helper T cells help to imprint antiviral resistance (1).

# Introduction
# Literature Review
# Methodology
## How I changed my project .fastq files into .fastq.gz files:

```bash
seqkit fq2fa filename.fastq -o solution/filename.fastq.gz
git add
git commit -m ""
git push
pull request
```


What my file size was before: 34.8 GB
What my file size was after: 2 3.9 GB

## What I got from seqkit for project data:
In SRR26186565.fastq.gz, there were 114,895,299 sequences. All sequences were a length of 90. Via seqkit head, the sequences all start an end with something different, so I'm wondering if barcodes were taken off already. 

```bash
seqkit stats SRR26186565.fastq.gz 
file                  format  type     num_seqs         sum_len  min_len  avg_len  max_len
SRR26186565.fastq.gz  FASTA   DNA   114,895,299  10,340,576,910       90       90       90

seqkit head SRR26186565.fastq.gz 
>SRR26186565.1 A00509:671:HNKGVDSX5:3:1101:1506:1000 length=90
AAGCAGTGGTATCAACGCAGAGTACATGGGGAAAGTCGGAGGTTCGAAGACGATCAGATA
CCGTCGTAGTTCCGACCATAAACGATGCCG
>SRR26186565.2 A00509:671:HNKGVDSX5:3:1101:1524:1000 length=90
CGTCTATTTTTATTTCTTCCAAACTACTATTTAGCTTAGAGAGTTAATGATGAGGTGGTG
CTAACAAAGAGAGACTTATACTTAGGGGGG
>SRR26186565.3 A00509:671:HNKGVDSX5:3:1101:2483:1000 length=90
AAGCAGTGGTATCAACGCAGAGTACATGGGGACCCATTTGCTGCTCAAGGCCATGGAACA
TTTTCCTAATCACCAACAGTTACAGAAGAA
>SRR26186565.4 A00509:671:HNKGVDSX5:3:1101:2700:1000 length=90
TTTAGAGTGAAGGACAAATACTCTTGTGGGTTTTGGTTGTCCCTTTTCATTTTTTACCAT
GCTGTATTACTAGATTATACTTTGATAACA
>SRR26186565.5 A00509:671:HNKGVDSX5:3:1101:3152:1000 length=90
TGGGTTCTTGGCTCCAGCTAACTATACAGCAGAGGACTGCCTTATTTGGCATCAATGAGA
GAGGAGGCCCTTGGTCCTGTGGAGGCTTGA
>SRR26186565.6 A00509:671:HNKGVDSX5:3:1101:3314:1000 length=90
GAGAAAACACTCCGTCCCCTATCATTACCAAACAGTAGCTGTGGTATGCACTCATTTCGT
AGGGGCCCTTACTTCTTGGAGGTAGCCTAG
>SRR26186565.7 A00509:671:HNKGVDSX5:3:1101:4056:1000 length=90
CAGGGAAAAGAGGTCGTTAGTGACTTTGACCACTGGTTACATCTACTCTTGCTATCTTTC
CATTATCCTGGTCTGTGCAGAAGTACAGGT
>SRR26186565.8 A00509:671:HNKGVDSX5:3:1101:4381:1000 length=90
CCCCGGGTTTCAACCGCTGTCTAGCATAAATCAGCAGCCAGCGTCGATGCACAGCGCAAT
CCCAGCACTTGGGAGGGAGAGGCAGGGGAA
>SRR26186565.9 A00509:671:HNKGVDSX5:3:1101:4833:1000 length=90
GCACAGTCCGCGGAGCCAAGGCAGAGGAAATTCTGGAGAAAGGCCTGAAGGTGCGGGAGT
ATGAGTTGCGGAAAAATAACTTCTCGGATA
>SRR26186565.10 A00509:671:HNKGVDSX5:3:1101:5448:1000 length=90
TCAGCCTGCCGCTCGGATTGATTATCCGATTCGGTAAATGCCCCCCTCCCACTTCTGTGT
TTGTGTCTTCTTTGTTTCTTTTTTCCCCTT
```

## Finding a pipeline that works for my data
Went to [`nf-core`](https://nf-co.re/) to search for a pipeline. Found one titled 'nf-core/scrnaseq' that may be able to work for my data set.

# Results
# Discussion
# Conclusion
# References
1. Lee, A., Floyd, K., Wu, S. et al. BCG vaccination stimulates integrated organ immunity by feedback of the adaptive immune response to imprint prolonged innate antiviral resistance. Nat Immunol 25, 41–53 (2024). https://doi.org/10.1038/s41590-023-01700-0 

# Data Availability
* [PMID 38036767](https://pubmed.ncbi.nlm.nih.gov/38036767/)
* [Nature](https://www.nature.com/articles/s41590-023-01700-0)
* [GSE244126](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE244126)
### Samples
#### Sample 1) GSM7807682 Lung, D0, rep 1
SRA: SRX21898392    

Run         | # of Spots  | # of Bases | Size  |Published
------------|-------------|------------|-------|----------
SRR26186565 | 114,895,299 | 15.9G      | 4.8Gb |2023-12-04
SRR26186566 | 115,135,212 | 15.9G      | 4.7Gb |2023-12-04

#### Sample 2) GSM7807683 Lung, D21, rep 1
