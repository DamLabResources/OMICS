# Week 9: Variant calling

Now that we have reads aligned to our genome we can look for areas where they differ.
We will use `bcftools` to call small genomic variants and manipulate the resulting files.
Now that we have a "complete" analysis, we will talk about basic shell scripting and creating pipelines.


# Learning Objectives

* List comonly used variant callers and their advantages & limitation. 
* Employ `bcftools` to call varaints in snowflake yeast.
* Use `bcftools` to filter variants by quality.
* Read basic information from variant call formatted files.
* Write a variant calling pipeline.

# Assignment and Project

This week we'll work primarily on our projects this week.

* In your project directory, create a file called `methods.md` and create a reference and link to it in your main `README.md` file.
* Use this file to enumerate the analysis steps of your pipeline.
* Use section headers `#` , `##`, and `###` to organize your document.
* Use ticks to put example commands.
* Describe the inputs and outputs of commands.
* Denote which files can be used across multiple samples.
* Note which files are "worth saving" and which are just temporary steps in the pipeline that should be cleaned up.

After this, **try** making a script that accomplishes these tasks.