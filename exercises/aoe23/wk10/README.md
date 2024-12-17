# Week 10 Assignment: Arden Edgerton

## Assignment Instructions: 

1. Adjust the makefile to run on the full or mini directory. 
2. Then, create the gene expression matrix for each grouping and place them in your exercises folder with a Readme describing the changes you made.

***

## Part 1: Adjust the make file to run on the full or mini directory

1. I first went through the steps we took in class to remake the quants folders that were generated during the in class lecture to refresh myself on the commands and make sure that I had the correct starting material. 

    `cd omics/aoe23/wk10`
    `mkdir quants`
    `nano makefile.og`
    
2. This make file og has the simplest commands that we used in class so that I could break down the steps more simply for myself. Given that I was getting error messages I used this to first focus on the mini ONLY. Also I changed the references to fastq to fastq.gz so that the were references the appropriate files within the source folder. (Contents of makefile.og below)

```bash
REF=/data/share/refs/SGD/salmonindex
SOURCE=/data/share/OMICS/wk10/mini


quants/%: $(SOURCE)/%_1.fastq.gz $(SOURCE)/%_2.fastq.gz
	salmon quant -i $(REF) -l A -1 $(SOURCE)/$*_1.fastq.gz -2 $(SOURCE)/$*_2.fastq.gz --validateMappings -o $@
```


3. ALthough we worked through a makefile that could make all at once I went through one by one for all of the mini folder using the commands: 

    `make -f  makefile.og quants/SRR24466374`
4. Repeated for each SRR file that I had iteratively. Note that once it was complete I had a folder for each MINI within the quants folder. 

5. Because I wanted to repeat this for full I then renamed this previously used quants folder to quants.mini and renamed the makefile that was previously named makefile.og to makefile.mini

6. To now use this iterative process to make quants for each of the full SRR's I first made a new quants directory, then I made a new make file called makefile.og.full
    `mkdir quants.full`
    `nano makefile.og.full2`
    
7. The contents for makefile.og.full is now edited to reference the full folder in week 10 (edited in source) and also put the output in the quants.full folder. See the contents below: 

```bash
REF=/data/share/refs/SGD/salmonindex
SOURCE_FULL=/data/share/OMICS/wk10/full
SOURCE_MINI=/data/share/OMICS/wk10/mini

# Update the quant output directory
QUANT_DIR = quants.full

# Collect the available FASTQ files for processing from both directories
FASTQ_FILES_FULL := $(wildcard $(SOURCE_FULL)/*_1.fq.gz)
FASTQ_FILES_MINI := $(wildcard $(SOURCE_MINI)/*_1.fastq.gz)

# Define the quantification targets based on the FASTQ files
QUANT_DIRS := $(patsubst $(SOURCE_FULL)/%_1.fq.gz,$(QUANT_DIR)/%,$(FASTQ_FILES_FULL))
QUANT_DIRS += $(patsubst $(SOURCE_MINI)/%_1.fastq.gz,$(QUANT_DIR)/%,$(FASTQ_FILES_MINI))

# Rule for all quantification
all: $(QUANT_DIRS)

# Rule for generating quantification from full directory
$(QUANT_DIR)/%: $(SOURCE_FULL)/%_1.fq.gz $(SOURCE_FULL)/%_2.fq.gz
	mkdir -p $(QUANT_DIR)  # Ensure the output directory exists
	salmon quant -i $(REF) -l A -1 $(SOURCE_FULL)/$*_1.fq.gz -2 $(SOURCE_FULL)/$*_2.fq.gz --validateMappings -o $@

# Rule for generating quantification from mini directory
$(QUANT_DIR)/%: $(SOURCE_MINI)/%_1.fastq.gz $(SOURCE_MINI)/%_2.fastq.gz
	mkdir -p $(QUANT_DIR)  # Ensure the output directory exists
	salmon quant -i $(REF) -l A -1 $(SOURCE_MINI)/$*_1.fastq.gz -2 $(SOURCE_MINI)/$*_2.fastq.gz --validateMappings -o $@
```


10. In a separate terminal I went back into my folder to run this again.

    `cd omicsaoe23/wk10/wk10_homework`
    
    `make -f makefile.og.full2`
    
11. Now I have a quants.full folder and a quants.mini folder for each that works appropriately. (NOTE: this step took a long time to run, when I do this for my project, remember that this will probably take a while)

*** 

## Part 2: Create the gene expression matrix for each grouping and place them in your exercises folder. 


1. make sure pandas installed


2. Python Script to Create Gene Expression Matrices:

    `nano gene_expression_matrix.py`
    
3. After making the place to write the script, I included the following code below:

```bash 

import os
import pandas as pd

# Define directories
quants_mini_dir = '/path/to/quants.mini'
quants_full_dir = '/path/to/quants.full'
output_dir = '/path/to/exercises'

# Function to read quant.sf files and create a gene expression matrix
def create_expression_matrix(dir, group_name):
    quant_files = [f for f in os.listdir(dir) if f.endswith("quant.sf")]
    gene_expr_data = []

    for file in quant_files:
        file_path = os.path.join(dir, file)
        # Read the quant.sf file
        data = pd.read_csv(file_path, sep='\t')  # Specify the separator if needed
        # Extract necessary columns
        data = data[['Name', 'TPM']]
        data['Sample'] = os.path.basename(dir)  # Adding a column for the sample name
        data.columns = ['Gene', 'Expression', 'Sample']  # Rename columns for clarity
        gene_expr_data.append(data)

    # Combine all data into a single DataFrame
    combined_data = pd.concat(gene_expr_data)
    # Save the matrix to a CSV file
    output_file = os.path.join(output_dir, f'gene_expression_matrix_{group_name}.csv')
    combined_data.to_csv(output_file, index=False)

# Create matrices for both mini and full
create_expression_matrix(quants_mini_dir, 'mini')
create_expression_matrix(quants_full_dir, 'full')

```

4. Then return to the command line to run the python script: 

    `python ~/path/to/gene_expression_matrix.py`


5. Then I loaded the gene expression matrices into this experiments folder. 