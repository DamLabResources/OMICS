# Week 6: Notes
 
### Learning Objectives


##### - Understand the Burroughs-Wheeler Alignment (BWA) algorithm and its applications.
##### - Differentiate between BWA and other alignment algorithms (like BLAST).
##### - Understand why we should not put large result-files into git repos.
##### - Understand the purpose of generating alignment indexes.
##### - Use samtools to view and count the number of aligned reads.
##### - Use samtools flagstat to summarize an alignment result.
##### - Understand the important fields of a SAM format.








### Assignment


Create a `excercise/{user}/wk06/README.md`.
Use this to keep track of your commands and present your results.
Use the read files in `~/share/OMICS/wk06/reads`.

 - Sub-sample the first 100K from each set into a new file in your working directory. Remember to keep track of sample names and R1/R2s.
 - Use `bwa mem` to align these reads to the SGD genome.
 - Use `samtools view` to determine how many reads aligned from each sample at a Q30 threshold. Create a table in your README describing this.
 - Use `samtools depth` and determine the average depth across each chromosome in each sample. 
 - After alignment, sorting, and indexing, download them to your own computer and load them into IGV.
 - Use the IGV browser, find a region where there seems to be a amino-acid change between the three samples. Take a screenshot and add it to the Readme.
 - Do a brief search about the protein, is anything known? Write about it in the README.

#### Sub-sample the first 100K from each set into a new file in your working directory. Remember to keep track of sample names and R1/R2s.

1. I copied the data from the shared/OMICS/wk06/reads directory into my home directory. 
    `jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06/wk06_hw$ cp ~/share/OMICS/wk06/reads/* .`
    
2. then I took the first 100K of each by doing the following commands: 


      `seqkit head -n 100000 OGstrain_R1.fq.gz -o OGstrain_R1_100k.fq.gz`
      
      `seqkit head -n 100000 OGstrain_R2.fq.gz -o OGstrain_R2_100k.fq.gz`
      
      `seqkit head -n 100000 SF_aer_R1.fq.gz -o SF_aer_R1_100k.fq.gz` 
      
      `seqkit head -n 100000 SF_aer_R2.fq.gz -o SF_aer_R2_100k.fq.gz` 
      
      `seqkit head -n 100000 SF_ann_R2.fq.gz -o SF_ann_R2_100k.fq.gz` 
      
      `seqkit head -n 100000 SF_ann_R1.fq.gz -o SF_ann_R1_100k.fq.gz`

#### Use `bwa mem` to align these reads to the SGD genome.

3. Then I used the piped code to complete the alignment: 


   `bwa mem refs/saccharomyces_cerevisiae.fa reads/OGstrain_R1_100k.fq.gz reads/OGstrain_R2_100k.fq.gz | samtools sort > alns/OGStrain100k.pipe.sorted.bam`
   
   `bwa mem refs/saccharomyces_cerevisiae.fa reads/SF_aer_R2_100k.fq.gz reads/SF_aer_R1_100k.fq.gz | samtools sort > alns/SF_aer_100k.pipe.sorted.bam`
   
   `bwa mem refs/saccharomyces_cerevisiae.fa reads/SF_ann_R2_100k.fq.gz reads/SF_ann_R1_100k.fq.gz | samtools sort > alns/SF_ann_100k.pipe.sorted.bam`
   
#### Use `samtools view` to determine how many reads aligned from each sample at a Q30 threshold. Create a table in your README describing this.   
   
   
