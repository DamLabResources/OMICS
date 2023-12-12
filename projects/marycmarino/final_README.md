# Mary Marino Omics Project

### My Project
- This semester, I examined RNA seq data collected from two strains of *Haemophilus influenzae*.
- The first strain examined, called Rd, is the lab strain of *H. flu* and does not contain our gene of interest.
- The second strain examined, named GC594, contains a gene known as the macrophage survival factor (*msf*), which confers the ability to survive within a macrophage and traffic *H. flu* throughout the body of an animal model.
	- We are interested in studying the differences between the transcriptomes of these two strains under several different conditions to understand what the presence of the *msf* gene affects at the gene expression level.
	- The two conditions I have examined throughout this project were growing the cultures as planktonic cultures or as a biofilm.
- RNA seq was performed on Rd and GC594 strains in both a log phase culture and a biofilm culture. There are triplicates of each strain under each condition.
- For more information about my data: [data.md](data.md)
- For a more detailed account of my project workflow: [README.md](README.md)

### How I Organized My Data
- Follow this path to access my files: `~/share/courses/OMICS/RDSLR`
- In the `RDSLR` folder, there are several sub-folders:
	- `aligned_files` = concatenated .bam files
	- `concat files` = concatenated .fastq files
	- `coverage` = bedtools coverage results
	- `reads` = all data shared with me by Leanie Williams
	- `refs` = reference genome and .fastq files for each of the strains/conditions I wanted to look at for this project from the gigantic list of reads shared with me
	- `final_salmon_quant` = my salmon quant files (it took a few tries)
	- `RdKW20_salmon_index` = my salmon index, using `RdKW20.fasta` as my reference genome
	- `scripts` = shell scripts to align and concatenate files, created with help from Leanie Williams
	- `tmp` = temporary files
	- `transcriptome` = transcriptome data shared with me by Leanie Williams
	- `vars` = variant calls .bcf files
- You can ignore the folder titled `stringent_MM_KB` – that is data that Leanie shared with me for my research outside of class
- Follow this path to access my project notes: `~/repos/OMICS/projects/marycmarino`
- In the `projects/marycmarino` folder, there are several important documents:
	- `data.md` = summary of the data used for this project
	- `makefile` = makefile for creating a salmon index
	- `methods.md` = outline of my analysis steps
	- `README.md` = main file where I've documented everything I've done throughout the semester
	- `final_README.md` = this file – official final submission for this project
- You can ignore the folder titled `genomes` – that is data from the wk02 exercises from earlier in this course

### My Project Workflow
- Step 1: received the data from Leanie and concatenated my reads together using shell scripts in `scripts` folder
- Step 2: aligned my reads to the reference genome
- Step 3: calculated coverage estimations
- Step 4: called variants
- Step 5: RNA sequence quanitification via `salmon`
- See [README.md](README.md) for the exact commands used to accomplish each of these steps of my project! 

### Next Steps
- Now that I have a `quant.sf` file from my `salmon quant` analysis, I would next choose to use this data to do downstream analysis of the differences in gene expression between my strains.
- I also believe that graphing or otherwise visualizing the data collected and interpreted here would be useful in understanding the transcriptomic differences between strains under different conditions.
