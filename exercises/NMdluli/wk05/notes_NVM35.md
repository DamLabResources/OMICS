## Demultiplex Samples: Notes on solutions 
Nontokozo Mdluli 09/24/24


# Multiplexed data statistics

To get basic statistics about the multiplexed FASTQ file, I used the following command:

```bash
seqkit stats data/multiplexed.fq 
```
The results showed that the multiplexed data has 1,900 reads. The results were stored in a tabular file muxed.stats.tsv

```bash
seqkit stats data/multiplexed.fq > muxed.stats.tsv
```

# Demultiplex the samples
To demultiplex the samples by forward and reverse barcodes, I used seqkit grep with intermediate steps. To start, I extracted reads with the forward barcode anywhere in the reads. I then filtered reads starting with ACCT from this file. I then reversed the reads and filtered reversed reads starting with the reverse barcode. After completing this filter, I then reversed reads back to original.
Using seqkit grep -h, I was able to grep using the following arguments:
-o solution/sample.fq specifies output file where reads will be saved.

-s searches specified pattern within the sequence of each read

-p 'ACCT' specifies the barcode to search for in the sequence

For the first two samples:

```bash
seqkit grep -o solution/forwardreads.fq -s -p 'ACCT' data/multiplexed.fq
seqkit grep -s -r -p ^ACCT -o solution/startfw.fq solution/forwardreads.fq  
seqkit seq -r -o solution/reversed_reads.fq solution/startfw.fq
seqkit grep -s -r -p ^GACC -o solution/SRR23803536r.fq solution/reversed_reads.fq
seqkit seq -r -o solution/SRR23803536.fq solution/SRR23803536r.fq 
seqkit grep -s -r -p ^GACT -o solution/SRR23803537r.fq solution/reversed_reads.fq 
seqkit seq -r -o solution/SRR23803537.fq solution/SRR23803537r.fq 
```
For the last two samples:

```bash
seqkit grep -o solution/forwardreads2.fq -s -p 'CTGC' data/multiplexed.fq
seqkit grep -s -r -p ^CTGC -o solution/startfw2.fq solution/forwardreads2.fq  
seqkit seq -r -o solution/reversed_reads2.fq solution/startfw2.fq 
seqkit grep -s -r -p ^GACC -o solution/SRR23803538r.fq solution/reversed_reads2.fq 
seqkit seq -r -o solution/SRR23803538.fq solution/SRR23803538r.fq 
seqkit grep -s -r -p ^GACT -o solution/SRR23803539r.fq solution/reversed_reads2.fq 
seqkit seq -r -o solution/SRR23803539.fq solution/SRR23803539r.fq 
```

# Trim the barcodes
I began by trimming the ends of my reads such that the trimmed reads begin at the fifth base and end on the fifth last base. This was done for each sample. 

```bash
seqkit subseq -r 5:-5 -o solution/trimmed_SRR23803536.fq solution/SRR23803536.fq
seqkit subseq -r 5:-5 -o solution/trimmed_SRR23803537.fq solution/SRR23803537.fq
seqkit subseq -r 5:-5 -o solution/trimmed_SRR23803538.fq solution/SRR23803538.fq
seqkit subseq -r 5:-5 -o solution/trimmed_SRR23803539.fq solution/SRR23803539.fq
```    
I then used gzip to zip and compress the trimmed files

```bash
gzip -c solution/trimmed_SRR23803536.fq > solution/SRR23803536.trimmed.fastq.gz
gzip -c solution/trimmed_SRR23803537.fq > solution/SRR23803537.trimmed.fastq.gz
gzip -c solution/trimmed_SRR23803538.fq > solution/SRR23803538.trimmed.fastq.gz
gzip -c solution/trimmed_SRR23803539.fq > solution/SRR23803539.trimmed.fastq.gz
```

## Demux statistics
Using seqkit stats, I generated stats for the trimmed and compressed data. This was piped to the tsv demultiplexed stat file.

```bash
seqkit stats solution/SRR23803536.trimmed.fastq.gz solution/SRR23803537.trimmed.fastq.gz solution/SRR23803538.trimmed.fastq.gz solution/SRR23803539.trimmed.fastq.gz > demuxed.stats.tsv
```
The resulting table was as follows:

|file                                   |format  |type | num_seqs |sum_len   |min_len  |avg_len  |max_len   |
|:-------------------------------------:|:------:|:---:|:--------:|:--------:|:-------:|:-------:|:--------:|
|solution/SRR23803536.trimmed.fastq.gz  |FASTQ   |DNA  |1,234     |153,328   |35       |124.3    |151       |
|solution/SRR23803537.trimmed.fastq.gz  |FASTQ   |DNA  |567       |82,897    |35       |146.2    |151       |
|solution/SRR23803538.trimmed.fastq.gz  |FASTQ   |DNA  |89        |12,039    |64       |135.3    |151       |
|solution/SRR23803538.trimmed.fastq.gz  |FASTQ   |DNA  |10        |1,323     |96       |132.3    |151       |

The the individual number of reads per sample are added together, they total 1,900 reads corresponding the multiplexed samples.
The results show that sample SRR23803536 has the highest number of reads and has the highest sum length of reads. It appears that read lengths in sample SRR23803537 are on average longer than the other samples. Reads with the shortest lengths were primarily found on samples SRR23803536 and SRR23803537. Overall, all samples had a similar max read length.    

## Reflection Questions
 - Are there an equal number of reads from each sample?
 - Are the read lengths the same between each sample?
The sample SRR23803536 has the highest number of reads, which corresponds to the highest sum lengths between the reads. The sample with the lowest number of reads also has the lowest sum lengths between the reads. 

