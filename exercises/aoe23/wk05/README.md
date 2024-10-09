# Week 5: Notes
 
#### This week we went over how to work with seqkit. We learned how to use this tool to make inquiries about both fasta/q files. Below are a list of commands that we learned as well as the associated function of each.



### **First, a note about the two directories that I have:**

(1)	How to get into the folder that has my data:
    ` $ cd share/aoe23`

(2)	How to get into my repos that includes the ReadME files for each week: 
    `$ cd repos/OMICS/projects/aoe23`

### **Start working in jupyter notebook**

In order to start working in the jupyter notebook must make sure that we pull down any changes that Dr. Dampier has made throughout the week:
1. Go to github fork that I have:` https://github.com/ardenedgerton/OMICS`
2. Click on Sync Fork
3. Open Jupyter notebook: `http://10.248.148.22/hub/user/aoe23/lab/tree/share`
4. Once the fork is synced use this code to pull down any changes made: (This will pull down the changes that were made from the fork/and this will also allow us to see the log to confirm that we have the recent additions. Another validation for this is to open week 5 folder and check for its contents (assuming that you are already in repos/OMICS/)
    - `$ cd repos/OMICS/`
    - `$ git pull`
    - `$ git config pull.rebase true`
    - `$ git log`

5. Confirm that the new additions to wk05 have been pulled down: 
    - `$ cd content/wk05`
    - `$ tree`



# Week 5 Assignment 
*Last week  I uploaded fastq files to the share/aoe23/. This week I want to (1) move those files into a folder that is called data, and (2) then zip them up so that they are smaller. I will keep the unzipped and zipped files temporarily in order to (3) show their change in disk space, and then I will (4) remove the files.

#### Deliverables for next week:
1. Zip up files
2. Use du -h to show the change in size to validate change in size 
3. Upload readME

## Step 0: Move the files to a new directory

 
1. First make folder: `mkdir data`
2. Then move `mv SRR27237081.fastq SRR27237082.fastq data/`
3. Needed to rename SRR272370771 to remove the 1 so did this code: `mv data/SRR272370771.fastq SRR27237077.fastq`
4. Realized that the move was then just in ao23 folder so moved it directly into data by using this code `mv SRR27237077.fastq data/SRR27237077.fastq`
5. Repeat the move of the rest of the files into data folder 


## Step 1: Zip the files

1. Use the code below to zip all of the files (I have 4 total so see the fact that each file was zipped independently and that is why there are 4 commands. 
    `gzip -9 data/SRR27237076.fastq -c > data/SRR27237076.fastq.gz
    gzip -9 data/SRR27237082.fastq -c > data/SRR27237082.fastq.gz
    gzip -9 data/SRR27237081.fastq -c > data/SRR27237081.fastq.gz
    gzip -9 data/SRR27237077.fastq -c > data/SRR27237077.fastq.gz`
2. Note this takes a long time to do and so i opened multiple terminals to do this at the same time, and then worked on something else

## Step 2: Compare the size of each file


1. First looked at all of the sizes of unzipped files using this sample command: 
    `du -h data/SRR27237076.fastq`

2. I got the following readout as a result: 
    **11G     data/SRR27237076.fastq**

3. I repeated for the rest of the files using the commands below: 
    - `$ du -h data/SRR27237077.fastq`
    - `$ du -h data/SRR27237081.fastq`
    - `$ du -h data/SRR27237082.fastq`

4. then looked at sizes of zipped files
    - `du -h data/SRR27237076.fastq.gz`
    - `du -h data/SRR27237077.fastq.gz`
    - `du -h data/SRR27237081.fastq.gz`
    - `du -h data/SRR27237082.fastq.gz`


5. I can see that all zipped files are now a range of 1.5G - 2.0G which is much smaller than the size they were before. (summarized in table below)

| Size  | File                          |
|-------|-------------------------------|
| 9.2G  | data/SRR27237077.fastq         |
| 13G   | data/SRR27237081.fastq         |
| 11G   | data/SRR27237082.fastq         |
| 1.8G  | data/SRR27237076.fastq.gz      |
| 1.5G  | data/SRR27237077.fastq.gz      |
| 2.0G  | data/SRR27237081.fastq.gz      |
| 1.8G  | data/SRR27237082.fastq.gz      |


## Step 3. All changes have now been uploaded to this readme file in 'notes.md'

1. Location: `repos/OMICS/exercises/aoe23/wk05/README.md`
2. These were previously saved in a notes.md file in my repos but were moved 2024-10-04
3. In order to make sure that they are all saved do the following commands: 
    - `git commit -a -m 'final updates to notes.md for class week 6'`
    - `git push`
4. and then sync fork within github site: https://github.com/ardenedgerton/OMICS/tree/main


## Update 2024-10-04
1. Previously had all of these notes saved in my md file "notes.md" in my repos/projects/aoe23
2. Today I edited this to look more presentable and readable for myself in the future and the professors in this class
3. I realized that I have been pushing and pulling to the origin, but I have not yet made a pull request to Dr. Dampier which is why my repos has not been updated adequately and will do so today!

## Ongoing to-do's

1. Write a markdown file that describes your dataset. Include that seqkit stats table as a markdown table.
    Code Used: 
    - `jupyter-aoe23@Mistake-Not:~/share/aoe23$ seqkit stats data/S*.gz*`
    - This summary is stored in a table in `repos/OMICS/projects/aoe23/datasummary.md`
2. Describe the number of reads per sample in your study. Does it tell you anything interesting?
    - This will be located in my `repos/OMICS/projects/aoe23/datasummary.md`