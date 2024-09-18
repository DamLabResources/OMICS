DIROUT := /data/share/dk497

hello_nix:
	echo $(HOSTNAME) HAS `nproc --all` CPU-CORES

# Download FASTQ files from RNA-seq single cell Illumina HiSeq 4000 reads
# https://www.ncbi.nlm.nih.gov/sra?term=SRX21898392
# https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump
# https://github.com/ncbi/sra-tools/wiki/08.-prefetch-and-fasterq-dump
SRR := SRR26186565
#SRR := SRR000001
download:
	vdb-dump --info $(SRR)
	prefetch $(SRR) --output-directory $(DIROUT)/$(SRR)
	fasterq-dump -p $(SRR) -t /tmp/dk497 --outdir $(DIROUT)/$(SRR)
	find $(DIROUT)/$(SRR)

