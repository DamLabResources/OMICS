## Variant Calling


# Create bcf files for the OG_strain, SF_aer, and SF_ann from chromosome VIII
This command generates bcf files for the strains. In this command saccharomyces is the reference sequence; there is an input bam file and output  bcf file

```bash
bcftools mpileup -r chrVIII -Ou -f /data/share/refs/SGD/saccharomyces_cerevisiae.fa /data/share/OMICS/wk06/alns/OGstrain.sorted.bam | bcftools call --ploidy 1 -mv -Ob -o OGstrain.bcf 

bcftools mpileup -r chrVIII -Ou -f /data/share/refs/SGD/saccharomyces_cerevisiae.fa /data/share/OMICS/wk06/alns/SF_aer.sorted.bam | bcftools call --ploidy 1 -mv -Ob -o SF_aer.bcf  

bcftools mpileup -r chrVIII -Ou -f /data/share/refs/SGD/saccharomyces_cerevisiae.fa /data/share/OMICS/wk06/alns/SF_ann.sorted.bam | bcftools call --ploidy 1 -mv -Ob -o SF_ann.bcf 
```

# Use bcftools isec to find varaints that are unique to each of the three strains
First, we index all the bcf files to speed up analysis.

```bash
bcftools index SF_ann.bcf 
bcftools index SF_aer.bcf 
bcftools index OGstrain.bcf 
```
Using the isec tool, find unique variants to each strain. This will output three vcf files that show unique variants to each strain.

```bash
bcftools isec -p unique_variants -n=1 OGstrain.bcf SF_ann.bcf SF_aer.bcf
```

# Use bedtools to find the unique variants that overlap with regions defined in /share/refs/SGD/saccharomyces_cerevisiae.gff
Before intersecting the unique variants with the reference, the vcf files need to be converted to bed files inorder to be compatible with bedtools.

```bash
 bcftools query -f '%CHROM\t%POS\t%POS\t%ID\n' unique_variants/0001.vcf |  awk '{print $1"\t"$2-1"\t"$3}' > SF_ann.bed
 bcftools query -f '%CHROM\t%POS\t%POS\t%ID\n' unique_variants/0000.vcf |  awk '{print $1"\t"$2-1"\t"$3}' > OGstrain.bed
 bcftools query -f '%CHROM\t%POS\t%POS\t%ID\n' unique_variants/0002.vcf |  awk '{print $1"\t"$2-1"\t"$3}' > SF_aer.bed
```

In addition, the reference was run as a bed file as well. The intersects were piped into aunique overlaps bed file for each strain. 

```bash
bedtools intersect -a OGstrain.bed -b saccharomyces_cerevisiae.gff -bed > OGstrain_unique_overlaps.bed
bedtools intersect -a SF_aer.bed -b saccharomyces_cerevisiae.gff -bed > SF_aer_unique_overlaps.bed
bedtools intersect -a SF_ann.bed -b saccharomyces_cerevisiae.gff -bed > SF_ann_unique_overlaps.bed
```

The overlaps were viewed on IGV. Single nucleotide variants were shown as ticks across each strain for chromosome VIII.

![Variant_Overlaps](repos/OMICS/exercises/NMdluli/wk09/Variant_Overlaps.png)

