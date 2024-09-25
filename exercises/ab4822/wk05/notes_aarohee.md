## Week 05 solution notes

##commands used
- navigating to repository 
	cd path to the folder
	cd repos/OMICS-2024-/content/wk05/solution/
	touch notes_aarohee.md
	vim notes_aarohee.md


##Fastq statistics using seqkit

##commands used
 
seqkit stats  data/multiplexed.fq

- The output showed 1900 reads before demultiplexing.

#for demultiplexing

mkdir -p solution
seqkit grep -r -s -p 'ACCT' multiplexed.fq | seqkit grep -r -s -p 'CCAG' > solution/SRR23803536.fastq
seqkit grep -r -s -p 'ACCT' multiplexed.fq | seqkit grep -r -s -p 'TCAG' > solution/SRR23803537.fastq
seqkit grep -r -s -p 'CTGC' multiplexed.fq | seqkit grep -r -s -p 'CCAG' > solution/SRR23803538.fastq
seqkit grep -r -s -p 'ACCT' multiplexed.fq | seqkit grep -r -s -p 'TCAG' > solution/SRR23803539.fastq


# -r enables regular expression mode, allows for more flexible matching
# -s search is case sensitive
# -p '....' is looking for pattern of sequence

Then the output from first seqkit grep command is piped into another seqkit grep command.

The output is redirected to a file name ".....fastq" in solution directory

###Trim the barcodes
For each sample ID, replace the forward and reverse code with "" and pipe, and store it on a different name.

seqkit replace -p '^ACCT' -r '' solution/SRR23803536.fastq | \
seqkit replace -p 'CCAG$' -r '' | \
seqkit seq -g | gzip > solution/SRR23803536.trimmed.fastq.gz

#Demux stats

seqkit stats solution/SRR23803536.fastq solution/SRR23803537.fastq solution/SRR23803538.fastq solution/SRR23803539.fastq > solution/demuxed.stats.tsv

seqkit stats solution/SRR23803536.trimmed.fastq.gz solution/SRR23803537.trimmed.fastq.gz solution/SRR23803538.trimmed.fastq.gz solution/SRR23803539.trimmed.fastq.gz >> solution/demuxed.stats.tsv

did the same for trimmed and concatenated and checked stats

cat solution/demuxed.stats.tsv

RESULTSSS

file                        format  type  num_seqs  sum_len  min_len  avg_len  max_len
solution/SRR23803536.fastq  FASTQ   DNA      1,595  218,687       43    137.1      159
solution/SRR23803537.fastq  FASTQ   DNA      1,328  191,361       43    144.1      159
solution/SRR23803538.fastq  FASTQ   DNA        882  125,097       51    141.8      159
solution/SRR23803539.fastq  FASTQ   DNA      1,328  191,361       43    144.1      159
file                                   format  type  num_seqs  sum_len  min_len  avg_len  max_len
solution/SRR23803536.trimmed.fastq.gz  FASTQ   DNA      1,595  218,687       43    137.1      159
solution/SRR23803537.trimmed.fastq.gz  FASTQ   DNA      1,328  191,361       43    144.1      159
solution/SRR23803538.trimmed.fastq.gz  FASTQ   DNA        882  125,097       51    141.8      159
solution/SRR23803539.trimmed.fastq.gz  FASTQ   DNA      1,328  191,361       43    144.1      159

From what we found, there is some variability in the number of reads across samples. Two of the samples had the exact same read count. The read lengths are similar, with all samples exihibiting a mininum of 43 bases. The maximum length across all samples as well is consistent at 159 bases. The minimum, average, and maximum read lengths for each sample remain consistent between the demultiplexed and trimmed files.


