Wk06 assignment

- seqkit head -n 100000 OGstrain_R1.fq.gz > OGstrain_R1.100K.fq to get a new fastq file with only the first 100K reads ... repeat for R2
- repeat for SF_ann and SF_aer samples
- bwa mem refs/saccharomyces_cerevisiae.fa reads/OGstrain_R1.100K.fq reads/OGstrain_R2.100K.fq | samtools sort > alns/OGstrain100K.sorted.bam to align and generate a sorted bam file
- repeat for SF_ann and SF_aer samples
- samtools index OGstrain100K.sorted.bam to index, which generates a .bam.bai file that we can use in IGV
- repeat for SF_ann and SF_aer samples
- samtools view -q 30 -c OGstrain100K.sorted.bam
- repeat for SF_ann and SF_aer samples

SAMPLE		|	READS ALIGNED  
OG strain	|	182307  
SF ann		|	184978  
SF aer		|	185103  

- samtools coverage OGstrain100K.sorted.bam to generate a table of coverage information -- samtools depth didn't give a valuable output but maybe i just don't know what i'm doing lol

chrname  meandepth  
          OG strain  SF ann  SF aer  
chrI  2.25518  1.75374  2.63285  
chrII	2.00101	2.0314    1.84091  
chrIII	2.29566      2.02336   2.29513  
chrIV	1.84287      1.95468   1.58198  
chrV	2.13249      2.26667   2.05592  
chrVI	2.40131      2.63287   2.48468  
chrVII	1.91178      1.92817   2.49365  
chrVIII	2.09369      2.58202   1.92991  
chrIV	2.14843      2.69938   2.71221  
chrX	2.06919      2.13238   1.82307  
chrXI	2.1039       2.1255    1.98496  
chrXII	2.90062      1.96415   1.871  
chrXIII	1.94711      1.9736    1.76977  
chrXIV	2.08138      2.59888   1.8834  
chrXV	1.92412      2.05429   1.72397  
chrXVI	1.92884      1.95635   1.68853  
chrmt	5.1878       0.692874  6.72008

- after acquiring the bai files, I loaded them into IGV and found this region in chromosome VIII, in the gene YHR071C-A, where there was a differene in all 3 samples: [igv snapshot](http://10.248.148.22/hub/user-redirect/lab/tree/OMICS/wk06/igv_snapshot.png)

This ORF is said to be "dubious" according to the Saccharomyces cerevisiae genome database and is unlikely to code for a functional protein; however, the reading frame also overlaps with that of NOP10, which is responsible for pseudouridylation and processing of 18S pre-rRNA.

Source: https://www.yeastgenome.org/locus/S000007455
