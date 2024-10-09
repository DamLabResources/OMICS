# Data Summary for Omics Project 

## Contents of This Data Summary

##### 1. Using Advanced Omics to Support my Thesis Research

##### 2. Data used from *Inosine Induces Stemness Features in CAR T cells and Enhances Potency* (Klysz, et al).

##### 3. Links to Primary Literature:

##### 4. Introduction 

##### 5. Location of Files: 

##### 6. Summary of File Sizes: 

##### 7. Summary of SSR IDs and corresponding samples of interest: 

##### 8. Summary of SSR IDs and corresponding samples of interest: 




***


### Using Advanced Omics to Support my Thesis Research

My thesis project is centered around the idea that novel immunomodulator ADA-1 may enhance the function of CD8+T cell in the context of HIV and Cancer. For this class I decided to focus on a paper that introducted over expression of ADA-1 in CAR-T cells as this was a critical piece of primary literature that I used to build my hypothesis: *Inosine Induces Stemness Features in CAR T cells and Enhances Potency* (Klysz, et al).  What they found high level was that overexpression of ADA-1 increased the stemlike phenotype of CAR-Ts and increased thier efficacy in targeting solid tumors. Beyond thier killing and proliferation assays, they preformed RNA seq to understand the differences between the control CAR-T cells and the ADA-1 overexpression edited CAR-T (ADAOE-CAR-T). 


### Data used from *Inosine Induces Stemness Features in CAR T cells and Enhances Potency* (Klysz, et al). 

For this data set and for the purposes of this class, I decided to work with the RNA seq data in the format of FASTQ files, from 4 samples. Control CAR-T (from 2 donors) and ADAOE-CAR-T (from those same 2 donors). Here I hope to use the tools learned in this class to make inquiries about the differences in gene expression between the two groups, to build upon my hypothesis that ADA-1 may enhance the function of CD8+T cells. 



### Links to Primary Literature:

- Link to paper: https://www-sciencedirect-com.ezproxy2.library.drexel.edu/science/article/pii/S1535610824000084?via%3Dihub

- Link to GEO Accession Viewer: https://www-ncbi-nlm-nih-gov.ezproxy2.library.drexel.edu/geo/query/acc.cgi?acc=GSE250443





### Introduction 

*In week 5 it was our assingment to zip up our files and use seqkit to look at the size of the files and run seqkit stats in order to understand a high level summaary of its contents. This markdown includes a high level summary of what type of data I have as well as  the seqkit stats.* 






### Location of Files: 
*I have the following files uploaded in the share directory here:*

    `~/share/aoe23/data/`







### Summary of File Sizes: 


| Size  | File                          |
|-------|-------------------------------|
| 9.2G  | data/SRR27237077.fastq         |
| 13G   | data/SRR27237081.fastq         |
| 11G   | data/SRR27237082.fastq         |
| 1.8G  | data/SRR27237076.fastq.gz      |
| 1.5G  | data/SRR27237077.fastq.gz      |
| 2.0G  | data/SRR27237081.fastq.gz      |
| 1.8G  | data/SRR27237082.fastq.gz      |










### Summary of SSR IDs and corresponding samples of interest: 

| Short Hand Sample ID | Sample ID from NCBI                 | Type of Edit | Donor | ncbi_ssr   | Zipped File Name               |
|----------------------|-------------------------------------|--------------|-------|------------|---------------------------------|
| ada_car_d48          | ADA-OE HA-CAR-T cells, donor 48     | ada-oe       | 43    | SRR27237076 | data/SRR27237076.fastq.gz       |
| car_d48              | control HA-CAR-T cells, donor 48    | control      | 48    | SRR27237077 | data/SRR27237077.fastq.gz       |
| ada_car_d43          | ADA-OE HA-CAR-T cells, donor 43     | ada-oe       | 48    | SRR27237081 | data/SRR27237081.fastq.gz       |
| car_d43              | control HA-CAR-T cells, donor 43    | control      | 43    | SRR27237082 | data/SRR27237082.fastq.gz       |













### Seqkit Stats for each file  

| File                       | Format | Type | Num Seqs   | Sum Len       | Min Len | Avg Len | Max Len |
|----------------------------|--------|------|------------|---------------|---------|---------|---------|
| data/SRR27237076.fastq.gz   | FASTQ  | DNA  | 26,450,863 | 3,967,629,450 | 150     | 150     | 150     |
| data/SRR27237077.fastq.gz   | FASTQ  | DNA  | 21,949,201 | 3,292,380,150 | 150     | 150     | 150     |
| data/SRR27237081.fastq.gz   | FASTQ  | DNA  | 29,749,784 | 4,462,467,600 | 150     | 150     | 150     |
| data/SRR27237082.fastq.gz   | FASTQ  | DNA  | 25,961,797 | 3,894,269,550 | 150     | 150     | 150     |

