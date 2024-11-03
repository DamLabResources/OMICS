# Week 10 Assignment: Arden Edgerton

## Assignment Instructions: 

1. Adjust the makefile to run on the full or mini directory. 
2. Then, create the gene expression matrix for each grouping and place them in your exercises folder with a Readme describing the changes you made.

***

## Part 1: Adjust the make file to run on the full or mini director

1. I first went through the steps we took in class to remake the quants folders that were generated during the in class lecture to refresh myself on the commands and make sure that I had the correct starting material. 

    `cd omics/aoe23/wk10`
    `mkdir quants`
    `nano makefile.og`
    
2. This make file og has the simplest commands that we used in class so that I could break down the steps more simply for myself. Given that I was getting error messages I used this to first focus on the mini ONLY. Also I changed the references to fastq to fastq.gz so that the were references the appropriate files within the source folder. (Contents of makefile.og below)

```bash
REF=/data/share/refs/SGD/salmonindex
SOURCE=/data/share/OMICS/wk10/mini


quants/%: $(SOURCE)/%_1.fastq.gz $(SOURCE)/%_2.fastq.gz
	salmon quant -i $(REF) -l A -1 $(SOURCE)/$*_1.fastq.gz -2 $(SOURCE)/$*_2.fastq.gz --validateMappings -o $@
```


3. ALthough we worked through a makefile that could make all at once I went through one by one for all of the mini folder using the commands: 

    `make -f  makefile.og quants/SRR24466374`
4. Repeated for each SRR file that I had iteratively. Note that once it was complete I had a folder for each MINI within the quants folder. 

5. Because I wanted to repeat this for full I then renamed this previously used quants folder to quants.mini and renamed the makefile that was previously named makefile.og to makefile.mini

6. To now use this iterative process to make quants for each of the full SRR's I first made a new quants directory, then I made a new make file called makefile.og.full
    `mkdir quants.full`
    `nano makefile.og.full`
    
7. The contents for makefile.og.full is now edited to reference the full folder in week 10 (edited in source) and also put the output in the quants.full folder. See the contents of the make file below: 








