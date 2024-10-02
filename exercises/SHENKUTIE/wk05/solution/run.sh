ln -s ../../../../content/wk05/data/multiplexed.fq
ln -s ../../../../content/wk05/data/sample_sheet.csv 
wc -l sample_sheet.csv 
cat sample_sheet.csv
seqkit stats multiplexed.fq  | tee muxed.stats.tsv 
#sample_name,forward,reverse
#SRR23803536,ACCT,CCAG
#SRR23803537,ACCT,TCAG
#SRR23803538,CTGC,CCAG
#SRR23803539,CTGC,TCAG
# Demultiplexed by barcode
seqkit grep -srip ^ACCT multiplexed.fq |seqkit grep -srip CCAG$ -o SRR23803536.fastq
seqkit grep -srip ^ACCT multiplexed.fq |seqkit grep -srip TCAG$ -o SRR23803537.fastq
seqkit grep -srip ^CTGC multiplexed.fq |seqkit grep -srip CCAG$ -o SRR23803538.fastq
seqkit grep -srip ^CTGC multiplexed.fq |seqkit grep -srip TCAG$ -o SRR23803539.fastq
# Trim barcode
seqkit fq2fa SRR23803536.fastq |seqkit replace -sp ^ACCT -r "" |seqkit replace -sp CCAG$ -r "" -o SRR23803536.trimmed.fastq
seqkit fq2fa SRR23803537.fastq |seqkit replace -sp ^ACCT -r "" |seqkit replace -sp TCAG$ -r "" -o SRR23803537.trimmed.fastq
seqkit fq2fa SRR23803538.fastq |seqkit replace -sp ^CTGC -r "" |seqkit replace -sp CCAG$ -r "" -o SRR23803538.trimmed.fastq
seqkit fq2fa SRR23803539.fastq |seqkit replace -sp ^CTGC -r "" |seqkit replace -sp TCAG$ -r "" -o SRR23803539.trimmed.fastq
# report stats
seqkit stats SRR23803536.trimmed.fastq > demuxed.stats.tsv
seqkit stats SRR23803537.trimmed.fastq >> demuxed.stats.tsv
seqkit stats SRR23803538.trimmed.fastq >> demuxed.stats.tsv
seqkit stats SRR23803539.trimmed.fastq >> demuxed.stats.tsv
