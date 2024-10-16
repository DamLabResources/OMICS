# Week 9 Lecture Notes

*** 

# Where everything is located from this week:  

### Lecture Notes: `repos/OMICS/projects/aoe23/wk09/lecture_wk09.md`

### Assignment: `repos/OMICS/exercises/aoe23/wk09/README.md`

### Lecture In Class Assignment Files Generated/Working Directory: `omics_aoe23/wk09/`


***

## Can Find Details for Commands Used in Class Walkthrough: `repos/OMICS/content/wk09/lecture.md`

## AE Notes from using these commands in class:

1. **Base Command Used to make BCF File**

    `bcftools mpileup -r chrI -Ou -f /data/share/refs/SGD/saccharomyces_cerevisiae.fa /data/share/OMICS/wk06/alns/OGstrain.sorted.bam | bcftools call --ploidy 1 -mv -Ob -o calls.bcf`


2. **To look at BCF File**

    `bcftools view calls.bcf | less -S`
    
        - note it is good to look at the file but it is not necessary for us to gain any information from it 
        - its good practice to always take a look at your file
        - NOte about the qualtiy scores: Indel Variants which is partly because we didnt start by running somethign to clear indels early 
        - Besides info column: it includes the name of the BAM file (in column titled format), and after this you can have as many samples as you have in the file
        - we only ran this with OG strain, so that is why there is only 1
        - To look at 2 samples: we can make 2 BAM Files 
        - BCF Files: Binary Format
        - VCF Files: You can visually inspect this--but you are not expected to be able to read it
        - BCF File is easy to grep.


3. **To look at variant stats (The most common, is to ask for the Summary Numbers)**

    `bcftools stats calls.bcf | grep '^SN'`


4.  **Variant Filtering: After you've done all of your calling and merging, you need to filter the variants.In general, you want to filter on at least two things.**

    - Read-depth AND Quality score filter in one line of code do this
    
        `bcftools filter -i "DP>=10&&QUAL>20" calls.bcf | less -S`
    
    - Now calls.bcf is ready to move and we can proceed with functional analysis.

5. **Make a File For Pipeline or SCRIPT!!

    `touch variant_pipeline.sh`
    
6. **Open the file: can just click to the file same way I edit readme**


7. **Once in file copy and paste this from `lecture.md`



            #!/bin/bash

             Script for aligning and variant calling yeast sequence data
            # variant_call path/to/sample.sorted.bam path/to/variants.bcf

            # Define some constants
            FILTER='DP>=10&&QUAL>20'

            # Useful to full paths in scripts so they run anywhere.
            REF=/data/share/refs/SGD/saccharomyces_cerevisiae.fa


            (bcftools mpileup -Ou -f $REF $1 |
            bcftools call -m |         
            bcftools filter -Ob -i $FILTER > $2)
            sh ./variant_pipeline.sh /data/share/OMICS/wk06/alns/OGstrain.sorted.bam OG_calls.bcf

8. **Nicely this has now become an automated process. and basically when I say sh it is a new command that i have defined. Note that there are some variables and other thresholds defined within that text. 

9. **Now we can run the pipeline with this code. note that I am saying first: sh, then referencing the bam file nad then having it create a file called OG_calls.bcf

    `sh variant_pipeline.sh ~/share/OMICS/wk06/alns/SF_aer.sorted.bam SF_aer.bcf`


10. **Now we are going to work in IGV

- Convert BCF file to vcf file 
    `bcftools view calls.bcf > calls.vcf`

- Download vcf file

- Open IGV

- use genome we have previously uploaded

- File, load from file 

- upload calls.vcf

- top bar: next to where you select the genome, select the chromosome 

- choose chromosome 1 because this is what the vcf file is including the variants from 

- can scroll through and look at this 

- Class ends here: move on to assignment





