# My project

## Description

I am analyzing *P. vivax* samples from Duffy negative and positive people from Botswana to round out analysis I am already conducting for people from Sudan. I am interested in comparing SNPs between Duffy negative and positive individuals and finding regions that may be unique in Duffy negative people that may lead to a reason for the parasite infecting the Duffy negative people. I will be looking at 43 potential erythrocyte binding genes, the LDH gene, as well as other noncoding areas that may affect expression of the 43 or other genes. Typically, parasites infecting Duffy negative individuals are less polymorphic than those in Duffy positive individuals, potentially due to a smaller pool and lower parasitemia.

I then did seqkit stats on my four data files and got the following results 

|file                   |format  |type   |num_seqs      |sum_len  |min_len  |avg_len  |max_len|
|---|---|---|---|---|---|---|---|
|ERR5709537_2.fastq.gz  |FASTQ   |DNA   |3,493,042  |527,449,342      |151      |151      |151|
|ERR5709538_1.fastq.gz  |FASTQ   |DNA   |2,335,700  |352,690,700      |151      |151      |151|
|ERR5709539_1.fastq.gz  |FASTQ   |DNA   |3,301,593  |498,540,543      |151      |151      |151|
|ERR5709560_1.fastq.gz  |FASTQ   |DNA   |3,363,901  |507,949,051      |151      |151      |151|

It is interesting how all of the reads are the same exact length, but I also used seqkit pair before this as I had a _ 1 and _ 2 so it may in part be due to that. There are a lot of reads in the files as not only is there P. viax DNA but there is also human DNA and potentially P. falciparum DNA in there as well due to coinfection. 
To get the paired reads I used 

seqkit pair -1 ERR5709560_1.fastq.gz -2 ERR5709560_2.fastq.gz -O resulterr5709560 -u

for each of the file pairs.
To understand much of this data I will need to align it to the P. vivax genome so I know I am looking at the right DNA sequences and not some human DNA. 
Upon doing 

seqkit head ERR5709537_1.fastq.gz 

I saw that the sequences look to be of ok quality, with a fairly equal combination of capital letters (good quality) and numbers/symbols.
