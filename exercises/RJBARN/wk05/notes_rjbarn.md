# use seqkit to get stats for the multiplex.fq file:
seqkit stats ../data/multiplexed.fq -T -a > muxed.stats.tsv

# Demultiplex the samples:
I did this by making a intermediate files that selected for sequences that started with 'ACCT' and 'CTGC'. 
seqkit grep -s -p "^ACCT" data/multiplexed.fq -r > solution/ACCT.fastq
seqkit grep -s -p "^CTGC" data/multiplexed.fq -r > solution/CTGC.fastq

I then demultiplexed the data by selecting for the correct end barcode based on the sequence name:
seqkit grep -s -p "CCAG$" solution/ACCT.fastq -r > solution/SRR23803536.fastq
seqkit grep -s -p "TCAG$" solution/ACCT.fastq -r > solution/SRR23803537.fastq
seqkit grep -s -p "CCAG$" solution/CTGC.fastq -r > solution/SRR23803538.fastq
seqkit grep -s -p "TCAG$" solution/CTGC.fastq -r > solution/SRR23803539.fastq


# quick approx.. of number of sequences in each: 
grep '^@' solution/SRR23803539.fastq | wc -l

Or to look at the total in all four files:
grep '^@' solution/SRR2380353*.fastq | wc -l      #ignore_italics*


# Remove the barcodes: 
This starts at line 2 and removes the first and last four from the sequence. It repeats this every 4th line. Then it does the same for the quality check lines starting at 0 and every 4th line. 

awk 'NR % 4 == 2 {seq = substr($0, 5, length($0) - 8); print seq} 
     NR % 4 == 0 {print substr($0, 5, length($0) - 8)} 
     NR % 4  != 2 && NR % 4 != 0' solution/SRR23803536.fastq > solution/SRR23803536.trimmed.fastq

awk 'NR % 4 == 2 {seq = substr($0, 5, length($0) - 8); print seq} 
     NR % 4 == 0 {print substr($0, 5, length($0) - 8)} 
     NR % 4  != 2 && NR % 4 != 0' solution/SRR23803537.fastq > solution/SRR23803537.trimmed.fastq

awk 'NR % 4 == 2 {seq = substr($0, 5, length($0) - 8); print seq} 
     NR % 4 == 0 {print substr($0, 5, length($0) - 8)} 
     NR % 4  != 2 && NR % 4 != 0' solution/SRR23803538.fastq > solution/SRR23803538.trimmed.fastq

awk 'NR % 4 == 2 {seq = substr($0, 5, length($0) - 8); print seq} 
     NR % 4 == 0 {print substr($0, 5, length($0) - 8)} 
     NR % 4  != 2 && NR % 4 != 0' solution/SRR23803539.fastq > solution/SRR23803539.trimmed.fastq


# Save as gzip file:
seqkit seq -o solution/SRR23803536.trimmed.fastq.gz solution/SRR23803536.trimmed.fastq
seqkit seq -o solution/SRR23803537.trimmed.fastq.gz solution/SRR23803537.trimmed.fastq
seqkit seq -o solution/SRR23803538.trimmed.fastq.gz solution/SRR23803538.trimmed.fastq
seqkit seq -o solution/SRR23803539.trimmed.fastq.gz solution/SRR23803539.trimmed.fastq

# seqkit stats summary of the data:
seqkit stats solution/SRR2380353* -T -a > solution/demuxed.stats.tsv   #ignore_italics*


# stat summary table
|file                              | format | type | num_seqs | sum_len  | min_len | avg_len | max_len |
|----------------------------------|--------|------|----------|----------|---------|---------|---------|
|solution/SRR23803536.fastq        | FASTQ  | DNA  |   1234   | 163200   | 43      | 132.3   | 159     |
|solution/SRR23803536.trimmed.fastq|     FASTQ|   DNA|     1234|    153328|  35|      124.3|   151|
|solution/SRR23803536.trimmed.fastq.gz|   FASTQ|   DNA|     1234|    153328|  35|      124.3|   151|
|solution/SRR23803537.fastq|              FASTQ|   DNA|     567|     87433|   43|      154.2|   159|
|solution/SRR23803537.trimmed.fastq|      FASTQ|  DNA |    567|     82897|   35|      146.2 |  151|
|solution/SRR23803537.trimmed.fastq.gz|   FASTQ|   DNA|     567|     82897|   35|      146.2|   151|
|solution/SRR23803538.fastq|              FASTQ|   DNA|     89|      12751|   72|      143.3|   159|
|solution/SRR23803538.trimmed.fastq|      FASTQ|   DNA|     89|      12039|   64|      135.3|   151|
|solution/SRR23803538.trimmed.fastq.gz|   FASTQ|   DNA|     89|      12039|   64|      135.3|   151|
|solution/SRR23803539.fastq|              FASTQ|   DNA|     10|      1403|    104|     140.3|   159|
|solution/SRR23803539.trimmed.fastq|      FASTQ|   DNA|     10|      1323|    96|      132.3|   151|
|solution/SRR23803539.trimmed.fastq.gz|   FASTQ|   DNA|     10|      1323|    96|      132.3|   151|

# Reflection paragraph:
Are there an equal number of reads from each sample?
Are the read lengths the same between each sample?

From the stat summary, it appears that there are a lot more reads for SRR23803536 compared to the other samples. SRR23803538 and SRR23803539 both have a pretty low number of reads. However, the read lengths according to the average length appear to be similar with some variation ranging from 124 to 154. The max read length are a lot closer in range (151 to 159). The min length found in the reads has quite a bit of variation (35 to 104). 
