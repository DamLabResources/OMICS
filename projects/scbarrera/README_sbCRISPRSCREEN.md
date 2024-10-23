This README is for CRISPR Screen Project Details Only

# Project: Knockout CRISPR Screen Determining Important Genes for HIV-1 Latency Reversal

### Project Introduction: 
This project will utilize data from a CRISPR knockout screen publication. Investigating host genes required for the reversal of HIV-1 latency.

### Literature Hypothesis:
Host factors (HIV dependency factors) required for HIV-1 replication also play a role in latency reversal (reactivation)

### Literature Goal:
To identify proteins whose function is more important for HIV-1 reactivation than normal T-cell biology.

### Screen Data: 
- I will be utilizing reads from J-Lat 10.6 cells treated with AZD5582 or DMSO (control) and compare them to each other and to the literature results.
- AZD5582 is a Latency Reversal Agent (LRA) (1nM treatment)
- J-Lats (latently infected T cells) were tranduced with a lentiviral vector containing library of sgRNAs targeting genes of interest & flanked by a Ψ-packaging signal. 
- This signal allows sgRNAS to be packaged into budding virions. 
- Cells were treated with activating doses of LRAs. 
- Authors sequenced both the supernatant containing sgRNAs vs. gDNA knockout pool. 
- I will not be utilizing all cell types from the literature: HEK293T cells, J-Lat 10.6 and J-Lat 5A8 previously knocked out for ZAP, primary CD4+ T cells


### Literature Review

### Project Methodology:
1. Proper mapping of reads
2. Comparing the genes that I determine as important for HIV-1 latency reversal are the same as the literature.

### Project Expected Results: 
- From the literature, genes required for reactivation from latency will be depleted in the viral supernatant and not in the genomic knockout pool. 
- Therefore, I should be able to identify the factors important in latency reactivation that were identified and validated in the literature that were treated with AZD5582.
- These may include the following genes:
    - ELL1
    - TBL1XR1
    - UBE2M
    - HDAC3
    - AMBRA1
    - ALYREF
    - Cyclin T1 (CCNT1) - labeled important
        - Forms the P-TEFb transcriptional elongation complex with Cyclin-dependent Kinase 9 (CDK9), was the top hit in two J-Lat models in their screen.
        - While HIV-1 Tat viral protein binding sites are conserved in CCNT1 and CCNT2, CCNT1-Tat complex can bind with the viral TAR RNA in order to recruit P-TEFb to the LTR.

### Discussion:
### Conclusion:
### References      


# Project Methods:
### 1. UPLOAD DATASET FROM PUBLICATION INTO COMPUTER-WORKING DIRECTORY (RAW READS FASTQ FILES):
Took fastq files from paper dataset and uploaded them in the projects/sbCRISPRSCREEN/reads directory via command:
`jupyter-sb4476@Mistake-Not:~/projects/sbCRISPRSCREEN/reads$ 
fasterq-dump -p SRR25648794`
- p is used to show progress
- SRR25648794 is the accession number
  
Selected the following fastq files from:
Paper Link: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10535513/
NCBI Project Acccession #: GSE240894
NCBI Project data link: https://www.ncbi.nlm.nih.gov/Traces/study/?acc=PRJNA1005659&o=acc_s%3Aa

Fastq files:
SRR25648800 – Jlat10.6  Treatment AZD5582
SRR25648801 – Jlat10.6 Treatment DMSO
SRR25648808 - Jlat10.6  Treatment AZD5582
SRR256488 - Jlat10.6 Treatment DMSO

### 2. COMPRESS FASTQ FILES
Compressed files in ~/projects/sbCRISPRSCREEN/reads via command:
`gzip SRR25648800_LRA.fastq SRR25648801_DMSO.fastq SRR25648808_LRA.fastq SRR25648809_DMSO.fastq`

Check the `du -h` to check how much of the drive is being used to make sure files zipped.

Delete unzipped files to make space if they weren't already.

### 3. GET STATS ON DATASET FILES (READS) 
Get statisatics from fastq files and write to new file in tsv format:
`jupyter-sb4476@Mistake-Not:~/projects/sbCRISPRSCREEN/reads$ 
seqkit stats *.gz -T > muxed.stats.tsv`

- -T = tabular format; if do not use -T then it will output in fixed width which is not useable 
- Note that since files have already been zipped seqkit works on the .gz files as it would the fastq files.
- These files are multiplexed files & have not been demultiplexed yet.

OUTPUT RESULTS: 
| file                      | format | type    | num_seqs| sum_len    | min_len | avg_len | max_len |
|---------------------------|--------|---------|---------|------------|---------|---------|---------|
| SRR25648800_LRA.fastq.gz  | FASTQ  | DNA     | 6054549 | 363272940  | 60      | 60.0    | 60      |
| SRR25648801_DMSO.fastq.gz | FASTQ  | DNA     | 6272376 | 376342560  | 60      | 60.0    | 60      |
| SRR25648808_LRA.fastq.gz  | FASTQ  | DNA     | 5511386 | 330683160  | 60      | 60.0    | 60      |
| SRR25648809_DMSO.fastq.gz | FASTQ  | DNA     | 5508393 | 330503580  | 60      | 60.0    | 60      |

- All 4 files have DNA reads that are 60 nucleotides in length with about 5.5million to 6.2 million sequences and a total # of bases ranging from 330 million to 363 million.


### 4. DEMULTIPLEX READS IF NECESSARY
Break up each read from fastq files and pull out sequences based on its barcode via seqkit grep. 
Will first need the 5' and 3' end barcode for the sequences we want to pull out.
This should be in a .csv file will contains the sample name and the barcode sequences.
For this data set the barcodes are.....?

Demultiplexing files via seqkit grep:
`add command here`


- Demultiplexing description: 
Due to the design of most NGS systems each flowcell is single-use and produces a constant number of sequence reads. 
Multiplexing is a common technique in NGS sequencing practice to get the most out of each run.
If you don't need all 5M reads for a single sample, you can multiplex multiple samples into the same sequencing run.
This is accomplished by adding a short & unique _barcode_ to each sample during the library preparation stage.
Then, each sample is pooled in equimolar ratios and sequenced on the same flowcell.
After sequencing, one can examine the _barcode_ and attribute each read to the specific sample.
This process is called demultiplexing.


### 5. TRIM OFF THE (BARCODES) ADAPTERS FROM THE ENDS OF THE SEQS IF HAVE NOT BEEN DONE ALREADY
There are various ways to do this but can utilize seqkit replace or seqkit amplicon:
`add command here` 


- Use `seqkit head FileName` to check the first couple of reads vs. just head which will give you the first couple of lines not whole reads
  
  
### CRISPR SCREEN PIPELINE TO LOOK AT GRNAS MAPPED TO THE HUMAN GENOME
- This pipeline will be different from what is available on [nf-core](https://nf-co.re/)
- I will be mapping gRNAs to the human genome 

- Obtain reference human genome and index and create .fai file
Copied contents from shared folder:
`jupyter-sb4476@Mistake-Not:
~/projects/sbCRISPRSCREEN/ref$ ln -s /data/share/refs/HS.GRCh38/ .`

- Index the reference genome if not already done so via `bwa index`:  
`jupyter-sb4476@Mistake-Not:~/projects/sbCRISPRSCREEN/ref/HS.GRCh38$ bwa index filename`

- This will create files within the same folder as the reference file

- To create a fa.fai file for the reference to use in IGV can use samtools. Tehnicially don't need this:  
`samtools faidx filename`
