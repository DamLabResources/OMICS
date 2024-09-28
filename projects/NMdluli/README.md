# Introduction
Project description: the goal of this project is to use RNAseq data to profile liver stage Plasmodium vivax parasites. The resource paper for this data is titled "A single-cell liver atlas of Plasmodium vivax infection".
P. vivax parasites can enter a hypnozoite stage and linger in the human liver for an extended period of time. These hypnozoites can reactivate to cause blood-stage infection. The resource paper uses a bioengineered human microliver platform to culture patient-derived P. vivax parasite for transcriptional profiling in replicative and non-replicative liver-stage parasites and their host cell dependence. For this project, I will only characterize parasite transcripts 1 day post hepatocyte infection and 11 days post hepatocyte infection.  


## Data Set Description
The bioproject number for this data is PRJNA810434. For each sample, I selected uninfected heptocyte samples and P. vivax infected hepatocytes.This way, I can delineate parasite transcriptome information. This will also provide some information on host baseline transcriptome, however, it would be ideal to get a true picture of host transcriptome by comparing uninfected hepatocytes to mock infected hepatocytes. The data will  compare samples from day 1 post infection at early parasite liver stage development (schizont stage) vs day 11 post infection at late parasite liver stage development (comprising a mix of both replicating schizonts and non-replicative hypnozoites). 

|Sample ID    |SRR Number  |Infection  |Days PI |Isolated Cell Type     |Description                                                        |
|:-----------:|:----------:|:---------:|:------:|:---------------------:|:-----------------------------------------------------------------:|
|GSM5916720   |SRR18134243 |Uninfected |1       |human hepatocytes      |to obtain baseline host/parasite transcriptome                     |
|GSM5916722   |SRR18134245 |P. vivax   |1       |P. vivax in hepatocytes|infection with 100K sporozoites representing early stage parasites |
|GSM5916736   |SRR18134267 |Uninfected |11	|human hepatocytes	|to obtain baseline host/parasite transcriptome                     |
|GSM5916738   |SRR18134269 |P. vivax   |11	|P. vivax in hepatocytes|100K sporozoites representing late stage parasites and hypnozoites |

## Exploring Data files with seqkit wk05
Before beginning any work with the files, I used `seqkit` to gzip the files so I could continue to work with the compressed files.

Comparing the sizes of the original and the compressed files I used `duh -h`. The table below summarizes the significant compression in size. Once compressed, the orinigal `fastq` files were deleted.

```bash
seqkit seq -o Project_Data/SRR18134243_1.fq.gz SRR18134243_1.fastq 
```

```bash
du -h SRR181342*.f*
```

|SRR ID       |Original Size .fq  |Compressed Size .gz   |
|:-----------:|:-----------------:|:--------------------:|
|SRR18134243_1|63G                |8.2G                  |
|SRR18134243_2|92G                |14G                   |
|SRR18134245_1|63G                |8.3G                  |
|SRR18134245_2|93G                |14G                   |
|SRR18134267_1|61G                |8.3G                  |
|SRR18134267_2|90G                |15G                   |
|SRR18134269_1|88G                |12G                   |
|SRR18134269_2|129G               |21G                   |

Using the .gz files, I used `seqkit stats` to count the number of reads in each file and summarized the results in a table.

```bash
seqkit stats SRR18134243_1.fq.gz SRR18134243_2.fq.gz SRR18134245_1.fq.gz SRR18134245_2.fq.gz SRR18134267_1.fq.gz SRR18134267_2.fq.gz SRR18134269_1.fq.gz SRR18134269_2.fq.gz > Pvivax_liver_parasites.stats.tsv
```

|file          |format| type |num_seqs    |sum_len        |min_len  |avg_len |max_len|
|:------------:|:----:|:----:|:----------:|:-------------:|:-------:|:------:|:-----:|
|SRR18134243_1 |FASTQ |DNA   |523,607,299 |10,472,145,980 |20       |20      |20     |
|SRR18134243_2 |FASTQ |DNA   |523,607,299 |26,180,364,950 |50       |50      |50     |
|SRR18134245_1 |FASTQ |DNA   |531,135,838 |10,622,716,760 |20       |20      |20     |
|SRR18134245_2 |FASTQ |DNA   |531,135,838 |26,556,791,900 |50       |50      |50     |
|SRR18134267_1 |FASTQ |DNA   |511,692,306 |10,233,846,120 |20       |20      |20     |
|SRR18134267_2 |FASTQ |DNA   |511,692,306 |25,584,615,300 |50       |50      |50     |
|SRR18134269_1 |FASTQ |DNA   |737,246,357 |14,744,927,140 |20       |20      |20     |
|SRR18134269_2 |FASTQ |DNA   |737,246,357 |36,862,317,850 |50       |50      |50     |
       
The sequence statistics show that each sample has over a hundred million reads. This makes sense because the data is generated from P. vivax infected hepatocytes, therefore, we are getting reads from both the parasite and the monolayer of hepatocytes (this is a tissue culture in vitro model). In addition, each monolayer of hepatocytes was infected with about 100K P. vivax sporozoites. To delineate P.vivax parasite transcripts from hepatocytes, the data will be aligned with parasite reference sequences to obtain parasite specific information. It was interesting to see that all samples had uniform read lengths which makes sense since this was a controlled experiment with the same tissue type and parasite species. This may also be explained by similar processing across the samples. 

I'm interested in exploring enriched developmental genes in P. vivax liver parsites. It's thought that the liver primarily hosts the asexual stages of the parasite during the early stages of infection, not the gametocytes. I wanted to check a male gametocyte motif in sequences from this P. vivax liver infection model. The previously identified blood stage male gametocyte motif that I used with `seqkit grep` is the motif CGTACA (Westenberger et al, 2010). Below is an example of the `seqkit grep` code used to check for the motif in each of the samples.

```bash
seqkit grep -o SRR43_1.fq.gz -s -p 'CGTACA' SRR18134243_1.fq.gz
```
I then ran stats on the motif filtered data.

```bash
seqkit stats SRR43_1.fq.gz SRR45_1.fq.gz SRR67_1.fq.gz SRR69_1.fq.gz > Male_gametes.stats.tsv
```

|file         |format|type |num_seqs |sum_len   |min_len|avg_len|max_len|
|:-----------:|:----:|:---:|:-------:|:--------:|:-----:|:-----:|:-----:|
|SRR43_1.fq.gz|FASTQ |DNA  |2,706,452|54,129,040|20     |20     |20     |
|SRR45_1.fq.gz|FASTQ |DNA  |2,923,613|58,472,260|20     |20     |20     |
|SRR67_1.fq.gz|FASTQ |DNA  |3,292,483|5,849,660 |20     |20     |20     |
|SRR69_1.fq.gz|FASTQ |DNA  |2,740,627|54,812,540|20     |20     |20     |

The results identified some reads that matched the male gaetocyte motif. However, this was identified in both infected and uninfected samples. I would have to align these samples to a reference P. vivax sequence to see where the identified sequences align.


## Literature Review
1. Westenberger SJ, McClean CM, Chattopadhyay R, Dharia NV, Carlton JM, Barnwell JW, Collins WE, Hoffman SL, Zhou Y, Vinetz JM, Winzeler EA. A systems-based analysis of Plasmodium vivax lifecycle transcription from human to mosquito. PLoS Negl Trop Dis. 2010 Apr 6;4(4):e653. doi: 10.1371/journal.pntd.0000653. PMID: 20386602;

## Methodology

## Results

## Discussion

## Conclusion

## References
