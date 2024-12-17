# Long Read Alignment

## seqkit stats summary of data:
|file |                              format | type | num_seqs | sum_len | min_len | avg_len | max_len|
|----|---------------------------------------|-----|----------|---------|--------|----------|-------|
d|ata/reads/T78276-MFG.small.fq.gz | FASTQ   |DNA |       500 | 861,404 |   1,000  |1,722.8 |   4,875|
|data/reads/T78276-SPL.small.fq.gz  |FASTQ  | DNA  |      500|  785,129  |  1,001 | 1,570.3  |  7,393|

## use minimap2 to align the reads from samples to K03455 genome

minimap2 -ax map-ont ./data/ref/K03455.fasta ./data/reads/T78276-MFG.small.fq.gz> ./data/align/T78276-MFG.sam

## use samtools to convert to sorted bam file with an index
samtools view -b ./data/align/T78276-MFG.sam > ./data/align/T78276-MFG.bam
samtools sort ./data/align/T78276-MFG.bam > ./data/align/T78276-MFG_sorted.bam
samtools index ./data/align/T78276-MFG_sorted.bam

## count the number of aligned records that map to the genome with MAPQ>20

| MFG | SPL |
|----|------|
| 853 | 580 |

## view in IVG
