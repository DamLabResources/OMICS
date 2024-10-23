REF_DIR := /data/share/refs/hgjlat
REF_FA := $(REF_DIR)/Jlat106_GRCH38.fa.gz
REF_GFF := $(REF_DIR)/Jlat106.gff3
DATA_DIR := /data/share/ceg327

## This is my project makefile

test:
	nextflow

# To-do: update
gzip:
	gzip SRR*.fastq

run_pipeline:
	mkdir -p results
	nextflow run \
		nf-core/atacseq \
		--input ./ATACseq_data.csv \
		--outdir ./results \
		--fasta $(REF_FA) \
		--gff $(REF_GFF) \
		--read_length 150 \
		-profile conda

## info from nf-core on custom reference genomes using nf-core/rnaseq as an example

dirs:
	find $(REF_DIR)
	find $(DATA_DIR) -name '*.fastq.gz'


save_reference:
	nextflow run \
    	nf-core/rnaseq \
   	--input samplesheet.csv \
    	--fasta Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa.gz \
    	--gtf Homo_sapiens.GRCh38.108.gtf.gz \
    	--save_reference \
    	<OTHER_PARAMETERS>
