## This is my project makefile
### all work was performed in Yawning-Angel

REF_DIR := /deepdata/share/cegunderson/refs #pulled from Mistake-Not
REF_FA := /deepdata/share/cegunderson/refs/Jlat106_GRCH38.fa.gz
REF_GFF := /deepdata/share/cegunderson/refs/Jlat106.gff #cp Jlat106.gff3 Jlat106.gff 
DATA_DIR := /deepdata/share/cegunderson
OUT_DIR := /mnt/local-dvc-cache/data-projects/chelsea/atacseq/results_10292024b
REF_BED := /deepdata/share/cegunderson/refs/Jlat106.bed
REF_TSS := /deepdata/share/cegunderson/refs/Jlat106.tss.bed

test:
	./nextflow

run_updated:
	./nextflow run \
		nf-core/atacseq \
		--input ./ATACseq_data.updated.csv \
		--outdir ./results_10302024 \
		--fasta $(REF_FA) \
		--gff $(REF_GFF) \
		--bed $(REF_BED) \
		--tss_bed $(REF_TSS) \
		--read_length 50 \
		-profile docker \
		--macs_gsize 3100000000 \
		--with control \
		-resume

#Below are the commands I used in troubleshooting the pipeline:

##-c nextflow.config is this still needed?
		
##run_TNF:
	./nextflow run \
		nf-core/atacseq \
		--input ./ATACseq_data.TNFonly.csv \
		--outdir $(OUT_DIR) \
		--fasta $(REF_FA) \
		--gff $(REF_GFF) \
		--read_length 50 \
		-profile docker \
		--macs_gsize 310000000 \
		-resume

##run_resume:
	./nextflow run \
	       	nf-core/atacseq \
	       	--input ./ATACseq_data.csv \
	       	--outdir $(OUT_DIR) \
	       	--fasta $(REF_FA) \
	       	--gff $(REF_GFF) \
	       	--read_length 150 \
	       	-profile docker \
	       	--macs_gsize 3100000000 \
		-resume

##run_narrowpeaks:
	./nextflow run \
	       	nf-core/atacseq \
	       	--input ./ATACseq_data.csv \
	       	--outdir ./results \
	       	--fasta $(REF_FA) \
	       	--gff $(REF_GFF) \
	       	--read_length 150 \
	       	-profile docker \
	       	--macs_gsize 3100000000 \
		--narrow_peak \
		-resume
## info from nf-core on custom reference genomes using nf-core/rnaseq as an example

##dirs:
	find $(REF_DIR)
	find $(DATA_DIR) -name '*.fastq.gz'


##save_reference:
	./nextflow run \
    	nf-core/rnaseq \
   	--input samplesheet.csv \
    	--fasta Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa.gz \
    	--gtf Homo_sapiens.GRCh38.108.gtf.gz \
    	--save_reference \
    	<OTHER_PARAMETERS>
