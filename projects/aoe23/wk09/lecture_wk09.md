# Week 9 Lecture Notes

*** 

# Where everything is located from this week:  

## Lecture Notes: `repos/OMICS/projects/aoe23/wk09/lecture_wk09.md`

## Assignment: `repos/OMICS/exercises/aoe23/wk09/README.md`

## Lecture In Class Assignment Files Generated/Working Directory: `omics_aoe23/wk09/`


***

## Commands Used in Class Walkthrough: `repos/OMICS/content/wk09/lecture.md`

## AE Notes from using these commands in class

1. Base Command Used to make BCF File

    `bcftools mpileup -r chrI -Ou -f /data/share/refs/SGD/saccharomyces_cerevisiae.fa /data/share/OMICS/wk06/alns/OGstrain.sorted.bam | bcftools call --ploidy 1 -mv -Ob -o calls.bcf`

2. To look at BCF File

    `bcftools view calls.bcf | less -S`
    
        - note it is good to look at the file but it is not necessary for us to gain any information from it 
        - its good practice to always take a look at your file
        - NOte about the qualtiy scores: Indel Variants which is partly because we didnt start by running somethign to clear indels early 
        - Besides info column: it includes the name of the BAM file (in column titled format), and after this you can have as many samples as you have in the file
        - we only ran this with OG strain, so that is why there is only 1
        - To look at 2 samples: we can make 2 BAM Files 
    
# BCF Files: Binary Format

# VCF Files: You can visually inspect this--but you are not expected to be able to read it

View command

