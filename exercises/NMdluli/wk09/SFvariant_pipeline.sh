# !/bin/bash

# Script for generating bcf files for the OG_strain, SF_aer, and SF_ann from chromosome VIII
# Script will use aligned seq data for variant calling 
# variant_call path/to/sample.sorted.bam path/to/variants.bcf


# Useful to full paths in scripts so they run anywhere.
REF=/data/share/refs/SGD/saccharomyces_cerevisiae.fa
GFF=/data/share/refs/SGD/saccharomyces_cerevisiae.gff

# This command generates bcf files for the strains. In this command $1 is the input bam file and $2 is the output  bcf file
(bcftools mpileup -r chrVIII -Ou -f $REF $1 |
 bcftools call --ploidy 1 -mv -Ob -o $2)

# Before identifying variants, the bcf files need to be indexed
bcftools index $2

# This command finds varaints that are unique to each of the three strains. The unique variant output file will be a vcf
bcftools isec -p unique_variant -n=1 $2

# Convert vcf to bed file
BED_FILE="${unique_variant%.vcf}.bed"
(bcftools query -f '%CHROM\t%POS\t%POS\t%ID\n' $unique_variant | 
awk '{print $1"\t"$2-1"\t"$3}' > $BED_FILE)

# Finding unique regions that overlap with Bedtools
OVERLAP_FILE="${BED_FILE%.bed}_overlap.bed"
bedtools intersect -a $BED_FILE -b $GFF -bed > $OVERLAP_FILE


#getting some errors running this, will continue to update.
