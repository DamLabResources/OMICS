## Notes for Week 5 assignment

seqkit stats multiplexed.fq
num_seqs = 1900


## Generating fastq files

First I used seqkit grep command (with Regan's help) to break multiplexed.fq into 4 separate files:

seqkit grep -s -r -i -p ^ACCT multiplexed.fq | seqkit grep -s -r -i -p CCAG$ -o solution/SRR23803536.fastq
repeat for all samples/barcodes


## Trimming the sequences

To remove the barcodes, first I converted each file to a fasta from a fastq
seqkit fq2fa SRR23803536.fastq > SRR23803536.fasta
repeat for all samples

Then I replaced the barcodes with an empty string
seqkit replace -s -p ^ACCT -r "" SRR23803536.fasta | seqkit replace -s -p CCAG$ -r "" -o SRR23803536.trimmed.fasta
repeat for all samples

Then I moved them each to different folders for organizational purposes :) and zipped them to .gz


## Getting the statistics

To get the statistics for each sample, I used seqkit stats and listed each sample
seqkit stats SRR238035336.trimmed.fasta.gz SRR238035337.trimmed.fasta.gz SRR238035338.trimmed.fasta.gz SRR238035339.trimmed.fasta.gz

file                         | format | type | num_seqs | sum_len | min_len | avg_len | max_len |
-----------------------------|--------|------|----------|---------|---------|---------|---------|
SRR23803536.trimmed.fasta.gz |  FASTA |  DNA |    1,234 | 153,328 |      35 |   124.3 |    151  |
SRR23803537.trimmed.fasta.gz |  FASTA |  DNA |      567 |  82,897 |      35 |   146.2 |    151  |
SRR23803538.trimmed.fasta.gz |  FASTA |  DNA |       89 |  12,039 |      64 |   135.3 |    151  |
SRR23803539.trimmed.fasta.gz |  FASTA |  DNA |       10 |   1,323 |      96 |   132.3 |    151  |


## Summary

The average length of each sample's reads is overall similar across the boar. However, sample "36" has over twice the number of reads as sample "37," but its average length is the lowest. Interestingly, sample "39" has by far the lowest number of reads, but the longest minimum length. I would be interested to see the quality scores of each sample to see if that correlates; I wouldn't be surprised if sample 39 has low quality, leading to fewer reads.