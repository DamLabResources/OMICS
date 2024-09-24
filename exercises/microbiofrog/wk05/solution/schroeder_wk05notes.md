Here are my notes for my week 5 homework assignment


seqkit stats multiplexed.fq 

|file|format |type  |num_seqs  |sum_len  |min_len  |avg_len  |max_len|
|---|---|---|---|---|---|---|---|
|multiplexed.fq  |FASTQ   |DNA      |1,900  |264,787       |43    |139.4      |159|

There are 1900 reads in the sample based on num_seqs. Since there are sample identifiers that do not follow a specific pattern (most start with @D00468 but some are @ and then a random series of numbers), I needed to grep based on the @. Seqkit grep was behaving weirdly so I used normal grep to verify this and again ended up with 1900 reads.

grep "^@" multiplexed.fq | cut -d ' ' -f1 | sort | uniq | wc -l
1900

I used seqkit's documentation webpage to get the code for demultiplexing, modifying from the example ($ zcat hairpin.fa.gz | seqkit grep -s -r -i -p ^aggcg) by getting rid of the zcat operation and adding a pipe after the first grep to grep both the forward and reverse barcodes as well as adding an -o tag to output it to the file. Here are my commands, used four separate commands (I tried to use chatgpt to do it all in one step but it kept taking me in loops that didn't work so I did each sample separately)

  seqkit grep -s -r -i -p ^ACCT multiplexed.fq | seqkit grep -s -r -i -p CCAG$ -o solution/SRR23803536.fastq
  seqkit grep -s -r -i -p ^ACCT multiplexed.fq | seqkit grep -s -r -i -p TCAG$ -o solution/SRR23803537.fastq
  seqkit grep -s -r -i -p ^CTGC multiplexed.fq | seqkit grep -s -r -i -p CCAG$ -o solution/SRR23803538.fastq
  seqkit grep -s -r -i -p ^CTGC multiplexed.fq | seqkit grep -s -r -i -p TCAG$ -o solution/SRR23803539.fastq
  
Next I removed the barcodes. Seqkit needed the files to be fasta to manipulate them instead of fastq so I changed to fasta before removing the barcodes. To make this code I used the seqkit documentation

  seqkit fq2fa SRR23803536.fastq | seqkit replace -s -p  ^ACCT -r "" | seqkit replace -s -p CCAG$ -r "" -o SRR23803536.trimmed.fasta
  seqkit fq2fa SRR23803537.fastq | seqkit replace -s -p  ^ACCT -r "" | seqkit replace -s -p TCAG$ -r "" -o SRR23803537.trimmed.fasta
  seqkit fq2fa SRR23803538.fastq | seqkit replace -s -p  ^CTGC -r "" | seqkit replace -s -p CCAG$ -r "" -o SRR23803538.trimmed.fasta
  seqkit fq2fa SRR23803539.fastq | seqkit replace -s -p  ^CTGC -r "" | seqkit replace -s -p TCAG$ -r "" -o SRR23803539.trimmed.fasta

However, I kept getting the error "[ERRO] fastx: stdin not detected" when trying to convert the fasta to fastq despite trying for hours and using the documentation website and chat gpt (which just kept taking me in circles) did not help at all. Thus I am leaving the files as .fasta.gz instead of .fastq.gz. I just used gzip to zip all of my files to .fasta.gz from .fasta

Then I got the statistics for all of my samples

seqkit stats SRR23803536.trimmed.fasta.gz SRR23803537.trimmed.fasta.gz SRR23803538.trimmed.fasta.gz SRR23803539.trimmed.fasta.gz > demuxed.stats.tsv

|file                          |format  |type  |num_seqs  |sum_len  |min_len  |avg_len  |max_len|
|---|---|---|---|---|---|---|---|
|SRR23803536.trimmed.fasta.gz  |FASTA   |DNA      |1,234  |153,328       |35    |124.3      |151|
|SRR23803537.trimmed.fasta.gz  |FASTA   |DNA        |567   |82,897       |35    |146.2      |151|
|SRR23803538.trimmed.fasta.gz  |FASTA   |DNA         |89   |12,039       |64    |135.3      |151|
|SRR23803539.trimmed.fasta.gz  |FASTA   |DNA         |10    |1,323       |96    |132.3      |151|


Summary:
I think it is interesting how SRR23803536 has more than 2x more reads than the sample with the next largest number of reads. Despite the number of reads being very different, ranging from 10 to 1234, I think it is interesting how the average read length is about the same across the board, only varying by about 22bp from the smallest to largest average. I wonder if the sample with the largest number of reads was at a higher concentration before sequencing than the sample with the smallest number of reads, or perhaps the quality of the DNA varied a lot between the samples and the lower quality lead to less reads--though then again the one with the smallest number of reads also had the largest minimum read length.


