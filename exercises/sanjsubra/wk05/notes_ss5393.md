Sanjita Subramanian

# Mux statistics
-----------------

$ seqkit stats data/multiplexed.fq

| file | format | type | num_seqs | sum_len | min_len | avg_len | max_len |
| --- | --- | --- | --- | --- | --- | --- | --- | 
| data/multiplexed.fq | FASTQ | DNA | 1,900 | 264,787 | 43 | 139.4 | 159 |

## Demultiplex the samples
---------------------------

### SRR23803536 and SRR23803537
---------------------------------
- These barcodes have the same 5' barcode 'ACCT'. 
- So first I used:

$ seqkit grep -R 1:4 -p 'ACCT' data/multiplexed.fq | seqkit stats

- This allowed me to search the data for 'ACCT' specifically in the first four residues (as my 5' primer).

| file | format | type | num_seqs | sum_len | min_len | avg_len | max_len |
| --- | --- | --- | --- | --- | --- | --- | --- | 
| data/multiplexed.fq | FASTQ | DNA | 1,801 | 250,633 | 43 | 139.2 | 159 |

- This told me that out of 1900 reads, 1801 have ACCT on the 5' end.

#### How I moved the reads into solution/SRR2380536:
- SRR2380536 3' barcode is 'CCAG', so I added to the previous command:

$ seqkit grep -R 1:4 -p 'ACCT' data/multiplexed.fq | seqkit grep -R -4:-1 -p 'CCAG' | seqkit stats

- To allow me to search within the 1801 reads for sequences with 'CCAG' in the last four residues (i.e. on the 3' end). 

| file | format | type | num_seqs | sum_len | min_len | avg_len | max_len |
| --- | --- | --- | --- | --- | --- | --- | --- | 
| data/multiplexed.fq | FASTQ | DNA | 1,234 | 163,200 | 43 | 132.3 | 159 |

- Then, I copied these reads into a new file:

$ seqkit grep -R 1:4 -p 'ACCT' data/multiplexed.fq | seqkit grep -R -4:-1 -p 'CCAG' > solution/SRR23803536.fastq

#### How I moved the reads into solution/SRR23803537
-----------------
- I followed the same strategy as for SRR23803536, but replaced 'CCAG' with 'TCAG':

$ seqkit grep -R 1:4 -p 'ACCT' data/multiplexed.fq | seqkit grep -R -4:-1 -p 'TCAG' | seqkit stats

| file | format | type | num_seqs | sum_len | min_len | avg_len | max_len |
| --- | --- | --- | --- | --- | --- | --- | --- | 
| data/multiplexed.fq | FASTQ | DNA | 567 | 87,433 | 43 | 154.2 | 159 |

- Then, I copied these reads into a new file:

$ seqkit grep -R 1:4 -p 'ACCT' data/multiplexed.fq | seqkit grep -R -4:-1 -p 'TCAG' > solution/SRR23803537.fastq

#### How I moved the reads into solution/SRR2380537:
----------------------------
$ seqkit grep -s -p 'ACCT''TCAG' data/multiplexed.fq > solution/SRR23803537.fastq

### SRR23803538 and SRR23803539
---------------------------------
- I employed the same strategy as above for demuxing the reads for the last two barcode pairs.

$ seqkit grep -R 1:4 -p 'CTGC' data/multiplexed.fq | seqkit stats

| file | format | type | num_seqs | sum_len | min_len | avg_len | max_len |
| --- | --- | --- | --- | --- | --- | --- | --- | 
| data/multiplexed.fq | FASTQ | DNA | 99 | 14,154  | 72 | 143 | 159 |

#### How I moved the reads into solution/SRR2380538:
----------------------------
$ seqkit grep -R 1:4 -p 'CTGC' data/multiplexed.fq | seqkit grep -R -4:-1 -p 'CCAG' | seqkit stats

$ seqkit grep -R 1:4 -p 'CTGC' data/multiplexed.fq | seqkit grep -R -4:-1 -p 'CCAG' > solution/SRR23803538.fastq

#### How I moved the reads into solution/SRR2380539:
-----------------
$ seqkit grep -R 1:4 -p 'CTGC' data/multiplexed.fq | seqkit grep -R -4:-1 -p 'TCAG' | seqkit stats

$ seqkit grep -R 1:4 -p 'CTGC' data/multiplexed.fq | seqkit grep -R -4:-1 -p 'TCAG' > solution/SRR23803539.fastq

## Trim the barcodes
---------------------------

- Demuxed files 
- I used the seqkit amplicon flags to isolate regions between the appropriate forward primers (ACCT or CTGC) and the complement of the reverse primers (5') (CTGG or CTGA) only on the positive strands
- I trimmed the primers by only taking the sequence starting and ending where the primers end/begin (-r 5:-5)
- I used -o to save trimmed sequences in the .gz format
- I only knew I was on the right track (at least I thought I was) by looking at the seqkit stats tables after every set of commands
 
### SRR23803536 
---------------------------------

$  seqkit amplicon -F ACCT -R CTGG -r 5:-5 -P solution/SRR23803536.fastq | seqkit stats

$  seqkit amplicon -F ACCT -R CTGG -r 5:-5 -P solution/SRR23803536.fastq -o solution/SRR23803536.trimmed.fastq.gz

- Check:
$ seqkit stats solution/SRR23803536.trimmed.fastq.gz

### SRR23803537 
---------------------------------

$ seqkit amplicon -F ACCT -R CTGA -r 5:-5 -P solution/SRR23803537.fastq | seqkit stats

$ seqkit amplicon -F ACCT -R CTGA -r 5:-5 -P solution/SRR23803537.fastq -o solution/SRR23803537.trimmed.fastq.gz

- Check:
$ seqkit stats solution/SRR23803537.trimmed.fastq.gz

### SRR23803538 
---------------------------------

$ seqkit amplicon -F CTGC -R CTGG -r 5:-5 -P solution/SRR23803538.fastq | seqkit stats

$ seqkit amplicon -F CTGC -R CTGG -r 5:-5 -P solution/SRR23803538.fastq -o solution/SRR23803538.trimmed.fastq.gz

- Check:
$ seqkit stats solution/SRR23803538.trimmed.fastq.gz

### SRR23803539
---------------------------------

$ seqkit amplicon -F CTGC -R CTGA -r 5:-5 -P solution/SRR23803539.fastq | seqkit stats

$ seqkit amplicon -F CTGC -R CTGA -r 5:-5 solution/SRR23803539.fastq -o solution/SRR23803539.trimmed.fastq.gz

- Check:
$ seqkit stats solution/SRR23803539.trimmed.fastq.gz 

## Demux statistics
---------------------------

| file | format | type | num_seqs | sum_len | min_len | avg_len | max_len |
| --- | --- | --- | --- | --- | --- | --- | --- | 
| solution/SRR23803536.fastq | FASTQ | DNA | 1,234 | 163,200 | 43 | 132.3 | 159 |
| solution/SRR23803536.trimmed.fastq.gz | FASTQ | DNA | 1,234 | 153,328 | 35 | 124.3 | 151 |
| solution/SRR23803537.fastq | FASTQ | DNA | 567 | 87,433 | 43 | 154.2 | 159 |
| solution/SRR23803537.trimmed.fastq.gz | FASTQ | DNA | 567 | 82,897 | 35 | 146.2 | 151 |
| solution/SRR23803538.fastq | FASTQ | DNA | 89 | 12,751  | 72 | 143.3 | 159 |
| solution/SRR23803538.trimmed.fastq.gz | FASTQ | DNA | 89 | 12,039  | 64 | 135.3 | 151 |
| solution/SRR23803539.fastq | FASTQ | DNA | 10 | 1,403  | 104 | 140.3 | 159 |
| solution/SRR23803539.trimmed.fastq.gz | FASTQ | DNA | 10 | 1,323  | 96 | 132.3 | 151 |

## Reflection Questions
---------------------------

My results indicate that there are not an equal number of reads from each sample. Samples SRR23803536 had the greatest number of reads (1234) while SRR23803539 had the fewest number of reads (10). Due to the discrepancy in sequence number between samples, the sum length of reads also differed. The difference in values for minimum length and average length of sequence were comparatively smaller. Notably, maximum length values did not change between samples. Comparing sequence reads and maximum length values between demuxed and trimmed files (per sample) thus supported that I was on the right path with the commands I chose. For example, seqkit amplicon command worked clearly when I added the -P flag, preventing extraction of irrelevant sequences recognized by the primers. 