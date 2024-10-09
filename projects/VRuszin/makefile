DIROUT := /data/share/vr433

hello:
	echo $(DIROUT)

all: SRR26186566

# Download FASTQ files from RNA-seq single cell Illumina HiSeq 4000 reads
# https://www.ncbi.nlm.nih.gov/sra?term=SRX21898392
# https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump
#fetch and fastq-dump download:
download:
	fasterq-dump -p SRR26186565 --outdir $(DIROUT)

SRR26186566:
	prefetch SRR26186566
