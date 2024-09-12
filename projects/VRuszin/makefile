DIROUT := share/vr433


# Download FASTQ files from RNA-seq single cell Illumina HiSeq 4000 reads
# https://www.ncbi.nlm.nih.gov/sra?term=SRX21898392
# https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump
download:
	fasterq-dump -p SRR26186565 --outdir $(DIROUT)
