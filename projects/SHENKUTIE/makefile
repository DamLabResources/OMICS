REF_DIR := /data/share/refs/pfalciparum
REF_FNA := $(REF_DIR)/GCF_000002765.6_GCA_000002765_genomic.fna.gz
REF_GTF := $(REF_DIR)/GCF_000002765.6_GCA_000002765_genomic.gtf.gz
REF_GFF := $(REF_DIR)/GCF_000002765.6_GCA_000002765_genomic.gff.gz
REF: REF_DIR/$(REF_FNA)
SEED := 100 
READ_DIR := ~/share/ts3576/myproject/

ref: refs/$(REF_FNA)

refs/$(REF_FNA): $(REF)	
	ln -s $(REF) refs

refs/$(REF_FNA).ERR4620265: refs refs/$(REF_FNA)
	bwa index refs/$(REF_FNA)

refs: 
	mkdir refs

refidx: refs/$(REF_FNA).ERR4620265


stats: 
	seqkit stats $(READ_DIR)/ERR4620265_*.fastq.gz
	seqkit stats $(READ_DIR)/ERR4620277_*.fastq.gz

stats100k: 
	seqkit stats ERR4620265_*.fastq.gz
	seqkit stats ERR4620277_*.fastq.gz

subsample: 
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/ERR4620265_1.fastq.gz |seqkit head -n 100000 -o ERR4620265_1.fastq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/ERR4620265_2.fastq.gz |seqkit head -n 100000 -o ERR4620265_1.fastq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/ERR4620277_1.fastq.gz |seqkit head -n 100000 -o ERR4620277_1.fastq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/ERR4620277_2.fastq.gz |seqkit head -n 100000 -o ERR4620277_2.fastq.gz

align: 
	bwa mem refs/$(REF_FNA) ERR4620265_* > ERR4620265.sam 
	bwa mem refs/$(REF_FNA) ERR4620277_* > ERR4620277.sam 
	
	
