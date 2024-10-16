# This README is notes for HW Assignments Only
README path: repos/OMICS/projects/scbarrera


# Week 05:
### Working Directory & Dataset Directory: projects/sbOMICS_HW/wk05


### Get stats on multiplexed files:
- Filename: muxed.stats.tsv
- Command:  
`jupyter-sb4476@Mistake-Not:~/projects/sbOMICS_HW/wk05$ 
seqkit stats data/multiplexed.* -T > muxed.stats.tsv`


- The # of reads is 1900

|file                      |format  |type    |num_seqs |sum_len |min_len |avg_len |max_len|
|--------------------------|--------|--------|---------|--------|--------|--------|-------|
|data/multiplexed.fq       |FASTQ   |DNA     |1900     |264787  |43      |139.4   |159    | 
|data/multiplexed.short.fa |FASTA   |DNA     |10       |1380    |66      |138.0   |159    |



### Demultiplex Samples
- Break up each read based on its barcode in sample_sheet.csv file
- I first pulled out the sequences that had the 5' barcode --> then piped that into a command that pulled out the 3' barcode from that set of sequences--> then wrote those results into a new fastq file with the sample name.
- Command:  
`seqkit grep -r -s -i -p ^ACCT data/multiplexed.fq |seqkit grep -r -s -i -p CCAG$ -o SRR23803536.fastq`  
`seqkit grep -r -s -i -p ^ACCT data/multiplexed.fq |seqkit grep -r -s -i -p TCAG$ -o SRR23803537.fastq`  
`seqkit grep -r -s -i -p ^CTGC data/multiplexed.fq |seqkit grep -r -s -i -p CCAG$ -o SRR23803538.fastq`  
`seqkit grep -r -s -i -p ^CTGC data/multiplexed.fq |seqkit grep -r -s -i -p TCAG$ -o SRR23803539.fastq`  


- -r = patterns are regular expression
- -s = search subseq on seq, both positive and negative strand are searched
- -p = search pattern (this should be before the barcode bc its the pattern I am looking for) 
- -i = ignore case
- ^ = start
- $ = end
- -o = outfile


- Check file with `seqkit head SRR23803536.fastq`


### Trim off the barcodes
- I first converted the fastq files into fasta files so that seqkit could read it:  
`seqkit fq2fa SRR23803536.fastq -o SRR23803536.fasta`  
`seqkit fq2fa SRR23803537.fastq -o SRR23803537.fasta`  
`seqkit fq2fa SRR23803538.fastq -o SRR23803538.fasta`  
`seqkit fq2fa SRR23803539.fastq -o SRR23803539.fasta`  

- Check file with `seqkit head SRR23803536.fasta`

- To trim the barcodes off I first used `seqkit amplicon` and it was trimming too much off so I skipped to seqkit replace since that worked for my classmates. (Will have to revisit seqkit amplicon.) Using seqkit replace it replaced the barcode with nothing so it removed barcode>
- This didn't work: `seqkit amplicon -F ACCT -R CCAG -r 5:-5 SRR23803536.fasta > SRR23803536.trimmed.fastq.gz`

- This command worked:  
`seqkit replace -s -p ^ACCT -r "" SRR23803536.fasta | seqkit replace -s -p CCAG$ -r "" -o SRR23803536.trimmed.fastq.gz`  
`seqkit replace -s -p ^ACCT -r "" SRR23803537.fasta | seqkit replace -s -p TCAG$ -r "" -o SRR23803537.trimmed.fastq.gz`  
`seqkit replace -s -p ^CTGC -r "" SRR23803538.fasta | seqkit replace -s -p CCAG$ -r "" -o SRR23803538.trimmed.fastq.gz`  
`seqkit replace -s -p ^CTGC -r "" SRR23803539.fasta | seqkit replace -s -p TCAG$ -r "" -o SRR23803539.trimmed.fastq.gz`  

### Statistics on all data
- Utilized seqkit stats again on all file types and wrote it to a .tsv file  
`seqkit stats -T *.fasta *.fastq *.fastq.gz > demuxed.stats.tsv`

- Results:
|file                          |format  |type  |num_seqs|sum_len |min_len|avg_len | max_len|
|------------------------------|--------|------|--------|--------|-------|--------|--------|
|SRR23803536.fasta             |FASTA   |DNA   |1,234   |163,200 |43     |132.3   |159     |
|SRR23803537.fasta             |FASTA   |DNA   | 567    |87,433  |43     |154.2   |159     |
|SRR23803538.fasta             |FASTA   |DNA   |  89    |12,751  |72     |143.3   |159     |
|SRR23803539.fasta             |FASTA   |DNA   |  10    | 1,403  |104    |140.3   |159     |
|SRR23803536.fastq             |FASTQ   |DNA   |1,234   |163,200 |43     |132.3   |159     |
|SRR23803537.fastq             |FASTQ   |DNA   | 567    |87,433  |43     |154.2   |159     |
|SRR23803538.fastq             |FASTQ   |DNA   |  89    |12,751  |72     |143.3   |159     |
|SRR23803539.fastq             |FASTQ   |DNA   |  10    | 1,403  |104    |140.3   |159     |
|SRR23803536.trimmed.fastq.gz  |FASTA   |DNA   |1,234   |153,328 |35     |124.3   |151     |
|SRR23803537.trimmed.fastq.gz  |FASTA   |DNA   | 567    |82,897  |35     |146.2   |151     |
|SRR23803538.trimmed.fastq.gz  |FASTA   |DNA   |  89    |12,039  |64     |135.3   |151     |
|SRR23803539.trimmed.fastq.gz  |FASTA   |DNA   |  10    | 1,323  |96     |132.3   |151     |

- The files ranged in the amount for each sample. They ranged from 10 sequences with the barcodes of interest to 1,234 sequences. Sample SRR23803536. In the trimmed files there is a decrease in bases (sum_len) as expected since the barcodes were trimmed off. The shortest length ranges from 35 to 96 and the max lenth is 151 for the trimmed files.

### Reflection Questions
- Are there an equal number of reads from each sample?
    - No there are not an equal number of reads for each sample.
 - Are the read lengths the same between each sample?
     - The read lengths also range between samples.
 

### Compress files not using
Compressed files in ~/projects/sbCRISPRSCREEN/reads via command:  
`gzip SRR25648800_LRA.fastq SRR25648801_DMSO.fastq SRR25648808_LRA.fastq SRR25648809_DMSO.fastq`

- Check the `du -h` to check how much of the drive is being used to make sure files zipped.
- Delete unzipped files to make space if they weren't already.  
  
    
-------------------------------------------------------------------------------------------------------
  
# Week 06:
### Working Directory: projects/sbOMICS_HW/wk06
### Data files directory: share/OMICS/wk06/reads

### Sub-sample the first 100K from each set
- I head the first 100000 reads from the fq (zipped) files and wrote that to a new .fq file for each sample  
`seqkit head -n 100000 ~/share/OMICS/wk06/reads/OGstrain_R1.fq.gz > ~/projects/sbOMICS_HW/wk06/OGstrain_R1.100k.fq`  

`seqkit head -n 100000 ~/share/OMICS/wk06/reads/OGstrain_R2.fq.gz > ~/projects/sbOMICS_HW/wk06/OGstrain_R2.100k.fq`  

`seqkit head -n 100000 ~/share/OMICS/wk06/reads/SF_aer_R1.fq.gz > ~/projects/sbOMICS_HW/wk06/SF_aer_R1.100k.fq`  

`seqkit head -n 100000 ~/share/OMICS/wk06/reads/SF_aer_R2.fq.gz > ~/projects/sbOMICS_HW/wk06/SF_aer_R2.100k.fq`  

`seqkit head -n 100000 ~/share/OMICS/wk06/reads/SF_ann_R1.fq.gz > ~/projects/sbOMICS_HW/wk06/SF_ann_R1.100k.fq`  

`seqkit head -n 100000 ~/share/OMICS/wk06/reads/SF_ann_R2.fq.gz > ~/projects/sbOMICS_HW/wk06/SF_ann_R2.100k.fq`  

- Check files with `seqkit head filename'


### Indexing: Align reads to SGD genome via 'bwa mem'
- SGD genome located in : share/refs/SGD
- Indexing: There are two alignment tools installed on this server.
     - `bwa` - designed for aligning short, nearly exact, reads
     - `minimap2` - designed for aligning long (possibly noisy) reads
     
- First: must index the reference genome via `bwa index`:  
`jupyter-sb4476@Mistake-Not:~/projects/sbOMICS_HW/wk06$ 
bwa index refs/saccharomyces_cerevisiae.fa`
- This will create files within the same folder as the reference file

- To create a fa.fai file for the reference to use in IGV can use samtools. Tehnicially don't need this:  
`samtools faidx refs/saccharomyces_cerevisiae.fa`

- Second: utilize `bwa mem` and create a new SAM file (sequence alignment mapping file) 
- The first file is ref then the 2nd, 3rd one is aligning to it - did this for all 3 sets of samples:  

`bwa mem refs/saccharomyces_cerevisiae.fa reads/OGstrain_R1.100k.fq reads/OGstrain_R2.100k.fq > alns/OGstrain.sam`  

`bwa mem refs/saccharomyces_cerevisiae.fa reads/SF_aer_R1.100k.fq reads/SF_aer_R2.100k.fq > alns/SF_aer.sam`  

`bwa mem refs/saccharomyces_cerevisiae.fa reads/SF_ann_R1.100k.fq reads/SF_ann_R2.100k.fq > alns/SF_ann.sam`  

- Look at SAM flag explanation by Broad Institute: https://broadinstitute.github.io/picard/explain-flags.html

### Indexing contd.: Convert sam file to bam file
- Utilized samtools to view sam file into bam file- did this for all 3:  
`samtools view -b alns/OGstrain.sam > alns/OGstrain.bam`  
`samtools view -b alns/SF_aer.sam > alns/SF_aer.bam`  
`amtools view -b alns/SF_ann.sam > alns/SF_ann.bam'  
- Note: this will always say "no samtools version available"


### Indexing Contd.: Sort bam file
- Utilied samtools sort   
`samtools sort alns/OGstrain.bam > alns/OGstrain.sorted.bam`  
`samtools sort alns/SF_ann.bam > alns/SF_ann.sorted.bam`  
`samtools sort alns/SF_aer.bam > alns/SF_aer.sorted.bam`  

- Look at file on screen
- do this for all 3  
`samtools view alns/OGstrain.sorted.bam | less -S`


### Indexing Contd.: Make bai file by indexing sorted bam file via `samtools index`  
`samtools index alns/OGstrain.sorted.bam`  
`samtools index alns/SF_ann.sorted.bam`  
`samtools index alns/SF_aer.sorted.bam`  


### Determine how many reads aligned from each sample at a Q30 threshold
- This was done via `samtools view` and counting how many had a quality score of 30 in the sorted bam file:   
`samtools view -c -q 30 alns/OGstrain.sorted.bam`  
- Results: 182307 reads had a Q30 threshold ranging in various chromosomes ex. chrI, II, III, IV, etc.

 
### Use `samtools depth` and determine the average depth across each chromosome in each sample. 
- This did not work: samtools depth cnv filename
- Consulting chatgpt:  

`samtools depth -a alns/OGstrain.sorted.bam | awk '{sum[$1]+=$3; count[$1]++} END {for (chr in sum) {print chr, sum[chr]/count[chr]}}' > OGstrain.sorted.depth.md`  

`samtools depth -a alns/SF_aer.sorted.bam | awk '{sum[$1]+=$3; count[$1]++} END {for (chr in sum) {print chr, sum[chr]/count[chr]}}' > SF_aer.sorted.depth.md`  

`samtools depth -a alns/SF_ann.sorted.bam | awk '{sum[$1]+=$3; count[$1]++} END {for (chr in sum) {print chr, sum[chr]/count[chr]}}' > SF_ann.sorted.depth.md`  

- -a = Computes the depth at each position across the genome and ensures even zero coverage positions are included.
- awk '{sum[$1]+=$3; count[$1]++}'= For each chromosome (stored in $1) sum the depths ($3 represents the depth at each position) and count the number of positions.
- END {for (chr in sum) {print chr, sum[chr]/count[chr]}}: After reading all lines, print the chromosome and the average depth (sum of depths divided by the count of positions).


### Load files into IGV
- After alignment, sorting, and indexing, I downloaded the files into my own computer and downloaded IGV from https://igv.org/doc/desktop/ and loaded the files into IGV.
- Downloaded the following files:
    - `saccharomyces_cerevisiae.fa` - The genome.
    - `saccharomyces_cerevisiae.fa.fai` - An index of the genome.
    - `saccharomyces_cerevisiae.gff` - The genomic annotations.
    - `filename.bam` - The aligned and sorted reads.
    - `filename.bam.bai` - The index for the reads.

#### In IGV:
- Load genome in 
    - Genomes
- Load file from browser shift .fa file + select fai file
    - Make sure to select .fa first
- Add tracks of annotation
    - File
    - Load from file
    - Click on .gff file
- Should now be a blue stuff showing where all the genes and features are
- Zoom in by clicking top and dragging range selecting
- Right click on track-
    - Expanded to expand
    - Compress
- File
- Load from file
- Select .bam and .bam.bai files
- Now can zoom in
    - Grey = identical to reference
    - Colors = diff from reference
- Right click on seq to show bases
- Bottom half is annotation file against reference
- Top part is alignment file against reference
- If click on sequence on bottom half can see annotation info
- Note: IGV will not tell you if its real or not it only visualizes files that it will create


### Find a region where there seems to be a amino-acid change between the three samples. Take a screenshot and add it to the Readme.
- A region where there appears to be a amino acid change between the 3 samples is on Chromosome X: at position 269,616. OGStrain appears to be calling a different base G instead of A. SF_aer appears to have a deletion at this location. SF_ann appears to be the same at this position in comparison to the reference.All 3 are different from each other and the reference genome predicts that this may be a part of a gene that encodes the ARG3 protein. This can also be noted as argF, or ornithine carbamoyltransferase. Ornithine carbamoyltransferase 3B is known to catalyze the biosynthesis of the arginine precursoe citrulline.  

[Click here for IGV Image](http://10.248.148.22/hub/user-redirect/lab/tree/repos/OMICS/projects/scbarrera/IGV%20Screenshot.pdf)

  
--------------------------------------------------------------------------------------

# Week 07 
No addtl HW- just class notes

# Week 08
Work on project files