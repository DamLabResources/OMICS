```bash
cd ~/repos/OMICS/content/wk05/solution/
vim notes_VRuszin.md
cd ~/repos/OMICS/content/wk05/data
```

# Stats:
# seqkit stats multiplexed.fq
    file            format  type  num_seqs  sum_len  min_len  avg_len  max_len
    multiplexed.fq  FASTQ   DNA      1,900  264,787       43    139.4      159   
    The # reads is 1,900

# Create fastq files for each sample:
```bash
seqkit grep -s -r -i -p ^ACCT multiplexed.fq | seqkit grep -s -r -i -p CCAG$ -o solution/SRR23803536.fastq
```
(done for the other 3 as well)
- -s = search subseq on seq, both positive and negative strand are searched
- -r = patterns are regular expression
- -i = ignore case
- -p = search pattern

# Converted to fasta:
```bash
seqkit fq2fa solution/SRR23803536.fastq -o solution/SRR23803536.fasta
```

# Trimming barcodes off:
```bash
seqkit replace -s -r -i -p "^ACCT" -r "" solution/SRR23803536.fasta | seqkit replace -s -r -i -p "CCAG$" -r "" > solution/SRR23803536.trimmed.fastq.gz
```
(done for the other 3 as well)

# Statistics:
```bash
seqkit stats *.fasta *.fastq *.fastq.gz > demuxed.stats.tsv
```
	file                          format  type  num_seqs  sum_len  min_len  avg_len  max_len
1	SRR23803536.fasta             FASTA   DNA      1,234  163,200       43    132.3      159
2	SRR23803537.fasta             FASTA   DNA        567   87,433       43    154.2      159
3	SRR23803538.fasta             FASTA   DNA         89   12,751       72    143.3      159
4	SRR23803539.fasta             FASTA   DNA         10    1,403      104    140.3      159
5	SRR23803536.fastq             FASTQ   DNA      1,234  163,200       43    132.3      159
6	SRR23803537.fastq             FASTQ   DNA        567   87,433       43    154.2      159
7	SRR23803538.fastq             FASTQ   DNA         89   12,751       72    143.3      159
8	SRR23803539.fastq             FASTQ   DNA         10    1,403      104    140.3      159
9	SRR23803536.trimmed.fastq.gz  FASTA   DNA      1,234  153,328       35    124.3      151
10	SRR23803537.trimmed.fastq.gz  FASTA   DNA        567   82,897       35    146.2      151
11	SRR23803538.trimmed.fastq.gz  FASTA   DNA         89   12,039       64    135.3      151
12	SRR23803539.trimmed.fastq.gz  FASTA   DNA         10    1,323       96    132.3      151

# Questions:
Are there an equal number of reads from each sample?
No, there were not an equal number of reads from each sample.

Are the read lengths the same between each sample?
No, the read lengths were not the same between each sample.
