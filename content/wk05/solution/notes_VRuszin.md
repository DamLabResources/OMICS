cd ~/repos/OMICS/content/wk05/solution/
vim notes_VRuszin.md
cd ~/repos/OMICS/content/wk05/data

Stats:
seqkit stats multiplexed.fq
    file            format  type  num_seqs  sum_len  min_len  avg_len  max_len
    multiplexed.fq  FASTQ   DNA      1,900  264,787       43    139.4      159   
    The # reads is 1,900

Create fastq files for each sample:
    seqkit grep -s -r -i -p ^ACCT multiplexed.fq | seqkit grep -s -r -i -p CCAG$ -o solution/SRR23803536.fastq (done for the other 3 as well)
        -s = search subseq on seq, both positive and negative strand are searched
        -r = patterns are regular expression
        -i = ignore case
        -p = search pattern

Converted to fasta:
    seqkit fq2fa solution/SRR23803536.fastq -o solution/SRR23803536.fasta

Trimming barcodes off:
   seqkit replace -s -r -i -p "^ACCT" -r "" solution/SRR23803536.fasta | seqkit replace -s -r -i -p "CCAG$" -r "" > solution/SRR23803536.trimmed.fastq.gz (done for the other 3 as well)

Statistics:
    seqkit stats *.fasta *.fastq *.fastq.gz > demuxed.stats.tsv

Questions:
    Are there an equal number of reads from each sample?
    No, there were not an equal number of reads from each sample.

    Are the read lengths the same between each sample?
    No, the read lengths were not the same between each sample.