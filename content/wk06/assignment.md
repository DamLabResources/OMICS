# Snowflake Yeast Alignment

# Instructions

Create a `excercise/{user}/wk06/README.md`.
Use this to keep track of your commands and present your results.
Use the read files in `~/share/OMICS/wk06/reads`.

 - Sub-sample the first 100K from each set into a new file in your working directory. Remember to keep track of sample names and R1/R2s.
 - Use `bwa mem` to align these reads to the SGD genome.
 - Use `samtools view` to determine how many reads aligned from each sample at a Q30 threshold. Create a table in your README describing this.
 - Use `samtools depth` and determine the average depth across each chromosome in each sample. 
 - After alignment, sorting, and indexing, download them to your own computer and load them into IGV.
 - Use the IGV browser, find a region where there seems to be a amino-acid change between the three samples. Take a screenshot and add it to the Readme.
 - Do a brief search about the protein, is anything known? Write about it in the README.


