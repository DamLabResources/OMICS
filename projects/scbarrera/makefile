DIR_PROJ := /home/jupyter-sb4476/projects/sbCRISPRSCREEN
DIR_READ := $(DIR_PROJ)/01.reads
DIR_20NT := $(DIR_PROJ)/02.reads_20nt
#$(DIR_PROJ)/02.reads_20nt/SRR25648809_DMSO_20nt.fastq
REF := $(DIR_PROJ)/00.ref/HS.GRCh38

#LRA is latenct reversal agent treatment
#DMSO is control no treatment
READ_LRA00 := $(DIR_READ)/SRR25648800_LRA.fastq.gz
READ_DMSO01 := $(DIR_READ)/SRR25648801_DMSO.fastq.gz
READ_LRA08 := $(DIR_READ)/SRR25648808_LRA.fastq.gz
READ_DMSO09 := $(DIR_READ)/SRR25648809_DMSO.fastq.gz

# Make target which extracts 20bp protospacer (x20) from reads for each file
x20: $(READ_LRA00)
	seqkit subseq -r 33:52 $(READ_LRA00) | seqkit seq -s > $(DIR_20NT)/SRR25648800_LRA_20nt.fasta
	ls -l $(DIR_20NT)
	head $(DIR_20NT)/SRR25648800_LRA_20nt.fasta
