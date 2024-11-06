# Wk09 Assignment Edgerton

## Notes from Assignment Description In Class/Comments from Will

- **Overall Goal:** High Level goal: you are trying to find the snps that make this a snowflake: so snps that are actually important in this context. 

- **Will already:**
    - Aligned the genomes
    - Intersected them against the genes using the .gff
    - Useful tools: SnpEff is a tool that takes the vcf file and looks at which gene is it in and asks: 
        - will it change the codon of that amino acid
        - low impact: synonomous mutation or no change mutation 
        - severe impact: frameshift/stopcodon


## Pipeline

Adjust your pipeline so you can specify which chromosome you generate variant calls for at the command line.
Update the documentation and place it in your week 9 excercise folder and commit it.

## Exercise

For each of the three strains aligned in `/data/share/omics/wk06/alns`

1. Use the pipeline to create bcf files for the OG_strain, SF_aer, and SF_ann from any chromosome but `chrI`.
2. Use `bcftools isec` to find varaints that are unique to each of the three strains.
3. Use `bedtools` to find the unique variants that overlap with regions defined in `/share/refs/SGD/saccharomyces_cerevisiae.gff`.
4. Visualize a selection of them in IGV.

***


## Log of Commands Used

### Part 1: 1. Use the pipeline to create bcf files for the OG_strain, SF_aer, and SF_ann from any chromosome but `chrI`.

1. I went back to the folder that I use for in class follow along assingments, specifically week 9 because I need to make changes to the pipeline that I previously made

    `cd omics_aoe23/wk09`
    
2. Then I used the file tools on the side to click on and open the variant pipeline that was made in class: 

    `omics_aoe23/wk09/variant_pipeline.sh`

3. I looked at what was in the current pipeline, and ajusted to look at chromosome II instead of chromosome I by changing the line in (bcftools mpileup)
    
**ORGINAL PIPELINE BELOW:** 

```bash
#!/bin/bash

# Script for aligning and variant calling yeast sequence data
# variant_call path/to/sample.sorted.bam path/to/variants.bcf

# Define some constants
FILTER='DP>=10&&QUAL>20'

# Useful to full paths in scripts so they run anywhere.
REF=/data/share/refs/SGD/saccharomyces_cerevisiae.fa


(bcftools mpileup -Ou -f $REF $1 |
    bcftools call -m |         
    bcftools filter -Ob -i $FILTER > $2)
sh ./variant_pipeline.sh /data/share/OMICS/wk06/alns/OGstrain.sorted.bam OG_calls.bcf
```



**UPDATED contents in pipeline**
    
```bash   
#!/bin/bash

# Script for aligning and variant calling yeast sequence data

# Define some constants
FILTER='DP>=10&&QUAL>20'

# Use full paths in scripts so they run anywhere.
REF=/data/share/refs/SGD/saccharomyces_cerevisiae.fa

(bcftools mpileup -Ou -f $REF -r chrII $1 |
  bcftools call -m |         
  bcftools filter -Ob -i $FILTER > $2)
```


4. I ran this code to make a bcf file for each based on chromosome II:


    `./variant_pipeline.sh /data/share/OMICS/wk06/alns/OGstrain.sorted.bam OG_calls_chr2.bcf`
    
    `./variant_pipeline.sh /data/share/OMICS/wk06/alns/SF_aer.sorted.bam SF_aer_chr2.bcf`
    
    `./variant_pipeline.sh /data/share/OMICS/wk06/alns/SF_ann.sorted.bam SF_ann_calls_chr2.bcf`
    
***

### PART 2: 2. Use `bcftools isec` to find varaints that are unique to each of the three strains.


1. I indexed each file using this: 
    ` bcftools index OG_calls_chr2.bcf`

    `bcftools index SF_aer_chr2.bcf`

    `bcftools index SF_ann_calls_chr2.bcf`

   
2. I then ran this command: 

    `bcftools isec -n-1 -c all OG_calls_chr2.bcf SF_aer_chr2.bcf SF_ann_calls_chr2.bcf -O z -p isec_output`

*** 

### PART 3: 3. Use `bedtools` to find the unique variants that overlap with regions defined in `/share/refs/SGD/saccharomyces_cerevisiae.gff`.

1. Convert bcf/vcf to bed format

`bcftools query -f 'chr\[%CHROM\t%POS\t%POS\t%ID\n\]' isec_output/0000.vcf.gz > unique_variants_OG.bed`

`bcftools query -f 'chr\[%CHROM\t%POS\t%POS\t%ID\n\]' isec_output/0001.vcf.gz > unique_variants_SF_aer.bed`

`bcftools query -f 'chr\[%CHROM\t%POS\t%POS\t%ID\n\]' isec_output/0002.vcf.gz > unique_variants_SF_ann.bed`



2. Then I prepared the regions from GFF

    `awk 'BEGIN {OFS="\t"} {if ($1 !~ /^#/) print $1, $4-1, $5, $3}' ~/share/refs/SGD/saccharomyces_cerevisiae.gff > regions.bed`
    
3. Then I found the intersects: 


    `bedtools intersect -a unique_variants_OG.bed -b regions.bed > unique_variants_OG_overlap.bed`
    `bedtools intersect -a unique_variants_SF_aer.bed -b regions.bed > unique_variants_SF_aer_overlap.bed`
    `bedtools intersect -a unique_variants_SF_ann.bed -b regions.bed > unique_variants_SF_ann_overlap.bed`
    
    
***

### PART$: 4. Visualize a selection of them in IGV.

1. Download all overlap bed files 

2. Load into IGV and screenshot an overlap. 
