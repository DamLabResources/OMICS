# Week 6 Notes/Commands 


### Types of aligners:

- minimap2 - designed for aligning long (possibly noisy) reads
   - this can look at things tat are zipped
- bwa - designed for aligning short, nearly exact, 
   - cannot look at things that are zipped which is why we need multiple files


### in class assignments/commands
I made a root directory called omics_aoe23 from home and put a folder called week6, and within week 6 i made a directory called 
I am in my project directory for week 6: 

`jupyter-aoe23@Mistake-Not:~$ mkdir omics_aoe23
jupyter-aoe23@Mistake-Not:~$ cd omics_aoe23/
jupyter-aoe23@Mistake-Not:~/omics_aoe23$ mkdir wk06
jupyter-aoe23@Mistake-Not:~/omics_aoe23$ cd wk06/
jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ mkdir refs`

copy everything in this directory: ~/share/refs/SGD/ into the refs/ forlder within my omics_aoe23 directory 


`jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ cp ~/share/refs/SGD/* refs/`
 
 confirm that everything copied over fine:
 
` jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ tree
.
└── refs
    ├── saccharomyces_cerevisiae.fa
    ├── saccharomyces_cerevisiae.fa.fai
    ├── saccharomyces_cerevisiae.fa.gz
    └── saccharomyces_cerevisiae.gff`
    
 What is each file? 
    ├── saccharomyces_cerevisiae.fa (this is the genome for 
    ├── saccharomyces_cerevisiae.fa.fai (this is the genome as an unpacked version)
    ├── saccharomyces_cerevisiae.fa.gz (this is the genome as a packed version)
    └── saccharomyces_cerevisiae.gff (this is a tabular file: that is intended to look at with human eyes: and you can grep and look for specific genes) it is not designed to be interpreted by us but can be given to a computer)
    
What if we want to look at the file and see what is in a file: 
`less -S refs/saccharomyces_cerevisiae.gff `

Note the last column in the tabular sheet that ends with .gff is a messy sequence of notes separated by semicolons and commas which is a tag value pair

## now we need to index with bwa
NOTE: that to find all of the commands bwa- help does not work: 

`jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ bwa -help
[main] unrecognized command '-help'
jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ bwa`

instead bwa alone shown above is the help. 


bwa index gives you: 

jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ bwa index

Usage:   bwa index [options] <in.fasta>

Options: -a STR    BWT construction algorithm: bwtsw, is or rb2 [auto]
         -p STR    prefix of the index [same as fasta name]
         -b INT    block size for the bwtsw algorithm (effective with -a bwtsw) [10000000]
         -6        index files named as <in.fasta>.64.* instead of <in.fasta>.* 

Warning: -a bwtsw' does not work for short genomes, while `-a is' and
         `-a div' do not work not for long genomes.
         
         
         

HOW TO INDEX/READOUT: 

jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ bwa index refs/saccharomyces_cerevisiae.fa
[bwa_index] Pack FASTA... 0.13 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 6.73 seconds elapse.
[bwa_index] Update BWT... 0.06 sec
[bwa_index] Pack forward-only FASTA... 0.04 sec
[bwa_index] Construct SA from BWT and Occ... 3.25 sec
[main] Version: 0.7.17-r1188
[main] CMD: bwa index refs/saccharomyces_cerevisiae.fa
[main] Real time: 10.697 sec; CPU: 10.207 sec


after indexing we now have way more files in the folder, see the new tree for this folder: 

jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ tree
.
└── refs
    ├── saccharomyces_cerevisiae.fa
    ├── saccharomyces_cerevisiae.fa.amb
    ├── saccharomyces_cerevisiae.fa.ann
    ├── saccharomyces_cerevisiae.fa.bwt
    ├── saccharomyces_cerevisiae.fa.fai
    ├── saccharomyces_cerevisiae.fa.gz
    ├── saccharomyces_cerevisiae.fa.pac
    ├── saccharomyces_cerevisiae.fa.sa
    └── saccharomyces_cerevisiae.gff
    
    
to look at the size of everything: 

jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ du -h refs/*


## now need to get some reads after we have done the index 

#### first make a new directory to put the reads into 
We will make directory and copy all of the reads 
jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ mkdir reads

#### then check whats in that reads folder that he wants us to copy from: 

jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ cp ~/share/OMICS/wk06/reads/

jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ cp ~/share/OMICS/wk06/reads/
OGstrain_R1.10K.fq  OGstrain_R1.fq.gz   OGstrain_R2.10K.fq  OGstrain_R2.fq.gz   SF_aer_R1.fq.gz     SF_aer_R2.fq.gz     SF_ann_R1.fq.gz     SF_ann_R2.fq.gz     srr_accessions.txt

#### only want the ones with 10K: use the star to distinctly take these two rather than doing separate steps

jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ cp ~/share/OMICS/wk06/reads/*10K* reads/
jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ tree
.
├── reads
│   ├── OGstrain_R1.10K.fq
│   └── OGstrain_R2.10K.fq
└── refs
    ├── saccharomyces_cerevisiae.fa
    ├── saccharomyces_cerevisiae.fa.amb
    ├── saccharomyces_cerevisiae.fa.ann
    ├── saccharomyces_cerevisiae.fa.bwt
    ├── saccharomyces_cerevisiae.fa.fai
    ├── saccharomyces_cerevisiae.fa.gz
    ├── saccharomyces_cerevisiae.fa.pac
    ├── saccharomyces_cerevisiae.fa.sa
    └── saccharomyces_cerevisiae.gff

2 directories, 11 files

#### want to look at the top of each file to make sure that the header for each matches which is important

`jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ seqkit head -n1 reads/OGstrain_R1.10K.fq `
@SRR28618276.1 NB501145:267:HG22FBGXH:1:11101:13794:1072 length=148
AAAAAGGCTCGACCAAGCTCAACGCGCTGTTGCAAAATGGAAANANTNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGANCNTNCANANTNNNNCTNNTNTTTGGNAGGTGTNTGCTCNNNTCTTCTCTTTCAGTTTGGTGCGCTNNT
+
AAAAAAEEEEEAEEE6EEEE66EEEEEEEEEEEEEEEEEEEEE#E#E##############################EE#E#E#AA#/#E####<E##E#EEEEE#AEEEEE#EEA<A###E<EEEE<<EEAEEEEEEEEEEEAE##E
`jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ seqkit head -n1 reads/OGstrain_R2.10K.fq `
@SRR28618276.1 NB501145:267:HG22FBGXH:1:11101:13794:1072 length=148
ATATACAGTAGGACGACCAATAAATCTGAATAGCGCACCAAACTGAAAGAGAAGANTAGAGCAAACACCTGCNAANGNNNNNNNNNNNNNNNNNNNNNNNNNNNTNNNNNNNNGNNNNANNCNNNNNNTANNNNNNNNNNTNTGNAAN
+
AAAAAEEEEEEEEEEEEEEEEEEEEEEEE6EEEEEEEEEEEEEEEEEEEEEEEEE#EEEEEEEEEE6EEEEA#EE#/###########################/########<####E##<######6A##########/#//#/<#


#### want to then get the stats: to do both at the same time use the star here: 

jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ seqkit stats reads/OGstrain_R*.10K.fq
file                      format  type  num_seqs    sum_len  min_len  avg_len  max_len
reads/OGstrain_R1.10K.fq  FASTQ   DNA     10,000  1,320,136       35      132      149
reads/OGstrain_R2.10K.fq  FASTQ   DNA     10,000  1,325,895       35    132.6      149



## now we want to do somehting with the reads and the index that we have



#### GENERATE A SAM FILE

jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ bwa mem refs/saccharomyces_cerevisiae.fa reads/OGstrain_R1.10K.fq reads/OGstrain_R2.10K.fq 


for the command above: if we just do this, it will spit out a ton of info 

in order to read it we wil use the pipe and do less -S

#### this output is a SAM File: within the sam file:
##### first line says: 

@SQ     SN:chrI LN:230218

@ shows header 
SN: chromosome number 
LN: legnth

##### then you get to a line that reads like this: 
@PG     ID:bwa  PN:bwa  VN:0.7.17-r1188 CL:bwa mem refs/saccharomyces_cerevisiae.fa reads/OGstrain_R1.10K.fq reads/OGstrain_R2.10K.fq

this tells you how many things have been done

###### the rest is a tabular file: i copeid the first two rows below:


SRR28618276.1   83      chrIV   1445535 60      148M    =       1445507 -176    ANNAGCGCACCAAACTGAAAGAGAAGANNNGAGCANACACCTNCCAAANANNAGNNNNANTNTGNANGNTCNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNANTNTTTCCATTTTGCAACAGCGCGTTGAGCTTGGTCGAG>
SRR28618276.1   163     chrIV   1445507 60      75M73S  =       1445535 176     ATATACAGTAGGACGACCAATAAATCTGAATAGCGCACCAAACTGAAAGAGAAGANTAGAGCAAACACCTGCNAANGNNNNNNNNNNNNNNNNNNNNNNNNNNNTNNNNNNNNGNNNNANNCNNNNNNTANNNNNNNNNNT>

column # | Describes (looking at first row)

1        | name of read: (SRR28618276.1)
2        | THIS IS THE SAM FLAG : (83/63) use the link below to understand all of the information that is associated with the number, something that we dont really need to use much 
3        | chromosome it is on: (chrIV)
4        | ? (60)
5        | (148M = 148 bases matched), (75M73S = 75 base pairs matched, and 73 base pairs were clipped or hung off)
6        | ? (=)
7        | ? (144507)
8        | ? (-176)
9        | the letters of the actual read

note this file is sorted by read name: in a specific order in the same order going down




SAM Spec = is a detailed reference that we can find on google to provide more information of how to read this. Can reference this link https://samtools.github.io/hts-specs/SAMv1.pdf

Sam flags: use the link here https://broadinstitute.github.io/picard/explain-flags.html
- this tool is good for explaining your sam flags but not actually something that you look at yourself a lot 


how coudl we loook at all of the reads in chromosome 1?
- the name sorted order is only useful in the beginning 
- rather than reading the entire file we could sort the file based on chromosome number 
- the order should be adjusted into where the chormosomes are....


#### NOW WE DO SORTING


first put the sam file in a specific place: 
`bwa mem ref/saccharomyces_cerevisiae.fa reads/OGstrain_R1.10K.fq reads/OGstrain_R2.10K.fq | tee test.sam`


use this long pipeline to make a sam file, then make a bam file, and then make a sort file 



jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ mkdir alns
jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06$ bwa mem refs/saccharomyces_cerevisiae.fa reads/OGstrain_R1.10K.fq reads/OGstrain_R2.10K.fq | samtools view -b | samtools sort > alns/OGSstrain_pipe.sorted.bam

note that before I made the alns folder these went directly into my directory, and i took the steps to move those back into my alns directory here: 

#### now working in IGV


For this excercise you need to download the following files:

saccharomyces_cerevisiae.fa - The genome.
saccharomyces_cerevisiae.fa.fai - An index of the genome.
saccharomyces_cerevisiae.gff - The genomic annotations.
test.bam - The aligned and sorted reads.
test.bam.bai - The index for the reads.
If you've installed samtools on your computer you could create some of these files locally.



first: download files and put in folder on desktop.


#### load genome
- open igv
- click genomes
- click load genomes from file in the drop down
- load .fa and .fai file at the same time using shift (make sure .fa is first)
 

#### load track 
- file
- load from file 
- select .gff file open 

#### then load the rest of the data

- file 
- load from file
- select .bam and .bam.bai file 
