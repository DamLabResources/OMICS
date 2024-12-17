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
ls -la
# locate .condarc
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
Re-ran the test and it made a little more progress, but then list the same error message. So I found viewed the .nextflow.log file to see what was wrong at line 768:
```bash
cd ~/.nextflow/assets/nf-core/atacseq/./workflows/
ls -al
cat atacseq.nf
cat -n atacseq.nf
# saw that line 768 error was related to adding my email
cd ~/repos/OMICS/projects/ceg327/
ls
nextflow run nf-core/atacseq -profile test,conda --outdir ./results --macs_gsize 2700000000 -resume
# removed '--email ceg327@drexel.edu'
```
Made a little more progress, then got the following error message:
```plaintext
Pipeline completed with errors-
ERROR ~ Error executing process > 'NFCORE_ATACSEQ:ATACSEQ:MERGED_LIBRARY_ATAQV_ATAQV (OSMOTIC_STRESS_T100_SE_REP1)'

Caused by:
  Process `NFCORE_ATACSEQ:ATACSEQ:MERGED_LIBRARY_ATAQV_ATAQV (OSMOTIC_STRESS_T100_SE_REP1)` terminated with an error exit status (127)

Command executed:
  ataqv \
      --ignore-read-groups \
      --mitochondrial-reference-name MT \
      --peak-file OSMOTIC_STRESS_T100_SE_REP1.mLb.clN_peaks.broadPeak \
      --tss-file genes.tss.bed \
       \
      --autosomal-reference-file genome.fa.autosomes.txt \
      --metrics-file "OSMOTIC_STRESS_T100_SE_REP1.ataqv.json" \
      --threads 2 \
      --name OSMOTIC_STRESS_T100_SE_REP1 \
      NA \
      OSMOTIC_STRESS_T100_SE_REP1.mLb.mkD.sorted.bam
  
  cat <<-END_VERSIONS > versions.yml
  "NFCORE_ATACSEQ:ATACSEQ:MERGED_LIBRARY_ATAQV_ATAQV":
      ataqv: $( ataqv --version )
  END_VERSIONS

Command exit status:
  127

Command output:
  (empty)

Command error:
  ataqv: error while loading shared libraries: libboost_filesystem.so.1.85.0: cannot open shared object file: No such file or directory

Work dir:
  /home/jupyter-ceg327/repos/OMICS/projects/ceg327/work/8c/acf7e67958659c10ba0587fd01d427

Tip: when you have fixed the problem you can continue the execution adding the option `-resume` to the run command line

 -- Check '.nextflow.log' file for details
```

### 4. Results

###  5. Discussion

### 6. Conclusion

### 7. References 




