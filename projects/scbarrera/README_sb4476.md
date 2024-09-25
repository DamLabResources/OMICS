#Project: Knockout CRISPR Screen Determining Important Genes for HIV-1 Latency Reversal

### Introduction: This project will utilize data from a CRISPR knockout screen publication. Investigating host genes required for the reversal of HIV-1 latency.

### Screen Data: J-Lats (latently infected T cells) were tranduced with a lentiviral vector containing library of sgRNAs targeting genes of interest & flanked by a Ψ-packaging signal. This signal allows sgRNAS to be packaged into budding virions. Cells were treated with activating doses of LRAs (latency reactivating agents). Sequence both the supernatant containing sgRNAs vs. gDNA knockout pool. 

### Literature Review

### Methodology:
1. Proper mapping of reads
2. Comparing the genes that I determine as important for JIV-1 latency reversal are the same as the paper.

### Expected Results: Genes required for reactivation from latency will be depleted in the viral supernatant and not in the genomic knockout pool. The study determined CCNT1 as important. While HIV-1 Tat viral protein binding sites are conserved in CCNT1 and CCNT2, CCNT1-Tat complex can bind with the viral TAR RNA in order to recruit P-TEFb to the LTR.

### Discussion:

### Conclusion:

### References      


# Assignments:
Notes week 04:
Took fastq files from paper dataset and uploaded them in the share directory to sb4476 directory via command:
jupyter-sb4476@Mistake-Not:~/share/sb4476$ 
fasterq-dump -p SRR25648794
-	p is used to show progress
-	SRR25648794 is the accession number

Selected:
SRR25648800 – Jlat10.6  Treatment AZD5582
SRR25648801 – Jlat10.6 Treatment DMSO
SRR25648808 - Jlat10.6  Treatment AZD5582
SRR256488 - Jlat10.6 Treatment DMSO


Notes Week 05:
-	Compressed files in share/sb4476 via:
gzip SRR25648800_LRA.fastq SRR25648801_DMSO.fastq SRR25648808_LRA.fastq SRR25648809_DMSO.fastq

-	checked the du -h to check how much of the drive is being used to make sure files zipped

-	delete unzipped files


Demultiplexing description: Due to the design of most NGS systems each flowcell is single-use and produces a constant number of sequence reads.
`Multiplexing` is a common technique in NGS sequencing practice to get the most out of each run.
If you don't need all 5M reads for a single sample, you can `multiplex` multiple samples into the same sequencing run.

This is accomplished by adding a short & unique _barcode_ to each sample during the library preparation stage.
Then, each sample is pooled in equimolar ratios and sequenced on the same flowcell.
After sequencing, one can examine the _barcode_ and attribute each read to the specific sample.
This process is called `demultiplexing`.


First get stats for sequencing files and write to new file:
jupyter-sb4476@Mistake-Not:~/repos/OMICS/content/wk05$ seqkit stats data/multiplexed.* -T > solution/muxed.stats.tsv

In order to demultiplexed and pull out sequences that we are selecting based on barcode from fastq files:

Utilize the .csv file which contains sample name and also the 5’ and 3’ end barcode for the sequence we want to pull out
-	jupyter-sb4476@Mistake-Not:~/repos/OMICS/content/wk05$ seqkit grep -r -s -p 'ACCT,CCAG' data/multiplexed.fq > solution/SRR23803536.fastq
-	jupyter-sb4476@Mistake-Not:~/repos/OMICS/content/wk05$ seqkit grep -r -s -p 'ACCT,TCAG' data/multiplexed.fq > solution/SRR23803537.fastq
-	jupyter-sb4476@Mistake-Not:~/repos/OMICS/content/wk05$ seqkit grep -r -s -p 'CTGC,CCAG' data/multiplexed.fq > solution/SRR23803538.fastq
-	jupyter-sb4476@Mistake-Not:~/repos/OMICS/content/wk05$ seqkit grep -r -s -p 'CTGC,TCAG' data/multiplexed.fq > solution/SRR23803539.fastq

-	Trim off the adapters from the ends of the seqs

-	Jupyter-sb4476@Mistake-Not:~/repos/OMICS/content/wk05$ seqkit amplicon -F ACCT -R CCAG -r 5:-5 solution/SRR23803536.fastq > solution/SRR23803536.trimmed.fastq.gz
[INFO] 1 primer pair loaded
jupyter-sb4476@Mistake-Not:~/repos/OMICS/content/wk05$ head solution/SRR23803536.trimmed.fastq.gz
@3024
AATATATAGTCTAGCGCTTTACGGAAGACAATGTATGTATTTCGGTTC
+
CCCCC;CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
@4100
GTCGAGGTTATATGATCTCTTTTCCGTCTTTTTACCGATT
+
CCCCCCCCCCCCCCC;CCCCCCCCCCCCCCCCCCCCCCCC
@D00468:259:HYKTMBCX2:1:1101:11391:18698
TCCAAATTTCTGGTTGAGAACAAGAGCAAGAATACAGAGGGGG

Not sure if the 3' end was trimmed correctly... stopped here