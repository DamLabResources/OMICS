# Data Summary for Omics Project 

## Contents of This Data Summary



##### 1. Links to Primary Literature:

##### 2. Introduction 

##### 3. Location of Files: 

##### 4. Summary of File Sizes: 

##### 5. Summary of SSR IDs and corresponding samples of interest: 

##### 6. Summary of SSR IDs and corresponding samples of interest: 




***



### Links to Primary Literature:

- Link to paper: https://www-sciencedirect-com.ezproxy2.library.drexel.edu/science/article/pii/S1535610824000084?via%3Dihub

- Link to GEO Accession Viewer: https://www-ncbi-nlm-nih-gov.ezproxy2.library.drexel.edu/geo/query/acc.cgi?acc=GSE250443

- Link to the SSR Run selector: https://www.ncbi.nlm.nih.gov/Traces/study/?acc=PRJNA1053617&o=acc_s%3Aa




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

