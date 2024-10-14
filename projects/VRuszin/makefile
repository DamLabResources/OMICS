DIROUT := /data/share/vr433
VER_ENSEMBL := 112
DIR_HS := /data/share/refs/HS.GRCh38

hello:
	echo $(DIROUT)
	ls -l $(DIR_HS)

all: SRR26186566/SRR26186566.fastq

# Download FASTQ files from RNA-seq single cell Illumina HiSeq 4000 reads
# https://www.ncbi.nlm.nih.gov/sra?term=SRX21898392
# https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump
#fetch and fastq-dump download:
download:
	fasterq-dump -p SRR26186565 --outdir $(DIR)
  
# https://github.com/ncbi/sra-tools/wiki/08.-prefetch-and-fasterq-dump
SRR26186566/SRR26186566.sra:
	prefetch SRR26186566

SRR26186566/SRR26186566.fastq: SRR26186566/SRR26186566.sra
	 fasterq-dump -p SRR26186566 --outdir SRR26186566

# -------------------------------------------------------------------
# Download human genome reference
#
refs: ${DIR_HS}/Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa.gz ${DIR_HS}/Homo_sapiens.GRCh38.$(VER_ENSEMBL).gtf.gz
	find ${DIR_HS}
	ls -l ${DIR_HS}

gtf:{DIR_HS}/Homo_sapiens.GRCh38.$(VER_ENSEMBL).gtf.gz
	find ${DIR_HS}
	ls -l ${DIR_HS}

${DIR_HS}:
	mkdir -p $@

${DIR_HS}/Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa.gz: Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa.gz ${DIR_HS}
	mv $< ${DIR_HS}

${DIR_HS}/Homo_sapiens.GRCh38.$(VER_ENSEMBL).gtf.gz: Homo_sapiens.GRCh38.$(VER_ENSEMBL).gtf.gz ${DIR_HS}
	mv $< ${DIR_HS}

Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa.gz:
	wget -L ftp://ftp.ensembl.org/pub/release-$(VER_ENSEMBL)/fasta/homo_sapiens/dna/$@

Homo_sapiens.GRCh38.$(VER_ENSEMBL).gtf.gz:
	wget -L ftp://ftp.ensembl.org/pub/release-$(VER_ENSEMBL)/gtf/homo_sapiens/$@

# -------------------------------------------------------------------
clobber:
	rm -rf ${DIR_HS}
