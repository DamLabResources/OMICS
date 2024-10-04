Wk05 Assignment

1. Created `notes_ceg327.md` file with ` vim 'notes_ceg327.md'`
2. Used command `seqkit stats multiplexed.fq` to get stats on data.
There are 1900 reads or `num_seqs' prior to demultiplexing data.

3. Used command `head sample_sheet.csv` and `tail sample_sheet.csv` to determine barcodes: 
`sample_name,forward,reverse
SRR23803536,ACCT,CCAG
SRR23803537,ACCT,TCAG
SRR23803538,CTGC,CCAG
SRR23803539,CTGC,TCAG`

4. After multiple unsuccessful attempts and consulting ChatGPT, I consulted Shirley and Joanna and they helped me figure out the right code as follows:
`seqkit grep -r -s  -p 'ACCT,CCAG' multiplexed.fq > SRR23803536.fastq'
'seqkit grep -r -s  -p 'ACCT,TCAG' multiplexed.fq > SRR23803537.fastq'
'eqkit grep -r -s  -p 'CTCG,CCAG' multiplexed.fq > SRR23803538.fastq'
'seqkit grep -r -s  -p 'CTCG,TCAG' multiplexed.fq > SRR23803539.fastq`

5. Consulted ChatGPT and used the following commands to trim the 5' and 3' barcodes from each sequence and zipped the files:
`seqkit subseq -r 5:-5 SRR23803536.fastq -o SRR23803536.trimmed.fastq
seqkit subseq -r 5:-5 SRR23803537.fastq -o SRR23803537.trimmed.fastq
seqkit subseq -r 5:-5 SRR23803538.fastq -o SRR23803538.trimmed.fastq
seqkit subseq -r 5:-5 SRR23803539.fastq -o SRR23803539.trimmed.fastq`
followed by
`seqkit subseq -r 5:-5 SRR23803536.fastq -o SRR23803536.trimmed.fastq.zg
seqkit subseq -r 5:-5 SRR23803537.fastq -o SRR23803537.trimmed.fastq.zg
seqkit subseq -r 5:-5 SRR23803538.fastq -o SRR23803538.trimmed.fastq.gz
seqkit subseq -r 5:-5 SRR23803539.fastq -o SRR23803539.trimmed.fastq.gz`
