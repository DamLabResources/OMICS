## Snow Flake Yeast Alignment
Nontokozo Mdluli 09/28/24 week06 

# Sub-sample the first 100K reads from each file 
I copied Snow Flake Yeast reads to my working directory.I then sub-sampled the first 100K reads from each set of sequences into a new reads file in my working directory using the `seqkit head` command. I also checked that 100K reads were filtered using the `seqkit stat` command.

```bash
cp ~/share/OMICS/wk06/reads/SF_aer_R1.fq.gz ~/share/nvm35/OMICS/wk06_HW/reads/ 

seqkit head -n 100000 SF_aer_R1.fq.gz > SF_aer_R1_100K.fq
seqkit stat SF_aer_R1_100K.fq
seqkit head -n 100000 SF_aer_R2.fq.gz > SF_aer_R2_100K.fq
seqkit head -n 100000 SF_ann_R1.fq.gz > SF_ann_R1_100K.fq
seqkit head -n 100000 SF_ann_R2.fq.gz > SF_ann_R2_100K.fq
```
# Align the Reads to the SGD Genome, convert to bam, and sort
To start, I indexed the reference genome. I then used `bwa mem` to align these reads to the SGD genome.

```bash
bwa index refs/saccharomyces_cerevisiae.fa
bwa mem refs/saccharomyces_cerevisiae.fa reads/SF_aer_R1_100K.fq reads/SF_aer_R2_100K.fq |samtools sort > alignments/SF_aer.bam
bwa mem refs/saccharomyces_cerevisiae.fa reads/SF_ann_R1_100K.fq reads/SF_ann_R2_100K.fq |samtools sort > alignments/SF_ann.bam
```

# Index bam files
Once aligned and sorted, the SF specific bam files were indexed to get bam.bai files

```bash
samtools index SF_aer.bam 
samtools index SF_ann.bam 
```

# The number of reads that aligned at Q30 threshold for each sample
Using `samtools view` I determined how many reads aligned from each sample at a Q30 threshold. 

```bash
samtools view -q 30 -c alignments/SF_aer.bam
samtools view -q 30 -c alignments/SF_ann.bam
```

|Sample Name|Number of Aligned Reads (Q30)|
|:---------:|:---------------------------:|
|SF_aer     |185,103                      |
|SF_ann     |184,978                      |

# The average depth across each chromosome in each sample

```bash
samtools depth alignments/SF_ann.bam | awk '{sum[$1] += $3; count[$1]++} END {for (chr in sum) {print chr, sum[chr] / count[chr]}}' 
samtools depth alignments/SF_aer.bam | awk '{sum[$1] += $3; count[$1]++} END {for (chr in sum) {print chr, sum[chr] / count[chr]}}' 
```
|           |SF Aerobic   |SF Anaerobic|
|:---------:|:-----------:|:----------:|
|Chromosome |Avg Depth    |Avg Depth   |
|chrI       |3.67         |2.97        |
|chrII      |2.83         |2.82        |
|chrIII     |3.19         |2.90        |
|chrIV      |2.60         |2.78        |
|chrV       |3.00         |3.04        |
|chrVI      |3.68         |3.38        |
|chrVII     |3.28         |2.76        |
|chrVIII    |2.90         |3.30        |
|chrIX      |3.47         |3.40        |
|chrX       |2.80         |2.94        |
|chrXI      |2.91         |2.87        |
|chrXII     |3.04         |3.42        |
|chrXIII    |2.75         |2.77        |
|chrXIV     |2.84         |3.28        |
|chrXV      |2.78         |2.87        |
|chrXVI     |2.76         |2.81        |
|chrmt      |14.69        |23.70       |

# Identified amino acid change and protein information
Using the sorted bam and bam.bai files for each SF sample and the saccharomyces_cerevisiae: genome, genome index, annotations - the SF samples were aligned against the reference genome on IGV. The following mutation was identified in chrXVI:475,551-478,857.

![Amino_acid_change](NMdluli/wk06/IGVmutations.png)

It appears that there may be some missense mutations in the translation elongation factor 1 subunit beta (chr1, 143,100 bp) in both the SF aerobic sample and the SF anaerobic sample. Some of the mutations are unique and some appear to be shared - but for the unique mutations, it's challenging to say if they are for certain unique since this region has poor coverage. Translation elongation factor 1 subunit beta is known to play a role in stimulating nucleotide exchange between tRNAs. Mutations in this gene would affect protein translation. 
 
