# OMICS PROJECT

***

## Introduction:

### Using Advanced Omics to Support my Thesis Research

My thesis project is centered around the idea that novel immunomodulator ADA-1 may enhance the function of CD8+T cell in the context of HIV and Cancer. For this class I decided to focus on a paper that introducted over expression of ADA-1 in CAR-T cells as this was a critical piece of primary literature that I used to build my hypothesis: *Inosine Induces Stemness Features in CAR T cells and Enhances Potency* (Klysz, et al).  What they found high level was that overexpression of ADA-1 increased the stemlike phenotype of CAR-Ts and increased thier efficacy in targeting solid tumors. Beyond thier killing and proliferation assays, they preformed RNA seq to understand the differences between the control CAR-T cells and the ADA-1 overexpression edited CAR-T (ADAOE-CAR-T). 

***

## Literature Review:

### Data used from *Inosine Induces Stemness Features in CAR T cells and Enhances Potency* (Klysz, et al). 

For this data set and for the purposes of this class, I decided to work with the RNA seq data in the format of FASTQ files, from 4 samples. Control CAR-T (from 2 donors) and ADAOE-CAR-T (from those same 2 donors). Here I hope to use the tools learned in this class to make inquiries about the differences in gene expression between the two groups, to build upon my hypothesis that ADA-1 may enhance the function of CD8+T cells. 

***

## Methodology:

1. First zip files with share folder to use for NF core and make sample sheet in appropriate format. See details on steps and data files used here : 

    ```
    ~/repos/OMICS/projects/aoe23/data_summary.md
    ```

2. Communicate with Josh to run nf core with the following sh, sample sheet and .gz zipped files for each located in `~/share/aoe23`



```

    jupyter-aoe23@Mistake-Not:~/share/aoe23$ tree
    .
    ├── data
    │   ├── SRR27237076.fastq.gz
    │   ├── SRR27237077.fastq.gz
    │   ├── SRR27237081.fastq.gz
    │   └── SRR27237082.fastq.gz
    ├── run.sh
    └── samplesheet.csv

    1 directory, 6 files



```

***

## Results:

#### 1. Josh uploaded all results to the following location: 
    ```
    ~/share/jcm385/aoe23/results

    ```
    
#### 2. I copied the filed to my working home directory and used the following resources to complete my project. 
       
1. Directory: `omics_aoe23/project`
       
2. Jupyter Notebook: `notebook_analysis_final.ipynb`
        
3. TPM File: `salmon.merged.gene_tpm.tsv`
        
4. Counts_Scaled file: `salmon.merged.gene_counts_scaled.tsv`     
        
5. Enrichr: For pathway analysis
        
6. PPT used to display final results for class

***

## Discussion: 

Given that I wanted to compare ADA overexpression vs. control CAR_T cells, this was a challenge with an n of 2. However there were some key representations of my data that I was able to accomplish working through a jupyter notebook that was originally used in class. Below are some highlights, however see full notebook for all data. 
- My PCA analysis showed that the biggest difference was between donors highlighting the need for additional samples (however--regardless I proceeded to look at genes of interest.)
- I was able to use python to generate visualizations of my data with the following outputs:
    - PCA
    - Barplot/stripplot with sns
    - heatmaps of genes of interest 
    - Volcano plot and scatter plot with LOG2FC and Bh-pvalues
- Overall, there was no meaningful pathway analysis when I put my exported subsets of genes into enrichr, which was to be expected. 
- In order to further my analysis I would like to adjust for donor differences, and include many more donors to look for meaningful changes in the transcriptome. 
    
***

## Conclusion: 

The key takeaways from this class were how to work with nf core and go from raw fasta file to a count table of differentially expressed genes and then finally uplaod that into enrichr. While this analysis did not show me meaningful results--I was able to use the skills learned in this class to do a practice workflow with data that I am interested in. 

***

## References:
 
Klysz, D.D., et al., Inosine induces stemness features in CAR-T cells and enhances potency. Cancer Cell, 2024. 42(2): p. 266-282.e8.
