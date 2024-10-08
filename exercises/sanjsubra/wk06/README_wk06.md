## Wk06 Assignment

#### Subsampling first 100k from read files:
$ seqkit sample -p 0.01 ~/share/OMICS/wk06/reads/SF_aer_R1.fq.gz | seqkit head -n 100000 -o reads/SF_aer_R1_100K.fq

$ seqkit sample -p 0.01 ~/share/OMICS/wk06/reads/SF_aer_R2.fq.gz | seqkit head -n 100000 -o reads/SF_aer_R2_100K.fq

$ seqkit sample -p 0.025 ~/share/OMICS/wk06/reads/SF_ann_R1.fq.gz | seqkit head -n 100000 -o reads/SF_ann_R1_100K.fq

$ seqkit sample -p 0.025 ~/share/OMICS/wk06/reads/SF_ann_R2.fq.gz | seqkit head -n 100000 -o reads/SF_ann_R2_100K.fq

$ seqkit sample -p 0.01 ~/share/OMICS/wk06/reads/OGstrain_R1.fq.gz | seqkit head -n 100000 -o OGstrain__R1_100K.fq

$ seqkit sample -p 0.01 ~/share/OMICS/wk06/reads/OGstrain_R2.fq.gz | seqkit head -n 100000 -o OGstrain__R2_100K.fq

#### Copying SGD files and indexing them:

$ cp ~/share/refs/SGD/saccharomyces_cerevisiae.* refs/

$ bwa index refs/saccharomyces_cerevisiae.fa

#### Using bwa mem to align reads to the SGD genome as .sam file:

$ bwa mem refs/saccharomyces_cerevisiae.fa reads/OGstrain__R1_100K.fq reads/OGstrain__R2_100K.fq > aligns/OGstrain.sam

$ bwa mem refs/saccharomyces_cerevisiae.fa reads/SF_aer_R1_100K.fq reads/SF_aer_R2_100K.fq > aligns/SF_aer.sam

$ bwa mem refs/saccharomyces_cerevisiae.fa reads/SF_ann_R1_100K.fq reads/SF_ann_R2_100K.fq > aligns/SF_ann.sam

#### Generating .bam from .sam:

$ samtools view -b aligns/OGstrain.sam > aligns/OGstrain.bam

$ samtools view -b aligns/SF_aer.sam > aligns/SF_aer.bam

$ samtools view -b aligns/SF_ann.sam > aligns/SF_ann.bam

#### Sorting .bam files:
$ samtools sort aligns/OGstrain.bam > aligns/OGstrain.sorted.bam

$ samtools sort aligns/SF_aer.bam > aligns/SF_aer.sorted.bam

$ samtools sort aligns/SF_ann.bam > aligns/SF_ann.sorted.bam

#### Using samtools view to determine how many reads aligned from each sample at a Q30 threshold.
$ samtools view -c -q 30 aligns/*.sorted.bam 

| Sample | Alignment at Q30 threshold |
| --- | --- |
| OGstrain.sorted.bam | 182096 |
| SF_aer.sorted.bam | 184571 |
| SF_ann.sorted.bam | 185001 |

#### Indexing sorted .bam files:
$ samtools index aligns/OGstrain.sorted.bam

$ samtools index aligns/SF_aer.sorted.bam 

$ samtools index aligns/SF_ann.sorted.bam 

#### Using samtools coverage to determine meandepth across each chromosome in each sample:

$ samtools coverage aligns/OGstrain.sorted.bam

$ samtools coverage aligns/SF_aer.sorted.bam

$ samtools coverage aligns/SF_ann.sorted.bam

| #rname | meandepth OGstrain.sorted.bam | meandepth SF_aer.sorted.bam | meandepth SF_ann.sorted.bam |
| --- | --- | --- | --- |
| chrI | 2.3343 | 2.63763 | 1.86709 |
| chrII | 2.03254 | 1.87435 | 2.05425 |
| chrIII | 2.29822 | 2.26339 | 1.95954 |
| chrIV | 1.82665 | 1.57139 | 1.93461 |
| chrV | 2.18552 | 2.06151 | 2.20837 |
| chrVI | 2.3454 | 2.37856 | 2.60512 |
| chrVII | 1.85548 | 2.41119 | 1.93827 |
| chrVIII | 2.05428 | 1.90581 | 2.63486 |
| chrIX | 2.10686 | 2.78363 | 2.71319 |
| chrX | 2.06054 | 1.86294 | 2.13248 |
| chrXI | 1.98508 | 1.96796 | 2.14146 |
| chrXII | 2.94599 | 1.87532 | 1.98288 |
| chrXIII | 1.93323 | 1.76773 | 1.98073 |
| chrXIV | 2.05384 | 1.89738 | 2.61368 |
| chrXV | 1.9546 | 1.74431 | 2.03191 |
| chrXVI | 1.92267 | 1.71942 | 1.92293 |
| chrmt | 4.89275 | 6.66911 | 0.818592 |



```python

```

![image.png](attachment:8c89c6ef-a1c4-4ac6-928b-f2377b29f2c0.png)

```python

```

![image2.png](attachment:fa1d1052-07e0-48f2-9035-5b6966bf2eae.png)

```python

```
##### Gene: KSS1

##### Protein: mitogen-activated serine/threonine-protein kinase Kss1

- KSS1 encodes a short 368-residue kinase kss1.
- KSS1 is required for pheromone signal transduction in S. cerevisiae.
- Kss1 is expressed in haploids and diploids.
- Kinase activity of Kss1 is required for its role in signal transmission.
- Kss1 is concentrated in the nucleus.

Source:

Ma D, Cook JG, Thorner J. (1995). Phosphorylation and localization of Kssl, a MAP kinase of the Saccharomyces cerevisiae pheromone response pathway. Molecular Biology of the Cell, 6:889-909.