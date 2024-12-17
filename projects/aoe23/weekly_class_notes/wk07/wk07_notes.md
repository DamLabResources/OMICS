# Week_07

## we are going to use this folder to specifically practice with long reads

jupyter-aoe23@Mistake-Not:~$ cd share/OMICS/wk07/
jupyter-aoe23@Mistake-Not:~/share/OMICS/wk07$ tree
.
├── reads
│   ├── T78276-MFG.small.fq.gz
│   └── T78276-SPL.small.fq.gz
└── refs
    └── K03455.fasta

2 directories, 3 files

### Lecture assingment 
   
   
   
   ## 1. Copy the reads and reference files to a working directory in your home.

go to home directory and make a folder for wk07
note home directory = ~/omics_aoe23

jupyter-aoe23@Mistake-Not:~/omics_aoe23$ mkdir wk07

then copy everything from Dr. Dampier's week 7 folder 


jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk07$ cp -r ~/share/OMICS/wk07/reads/ reads/
jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk07$ cp -r ~/share/OMICS/wk07/refs/ refs/ 



jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk07$ seqkit stats reads/*
file                          format  type  num_seqs  sum_len  min_len  avg_len  max_len
reads/T78276-MFG.small.fq.gz  FASTQ   DNA        500  861,404    1,000  1,722.8    4,875
reads/T78276-SPL.small.fq.gz  FASTQ   DNA        500  785,129    1,001  1,570.3    7,393

  ## 2. Use minimap2 to align the reads from each sample to the K03455 genome.

### for the first read: 


using minimap2, command is -ax sr (include the reference sequence) (and then the read and then) > name of new sam file that we want !!


jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk07$ minimap2 -ax sr refs/K03455.fasta reads/T78276-MFG.small.fq.gz > MFG.sam


### repeat for second read

jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk07$ minimap2 -ax sr refs/K03455.fasta reads/T78276-SPL.small.fq.gz > SPL.sam

   ## 3. Use samtools to convert to a sorted bam file with an index.
   
   
### MAKE A BAM FILE for each 
   
   
jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk07$ sam tools sort MFG.sam > MFG.sorted.bam

jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk07$ sam tools sort SPL.sam > SPL.sorted.bam


### INDEX EACH!! 

jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk07$ samtools index MFG.sorted.bam


jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk07$ samtools index SPL.sorted.bam


   ## 4. Count the number of aligned records that map to the genome with at least a MAPQ>20.
   
   
   











NOTE!! Make sure that the header works for this!!!!!
   
