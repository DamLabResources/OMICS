# Wk06 Assignment: aligning to a genome

## Command to downsample for the first 100k reads (repeat for each of the six samples:
seqkit head -n 100000 ~/share/OMICS/wk06/reads/SF_ann_R2.fq.gz > SF_ann_R2_100k.fq 

## Align to the ref genome, sort and create bam file:
bwa mem refs/saccharomyces_cerevisiae.fa assignment/100k_data/SF_ann_R1_100k.fq assignment/100k_data/SF_ann_R2_100k.fq | samtools view -b | samtools sort > assignment/aligns/SF_ann_100k_pipe.sorted.bam

## Create index file:
samtools index assignment/aligns/SF_ann_100k_pipe.sorted.bam

## Determine how many reads aligned from each sample at a Q30 threshold
samtools view -q 30 -c assignment/aligns/SF_ann_100k_pipe.sorted.bam 

| Sample | reads aligned Q30 |
| --------- | ------------------------- |
| SF_ann_100k | 184978 |
| SF_aer_100k | 185103 |
| OGstrain_100k | 182307 |

## Determine average depth across each chromosome in each sample
samtools depth assignment/aligns/SF_ann_100k_pipe.sorted.bam | awk '{sum[$1] += $3; count[$1]++} END {for (chr in sum) print chr, sum[chr]/count[chr]}' > SF_ann_100k_depth_summary_stats.md 

## Summary of read depth:
|chrom| OG strain | SF_ann|	SF_aer|
|-----|-----------|---------|----------------|
|chrI|	3.32419|	2.96831|	3.66855|
|chrII|	2.79851|	2.82478|	2.82507|
|chrIII|	3.08801|	2.89845|	3.19126|
|chrIV|	2.70478|	2.78312|	2.60359|
|chrIX|	2.94986|	3.40055|	3.47094|
|chrmt|	10.0564|	23.6978|	14.6935|
|chrV|	2.92396|	3.04038|	2.99737|
|chrVI|	3.17634|	3.37869|	3.3676|
|chrVII|	2.72655|	2.76491|	3.28045|
|chrVIII|	2.95757|	3.29766|	2.89715|
|chrX|	2.89173|	2.93878|	2.79502|
|chrXI|	2.83491|	2.87083|	2.90822|
|chrXII|	4.14875|	3.41843|	3.03549|
|chrXIII|	2.77689|	2.77465|	2.7546|
|chrXIV|	2.9069|	3.27894|	2.83804|
|chrXV|	2.76928|	2.86569|	2.7793|
|chrXVI|	2.80833|	2.81457|	2.75876|


## IGV 



![image.png](attachment:cf24f26c-2dee-4efd-818f-c285660e6690.png)![image.png](attachment:c435c3a4-a17a-423e-9a50-2d9affd16d16.png)

```python

```

The above image shows a difference in sequence between the OG strain (G), the SF aer strain (T) and the reference genome (A) in the YARWsigma1 gene at location chrI:182,731. This is a transpsoon-yeast element. This type of element is improtant for gene expansion and genome evelution because it is reinserted into the genome at a new location after having been reverse-transcribed from DNA (https://www.yeastgenome.org/locus/S000006795).
