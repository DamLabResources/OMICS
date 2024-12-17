# Week 12 Homework Edgerton

***
## 2024-11-04 In Class Notes

### Copy Data and Will's Notebook into home folder:
1. In class: We first copied the data to home directory so that we can all work on it simultaneously
    `cd omics_aoe23/`
     `mkdir wk12`
     `cd wk12`
     `cp -r  ~/share/OMICS/wk12* . `
     `tree`

2. Note that README in wk12 content folder has simple breakdowns for each visualization and use this reference to tell which statistics to use: 
    https://pingouin-stats.org/build/html/guidelines.html
    
3. Copy Will's Python Lecture Workbook into my folder for referencing/so that I can make changes/notes while working in class. 
    `cp -r  ~/repos/OMICS/content/wk12* .`

### In Class Adjustments made to Will's Walkthrough/Notes

1. Normalizing Data: Heatmap normalization mu = average value of each gene

First do the math to make all of the means = 0
cols = ['gene 1, gene 2, gene 3']
mu = rna_matrix.loc [cols].mean(axis=1)
(rna_matrix.loc[cols].T-mu)

Now you have it adjusted to mean = 0 for each and then you need to divide by the standard deviation: 
std = rna_matrix.loc[cols].std(axis=1)
unit_normed = (rna_matrix.loc[cols].T-mu)/std

To put it all together: 
sns.clustermap(unit_normed.T)

**All code together:**
mu = rna_matrix.loc [cols].mean(axis=1)
std = rna_matrix.loc[cols].std(axis=1)
unit_normed = (rna_matrix.loc[cols].T-mu)/std

**Now each unit is one standard deviation of the data: so this will show warm colors = high std dev over the mean, and cool = low std deviation over the mean. 

2. Lineaer Models

This is critical so that we can look at all of our samples at once. This is a specific way that we can consider each of thse variables together. 
If we had only pairwise we could only look at:
    - ctrl vs stim
    - ctrl vs stim time 2 
    - ctrl vs tat
    - ctrl vs stim tat 
    - HOWEVER...if we want to cnsider all of these sampeles together use linear regression!

Key things to keep track of: 
- degrees of freedom
- number of samples that you have


Ideally you want 10X of samples to degrees of freedom. Lowest acceptable is 2. 

Given that we have degree of freedom: 7, we would want ideally 14-70+ samples. Less than 14 not acceptable
        The regression had 7 degrees of freedom and there were 24 samples.

**OUTPUT**
bash```
These effects were determined.
Name                                              Significant Genes
Stim[T.Yes]                                       1039
Stim[T.Yes]:Tat[T.Tat50]                          12
Tat[T.Tat250]                                     3
Tat[T.Tat50]                                      17
timepoint[T.6X]                                   1336
timepoint[T.6X]:Stim[T.Yes]                       832
timepoint[T.6X]:Tat[T.Tat50]                      10
```