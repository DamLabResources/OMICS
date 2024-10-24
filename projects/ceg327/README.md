## This is the new README file where I describe my OMICS project
### 1. Introduction
This goal of this project is to analyze publicly available ATAC-seq datasets from models of HIV-1 latency for regions of chromatin accessibility across the integrated provirus. This information will be used to determine sites accessible for CRISPR gRNA targeting.

### 2. Literature Review

### 3. Methodology
Bioproject: PRJNA764194

SRA: SRP337615

Run ID		| Run Info
----------------|-------------------------------------------------
SRR15931104	| J-Lat 8.4-ATAC_TNF_rep1; Homo sapiens; ATAC-seq
SRR15931102	| J-Lat 8.4-ATAC_rep1; Homo sapiens; ATAC-seq
SRR15931099	| J-Lat 10.6-ATAC_TNF_rep1; Homo sapiens; ATAC-seq
SRR15931096	| J-Lat 10.6-ATAC_rep1; Homo sapiens; ATAC-seq

Made changes to nextflow atacseq pipeline as detailed in the makefile
```bash
~/repos/OMICs/projects/ceg327/makefile
```
I had to re-install nextflow in my repo, as I couldn't run it from the makefile. 

Next, I had to run the test the pipeline to confirm whether everything is working:
```bash
nextflow run nf-core/atacseq -profile test,conda --outdir ./results
```
Kept getting an error message related to the conda channel configuration, so I reordered the channels by editing the .condarc file located in the home directory:
```bash
conda config --show channels
conda config --remove channels defaults
conda config --remove channels bioconda
conda config --remove channels conda-forge
```
When adding the channels back individually did not work, I reorderd the channels manually in the .condarc file:
```bash
cd ~/
ls -la # locate .condarc
vim .condarc
cd repos/OMICS/projects/ceg327/
conda config --show channels
```
I also added '--macs_gsize 2700000000', to eliminate errors related to the kmers-utilization.

Then, I re-ran the nextflow test:
```bash
nextflow run nf-core/atacseq -profile test,conda --outdir ./results --macs_gsize 2700000000 --email ceg327@drexel.edu -resume
```
Received an error involving matplotlib:
```plaintext
AttributeError: module 'matplotlib.cm' has no attribute 'register_cmap'
```
Upgraded matplotlib to most recent version:
```bash
pip install --upgrade matplotlib
```
Re-ran the test and it made a little more progress, but then list the same error message.

### 4. Results

###  5. Discussion

### 6. Conclusion

### 7. References 




