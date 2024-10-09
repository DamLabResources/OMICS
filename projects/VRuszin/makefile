DIROUT := /data/share/vr433

hello:
	echo $(DIROUT)

all: SRR26186566/SRR26186566.sra

# Download FASTQ files from RNA-seq single cell Illumina HiSeq 4000 reads
# https://www.ncbi.nlm.nih.gov/sra?term=SRX21898392
# https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump
#fetch and fastq-dump download:
download:
	fasterq-dump -p SRR26186565 --outdir $(DIROUT)

# https://github.com/ncbi/sra-tools/wiki/08.-prefetch-and-fasterq-dump
SRR26186566/SRR26186566.sra:
	prefetch SRR26186566

download:
	 fasterq-dump -p SRR26186566 --outdir SRR26186566
