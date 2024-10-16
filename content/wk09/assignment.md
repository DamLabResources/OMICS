# Assignment

In this assignment you will practice using your the pipeline to create BCF files from alignments.

Keep a long of your commands and results in `{repo_root}/excercises/{userid}/wk09`.

## Pipeline

Adjust your pipeline so you can specify which chromosome you generate variant calls for at the command line.
Update the documentation and place it in your week 9 excercise folder and commit it.

## Exercise

For each of the three strains aligned in `/data/share/omics/wk06/alns`

1. Use the pipeline to create bcf files for the OG_strain, SF_aer, and SF_ann from any chromosome but `chrI`.
2. Use `bcftools isec` to find varaints that are unique to each of the three strains.
3. Use `bedtools` to find the unique variants that overlap with regions defined in `/share/refs/SGD/saccharomyces_cerevisiae.gff`.
4. Visualize a selection of them in IGV.
