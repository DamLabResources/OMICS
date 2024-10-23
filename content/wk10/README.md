# Introduction

This week we will look at the `salmon` RNA-Seq quantification tool.
It uses a psuedo-mapping technique to rapidly quantify transcriptomic data.
In addition to learning the `salmon` tool we will cover `makefile`s.
These types of files are an important piece of a bioinformatics toolbox because they can encapsulate complex pipelines in a single file. 

# Learning Objectives

By the end of this week you should be able to:
 * Recite and describe the three steps of a `salmon` quantification pipeline.
 * Construct commands for building `salmon` indexes, quantification, and merging.
 * Run `make` commands.
 * Describe makefile `replacements`.
 * Utilize `wildcard` and `patsubst` makefile functions to create file-conditional makefile pipelines.
 
# Assignment

Adjust the makefile to run on the `full` or `mini` directory.
Then, create the gene expression matrix for each grouping and place them in your `exercises` folder with a `Readme` describing the changes you made.
