Wk09 assignment

- using the instructions from the lecture, I created a variant pipeline sh file
- to test the script, I used the sh command and called the OGstrain.sorted.bam file
- to specify the chromosome, I added an additional variable called CHR where I specified chromosome VIII; then I added -r to the mpileup command
```bash
sh variant_pipeline.sh /data/share/OMICS/wk06/alns/OGstrain.sorted.bam OG_calls.chr8.bcf
```
- running the command I generated OG_calls.chr8.bcf; then I repeated this for SF_aer and SF_ann
- trying to run bcftools isec required indexing, so I ran bcftools index on each bcf file prior to isec
- isec revealed variations at multiple locations on chromosome 8, including positions 562109 (A -> ATTTTTTTTT), 562139 (T -> TGTAGTAGTA), and 562596 (G -> GGGTGTGGTGTGGTGTG)
- then I used bedtools intersect to find unique variants that overlap with the reference genome
- however, bedtools would not accept bcf files, so I used bcftools convert to convert the bcf files back to vcf

```bash
bedtools intersect -a /data/share/refs/SGD/saccharomyces_cerevisiae.gff -b OG_calls.chr8.vcf > OGintersect.bed
```

However attempting to open this bed file in IGV gave this error upon using the built-in indexing function:
[error](http://10.248.148.22/hub/user-redirect/lab/tree/OMICS/wk09/error.png)

I'm guessing this is to do with "SGD" as opposed to an integer but I am unsure how to solve this error...