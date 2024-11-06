# Week 12 Homework Edgerton

## Key notes from in class that help with assignment

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



3. Heatmap normalization mu = average value of each gene

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