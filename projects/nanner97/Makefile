## this is my project makefile

REF_DIR := ~/OMICSProject/genomes
REF_FA := ~/OMICSProject/genomes/Jlat106_GRCH38.fa.gz #from class pc
REF_GFF := ~/OMICSProject/genomes/Jlat106.gff #from class pc
DATA_DIR := ~/OMICSProject/project
OUT_DIR := ~/OMICSProject/project/output
REF_BED := ~/OMICSProject/genomes/Jlat106.bed
PROJ_CSV := ~/OMICSProject/project/atac.csv
MACS := 3100000000
READ := 100

test:
	~/nextflow

run_updated:
	~/nextflow run \
		nf-core/atacseq \
		--input ~/OMICSProject/project/atac.csv \
		--outdir ~/OMICSProject/project/output \
		--fasta $(REF_FA) \
		--gff $(REF_GFF) \
		--bed $(REF_BED) \
		--read_length 100 \
		--with_control \
		--max_cpus 11 \
		--max_memory 31.GB \
		-profile docker \
		--macs_gsize 3100000000 \
		-with-trace \
		-with-report \
		-resume

run_resume:
	~/nextflow run \

dumb_test:
	~/touch dtfile.txt \
