This README is for CRISPR Screen Project Details

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
- For the purpose of this project I will not be utilizing all cell types from the literature: (HEK293T cells, and J-Lat 5A8 previously knocked out for ZAP, primary CD4+ T cells)


### Project Methodology:
1. Proper extraction and counts of protospacer reasds
2. Comparing that the top 5 genes that I determine as important for HIV-1 latency reversal are the same as the literature.

### Project Expected Results: 
- From the literature, genes required for reactivation from latency will be depleted in the viral supernatant and not in the genomic knockout pool. 
- Therefore, I should be able to identify the top 5 factors important in latency reactivation that were identified and validated in the literature that were treated with AZD5582. Because I am working with less samples and not all the LRA treatments, as well as a different method from the paper I expect I may also get different factors/ genes that did not come up as their top hits.
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
  
### My Screen Results:
- I was able to get the top 5 from each of the samples but note I was unable to combine them and see their log2. My results prior to this last step was the following genes were in the top 5 for both the control and the LRA treated cells:
    - BAP1	Deubiquitination/ tumor suppressor
    - KDM4B	Encodes lysine demethylase
    - EMP3	Formation of the sheath of compact myelin
    - NCL	Chromatin remodeling, transcription of rRNA, rRNA maturation, ribosome assembly, nucleocytoplasmic transport
    - ERFL	Predicted to enable DNA-binding transcription factor activity
    - PYG02	Enables chromatin binding activity; histone acetyltransferase regulator activity; and histone binding activity
    - ARVCF	Encodes a protein that plays a role in the formation of adherens junctions
  
  
### Conclusion:
- We were able to get the counts for all gRNAs. Using the threshold for clusterer appeared to have halved the amount of possible gRNAs. Adding the threshold for Casoffinder as well by no more than 2 also decreased the amount of gRNAs. We see the same genes for both the treated and control DMSO samples. This isn't surprising since I needed the last step to compare all and not just pull out the top 5. It also would mean that those genes needed for T cell function would also be needed in latency reactivation. Moving forward I will need to make that comparison with all the samples and plot the log2 in a volcano plot to see the top hits.
     


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
This step was not needed for the data set downloaded from literature.
  

### 5. TRIM OFF THE (BARCODES) ADAPTERS FROM THE ENDS OF THE SEQS IF HAVE NOT BEEN DONE ALREADY
There are various ways to do this but can utilize seqkit replace or seqkit amplicon. This step was already done to the file.
  
- Use `seqkit head FileName` to check the first couple of reads vs. just head which will give you the first couple of lines not whole reads
  
  
### 6. CRISPR SCREEN PIPELINE TO LOOK AT GRNAS MAPPED TO THE HUMAN GENOME
- This pipeline will be different from what is available on [nf-core](https://nf-co.re/) because it is a crispr screen, but the gRNA is delivered in a lentivirus that is integrated into the same genome it is editing. So we need to extract the protospacer sequence within the lentivirus, within the human cell genome because this will represent the gene bc the protospacer is targeting it. We then want the counts of how many times the gene showed up to indicate whether or not it is importnat for latency reversal. 
  
- Since I will be mapping gRNAs to the human genome at the end. Obtain reference human genome and index and create .fai file
Copied contents from shared folder:
`jupyter-sb4476@Mistake-Not:
~/projects/sbCRISPRSCREEN/ref$ ln -s /data/share/refs/HS.GRCh38/ .`

- Index the reference genome if not already done so via `bwa index`:  
`jupyter-sb4476@Mistake-Not:~/projects/sbCRISPRSCREEN/ref/HS.GRCh38$ bwa index filename`

- This will create files within the same folder as the reference file

- If needed create a fa.fai file for the reference to use in IGV can use samtools. Didn't need for this pipeline.  
`samtools faidx filename`

#### Make a makefile that runs python script counting how many times protospacer showed up on all 4 files containing 20nt reads files. WD & DK created. There were raw counts which is each gRNA sequence counted as is and there was UMI-clusterer used to cluster the sequences that are similar with a threshold of 5 nt difference. 
-Makefile name: version2_count_protospacers.py - has been renamed version2_count_protospacers.py
- On command line:  
`(base) jupyter-sb4476@Mistake-Not:~/repos/OMICS/projects/scbarrera$`

- For: SRR25648800_LRA_20nt.csv  
`python sbversion_count_protospacers.py ~/projects/sbCRISPRSCREEN/02.reads_20nt/SRR25648800_LRA_20nt.txt ~/projects/sbCRISPRSCREEN/03.counts_20nt/rawout_SRR25648800_LRA_20nt.csv ~/projects/sbCRISPRSCREEN/03.counts_20nt/clustout_SRR25648800_LRA_20nt.csv`

- For: SRR25648801_DMSO_20nt.csv  
`python sbversion_count_protospacers.py ~/projects/sbCRISPRSCREEN/02.reads_20nt/SRR25648801_DMSO_20nt.txt ~/projects/sbCRISPRSCREEN/03.counts_20nt/rawout_SRR25648801_DMSO_20nt.csv ~/projects/sbCRISPRSCREEN/03.counts_20nt/clustout_SRR25648801_DMSO_20nt.csv`

- For: SRR25648808_LRA_20nt.csv  
`python sbversion_count_protospacers.py ~/projects/sbCRISPRSCREEN/02.reads_20nt/SRR25648808_LRA_20nt.txt ~/projects/sbCRISPRSCREEN/03.counts_20nt/rawout_SRR25648808_LRA_20nt.csv ~/projects/sbCRISPRSCREEN/03.counts_20nt/clustout_SRR25648808_LRA_20nt.csv`

- For: SRR25648809_DMSO_20nt.csv  
`python sbversion_count_protospacers.py ~/projects/sbCRISPRSCREEN/02.reads_20nt/SRR25648809_DMSO_20nt.txt ~/projects/sbCRISPRSCREEN/03.counts_20nt/rawout_SRR25648809_DMSO_20nt.csv ~/projects/sbCRISPRSCREEN/03.counts_20nt/clustout_SRR25648809_DMSO_20nt.csv`
  
- Output in 03.counts_20nt as rawout and clustout in a .csv file
  
#### Take the sequences in the files and format them in a .txt file for Cas-offinder. For the purpose of this project I took the top 6 sequences.
- Output in 04.casoffinder_prep
  
####  Utilize Cas-offinder to align the protospacers with the human genome
- This will match protospacers and also give back protopacers with 2 or less mismatches that are found in the human genome. 
- It will also return the location of where the protospacer is found.
- I utilized a command to do this on command line but the reference directory path kept giving me error so I entered it into the Cas-offinder browser manually.
- Command that did not work:
`cas-ffinder casprep_SRR25648800_LRA.fa C ~/projects/sbCRISPRSCREEN/05,casoffinder_out/casout_SRR25648800_LRA.txt`
- On web browser:
    - threshold=2 mismatches
    - PAM = SpCas9 = NGG
    - Reference genome = Human GRCh38
    
- Output in 05.cas0ffinder_out
  
  
#### Determine names of genes via bedtools - First make a bedfile from Cas-offinder
- Now that we have the location of the gene in the human genome that the protospacers align to we can search for the gene name by intersecting the location of the protospacer/ gene with the annotated file with the gene name via bedtools.
- First we need to convert the cas-offinder output into a simple .bed file with 3 columns
- You can also add an additional 4th column with a label name to be able to find the protospacer that matched and sort it out later
- I had to manually remove the first label line because it wasn't working on command line.
- Make sure .bed file is tab delimited
- Also make sure that bed file has the same chromosome labeling. Ex. both files should say chromosome 1 or just 1
    - I had to edit bed file to remove the “chromosome" and leave numbers, but I could have also addrd "chromosome" to both files instead
    

  
- On command line:
`(base) jupyter-sb4476@Mistake-Not:~/projects/sbCRISPRSCREEN/05.casoffinder_out/counts_added$ 
awk '{print $4, $5, $5 + length($2), $9}' top5cnt_casoffout_SRR25648800_LRA.txt > ~/projects/sbCRISPRSCREEN/06.casoffinder_bed/top5cnt_casoffout_SRR25648800_LRA.bed`

`awk '{print $4, $5, $5 + length($2), $9}' top5cnt_casoffout_SRR25648808_LRA.txt > ~/projects/sbCRISPRSCREEN/06.casoffinder_bed/top5cnt_casoffout_SRR25648808_LRA.bed`

`awk '{print $4, $5, $5 + length($2), $9}' top5cnt_casoffout_SRR25648801_DMSO.txt > ~/projects/sbCRISPRSCREEN/06.casoffinder_bed/top5cnt_casoffout_SRR25648801_DMSO.bed`

`awk '{print $4, $5, $5 + length($2), $9}' top5cnt_casoffout_SRR25648809_DMSO.txt > ~/projects/sbCRISPRSCREEN/06.casoffinder_bed/top5cnt_casoffout_SRR25648809_DMSO.bed`
  
- Explanation:
    - $4: Chromosome name
    - $5: Start position
    - $5 + length($2): End position (calculated by adding guide length to start)
    - $9: Optional name for the off-target site- ex can give it a grna name or label it how many counts etc. so that later on when need to find it you can just grep it
    
     
#### Determine names of genes via bedtools - Second intersect bed file and .gtf file
-  We need to intersect the bedfile with the .gtf file which contains the annotated genome
- On command line:  
`(base) jupyter-sb4476@Mistake-Not:~/projects/sbCRISPRSCREEN/06.casoffinder_bed/rename_chromosome$ 
bedtools intersect -a Homo_sapiens.GRCh38.112.gtf -b rmchr_top5cnt_casoffout_SRR25648800_LRA.bed > ~/projects/sbCRISPRSCREEN/07.bedintersect_out/intersect_SRR25648800_LRA_Homo_sapiens.GRCh38`
- a reference
- b intersecting file
- can add -waoright before writing it to a new file = give name that’s in bed file – in this case I labeled the amount of counts of grna as name ex: Ct3453 but it didn’t show up so I left it alone as is.

`$ bedtools intersect -a Homo_sapiens.GRCh38.112.gtf -b rmchr_top5cnt_casoffout_SRR25648801_DMSO.bed > ~/projects/sbCRISPRSCREEN/07.bedintersect_out/intersect_SRR25648801_DMSO_Homo_sapiens.GRCh38`

`$ bedtools intersect -a Homo_sapiens.GRCh38.112.gtf -b rmchr_top5cnt_casoffout_SRR25648808_LRA.bed > ~/projects/sbCRISPRSCREEN/07.bedintersect_out/intersect_SRR25648808_LRA_Homo_sapiens.GRCh38`

`bedtools intersect -a Homo_sapiens.GRCh38.112.gtf -b rmchr_top5cnt_casoffout_SRR25648809_DMSO.bed > ~/projects/sbCRISPRSCREEN/07.bedintersect_out/intersect_SRR25648809_DMSO_Homo_sapiens.GRCh38`
  
- Output files containing gene names & position in 07.bedintersect_out/intersect_SRR25648800_LRA_Homo_sapiens.GRCh38
  
#### Extract gene name from these files for each protospacer
- I did this manually but it would have been easier to add the label into the bed file originally in the 4th row to identify protospacer and the gene it coincides with.
  
#### Find fold change for each sample
- I couldn't get this to work but its needed since each sample has replicates and this is where stats would come from.


    












