## Week 5: Notes
 
### *This week we went over how to work with seqkit. We learned how to use this tool to make inquiries about both fasta/q files. Below are a list of commands that we learned as well as the associated function of each.*


# Introduction
**First, a note about the two directories that I have:**

(1)	How to get into the folder that has my data:

    ` $ cd share/aoe23`

(2)	How to get into my repos that includes the ReadME files for each week: 
    `$ cd repos/OMICS/projects/aoe23`

**Start working in jupyter notebook**

In order to start working in the jupyter notebook must make sure that we pull down any changes that Dr. Dampier has made throughout the week:
1.	Go to github fork that I have: https://github.com/ardenedgerton/OMICS
2.	Click on Sync Fork
3.	Open Jupyter notebook: http://10.248.148.22/hub/user/aoe23/lab/tree/share
4.	`$ cd repos/OMICS/`
5.	`$ git pull`
6.	`$ git config pull.rebase true`
7.	`$ git log`

This will pull down the changes that were made from the fork/and this will also allow us to see the log to confirm that we have the recent additions. Another validation for this is to open week 5 folder and check for its contents (assuming that you are already in repos/OMICS/ :

8.	`$ cd content/wk05`

9.	`$ tree`



# Week 5 Assignment 
*Deliverables for next week:*
1.	Zip up files
2.	Use du -h to show the change in size to validate change in size 
3.	Upload readME

# 1. Zip up files

*Last week  I uploaded fastq files to the share/aoe23/. This week I want to (1) move those files into a folder that is called data, and (2) then zip them up so that they are smaller. I will keep the unzipped and zipped files temporarily in order to (3) show their change in disk space, and then I will (4) remove the files.


## Move files into new folder
 
First make folder: `mkdir data`
then move `mv SRR27237081.fastq SRR27237082.fastq data/`
noted that need to rename SRR272370771 to remove the 1 so did this code: `mv data/SRR272370771.fastq SRR27237077.fastq`
realized that the move was then just in ao23 folder so moved it directly into data by using this code `mv SRR27237077.fastq data/SRR27237077.fastq`

repeat the move of the rest of the files into data folder 


## Zip the files

`gzip -9 data/SRR27237076.fastq -c > data/SRR27237076.fastq.gz
gzip -9 data/SRR27237082.fastq -c > data/SRR27237082.fastq.gz
gzip -9 data/SRR27237081.fastq -c > data/SRR27237081.fastq.gz
gzip -9 data/SRR27237077.fastq -c > data/SRR27237077.fastq.gz`


Repeat for each file 
Note this takes a long time to do and so i opened multiple terminals to do this at the same time, and then worked on something else

# 2. Compare the size of each file


First looked at all of the sizes of unzipped files

jupyter-aoe23@Mistake-Not:~/share/aoe23$ `du -h data/SRR27237076.fastq`
11G     data/SRR27237076.fastq
jupyter-aoe23@Mistake-Not:~/share/aoe23$ `du -h data/SRR27237077.fastq`
9.2G    data/SRR27237077.fastq
jupyter-aoe23@Mistake-Not:~/share/aoe23$ `du -h data/SRR27237081.fastq`
13G     data/SRR27237081.fastq
jupyter-aoe23@Mistake-Not:~/share/aoe23$ `du -h data/SRR27237082.fastq`
11G     data/SRR27237082.fastq

then looked at sizes of zipped files

jupyter-aoe23@Mistake-Not:~/share/aoe23$ `du -h data/SRR27237076.fastq.gz`
1.8G    data/SRR27237076.fastq.gz
jupyter-aoe23@Mistake-Not:~/share/aoe23$ `du -h data/SRR27237077.fastq.gz` 
1.5G    data/SRR27237077.fastq.gz
jupyter-aoe23@Mistake-Not:~/share/aoe23$ `du -h data/SRR27237081.fastq.gz` 
2.0G    data/SRR27237081.fastq.gz
jupyter-aoe23@Mistake-Not:~/share/aoe23$ `du -h data/SRR27237082.fastq.gz`
1.8G    data/SRR27237082.fastq.gz

can see that all zipped files are now a range of 1.5G - 2.0G which is much smaller than the size they were before.

# 3. All changes have now been uploaded to this readme file in 'notes.md'

in order to make sure that they are save I will 
`git commit -a -m 'final updates to notes.md for class week 6'`

`git push `

and then sync fork within github site: https://github.com/ardenedgerton/OMICS/tree/main
 