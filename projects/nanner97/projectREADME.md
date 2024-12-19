### This is the readme for my project!!

From Conrad _et al._ 2017, "The Short Isoform of BRD4 Promotes HIV-1 Latency by Engaging Repressive SWI/SNF Chromatin-Remodeling Complexes," doi 10.1016/j.molcel.2017.07.025

ATAC-seq data from Illumina HiSeq 2500

SRR5720369 & SRR5720371 = DMSO  
SRR5720370 & SRR5720372 = JQ1

JQ1 is a bromodomain inhibitor with modest latency reversal capacity, BUT even at these sub-optimal doses it can still increase chromatin accessibility at the 5' LTR of HIV-1

*The aim of this project* is to determine if our anti-HIV guide RNAs overlap with regions of openness after stimulation with JQ1

nf-core atac-seq pipeline found at https://nf-co.re/atacseq/2.1.2/

**To download:**
```bash
fasterq-dump -p SRR*.fastq
```

**To zip:**
```bash
zip SRR*\_x.fastq
```
will output a fastq.gz with the same file name

|file                  |format |type |num_seqs     |sum_len         |min_len |avg_len |max_len |
|----------------------|-------|-----|-------------|----------------|--------|--------|--------|
|SRR5720369_1.fastq.gz | FASTQ | DNA | 70,327,765  | 7,032,776,500  | 100    | 100    | 100    |
|SRR5720369_2.fastq.gz | FASTQ | DNA | 70,327,765  | 7,032,776,500  | 100    | 100    | 100    |
|SRR5720370_1.fastq.gz | FASTQ | DNA | 100,789,168 | 10,078,916,800 | 100    | 100    | 100    |
|SRR5720370_2.fastq.gz | FASTQ | DNA | 100,789,168 | 10,078,916,800 | 100    | 100    | 100    |
|SRR5720371_1.fastq.gz | FASTQ | DNA | 42,187,695  | 4,260,957,195  | 101    | 101    | 101    |
|SRR5720371_2.fastq.gz | FASTQ | DNA | 42,187,695  | 4,260,957,195  | 101    | 101    | 101    |
|SRR5720372_1.fastq.gz | FASTQ | DNA | 48,634,901  | 4,912,125,001  | 101    | 101    | 101    |
|SRR5720372_2.fastq.gz | FASTQ | DNA | 48,634,901  | 4,912,125,001  | 101    | 101    | 101    |

**Docker image**
I am running this pipeline on my own Ubuntu setup on my home computer which has 32GB RAM and a 12-core CPU
Therefore I had to install Nextflow via curl according to the documentation
To load in nf-core I set up a docker container and added it to my bashrc

```bash
docker run -itv `pwd`:`pwd` -w `pwd` -u $(id -u):$(id -g) -e $HOME=/tmp nfcore/tools
```

Setting HOME was required for the proper permissions to run the container

**Subsampling**
```bash
seqkit head -n 20000000 SRR*\_x.fastq
```
will sub-sample each to the first 20 million reads

**Makefile creation**  
With Dr. Klopfenstein and Chelsea's help I created a Makefile with the following contents:

```bash
## this is my project makefile

REF_DIR := ~/OMICSProject/genomes
REF_FA := ~/OMICSProject/genomes/Jlat106_GRCH38.fa.gz #from class pc
REF_GFF := ~/OMICSProject/genomes/Jlat106.gff #from class pc
DATA_DIR := ~/OMICSProject/project
OUT_DIR := ~/OMICSProject/project/output
REF_BED := ~/OMICSProject/genomes/Jlat106.bed
PROJ_CSV := ~/OMICSProject/project/atac.csv
MACS := 3100000000
READ := 100

test:
        ~/nextflow

run_updated:
        ~/nextflow run \
                nf-core/atacseq \
                --input ~/OMICSProject/project/atac.csv \
                --outdir ~/OMICSProject/project/output \
                --fasta $(REF_FA) \
                --gff $(REF_GFF) \
                --bed $(REF_BED) \
                --read_length 100 \
                --with_control \
                --max_cpus 11 \
                --max_memory 31.GB \
                -profile docker \
                --macs_gsize 3100000000 \
                -with-trace \
                -with-report \
                -resume

run_resume:
        ~/nextflow run \
```

The makefile allows me to customize the reference genome and other parameters

Then I ran the pipeline
```bash
make run_updated
```
**Running the pipeline**  
Immediately I ran into errors with SRR5720369 because for some reason it had non-English characters -- threw errors in macs2 and picard that it was unable to be read, so ultimately I just got rid of it

The other samples ran fine until it was time for deepTools to run; it was unable to read the .tss.bed file that was generated from the Jlat genome
To solve this I just copied and pasted the contents of the reference bed file and that seemed to solve the error

**gRNAs**  
To be able to align the gRNAs to the resulting peaks, I created a bed file that specified where each gRNA sits on the HIV-1 provirus

**Getting results**  
The pipeline puts out bigwig files which can be visualized in IGV
At the 5' end, the gRNAs do indeed overlap regions of increased accessibility: [5'](http://10.248.148.22/hub/user-redirect/lab/tree/share/jj993/OMICS_project/five%20prime2.png) which supports our "Tickle & Tweeze" strategy

The 3' end does not align very well, but does so upstream: [3'](http://10.248.148.22/hub/user-redirect/lab/tree/share/jj993/OMICS_project/three%20prime2.png) [upstream](http://10.248.148.22/hub/user-redirect/lab/tree/share/jj993/OMICS_project/upstream.png)
I believe this is because our genome is based on J-Lat 10.6, but the study uses J-Lat A2 which does not contain the full-length provirus

**Future directions**  
- Align gRNAs to peaks created with other LRAs
- Try to correct .tss.bed reading issue --> need to look into deepTools and see if this can be specified anywhere
