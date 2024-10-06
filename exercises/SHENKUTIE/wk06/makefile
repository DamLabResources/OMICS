REFFA := saccharomyces_cerevisiae.fa
REFDIR := ~/share/refs/SGD
REF := ~/share/refs/SGD/$(REFFA)
SEED := 100
READ_DIR := ~/share/OMICS/wk06/reads/

all: subsample

ref: refs/$(REFFA)

refs/$(REFFA): $(REF)
	ln -s $(REF) refs

refs/$(REFFA).ann: refs refs/$(REFFA)
	bwa index refs/$(REFFA)

refs:
	mkdir refs

refidx: refs/$(REFFA).ann

stats:
	seqkit stats $(READ_DIR)/SF_ann_*.fq.gz
	seqkit stats $(READ_DIR)/SF_aer_*.fq.gz
	seqkit stats $(READ_DIR)/OGstrain*.fq.gz

stats100k:
	seqkit stats SF_ann_*.fq.gz
	seqkit stats SF_aer_*.fq.gz
	seqkit stats OGstrain*.fq.gz

subsample:
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/SF_ann_R1.fq.gz |seqkit head -n 100000 -o SF_ann_R1_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/SF_ann_R2.fq.gz |seqkit head -n 100000 -o SF_ann_R2_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/SF_aer_R1.fq.gz |seqkit head -n 100000 -o SF_aer_R1_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/SF_aer_R2.fq.gz |seqkit head -n 100000 -o SF_aer_R2_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/OGstrain_R1.fq.gz |seqkit head -n 100000 -o OGstrain_R1_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/OGstrain_R2.fq.gz |seqkit head -n 100000 -o OGstrain_R2_100k.fq.gz
	seqkit stats *_100k.fq.gz

align: 
	bwa mem refs/$(REFFA) SF_ann_R?_100k.fq.gz > SF_ann.sam
	bwa mem refs/$(REFFA) SF_aer_R?_100k.fq.gz > SF_aer.sam
	bwa mem refs/$(REFFA) OGstrain_R?_100k.fq.gz > OGstrain.sam
	ls -l *.sam

view:
	samtools view -q 30 -f 0 -c SF_ann.sam
	samtools view -q 30 -f 0 -c SF_aer.sam
	samtools view -q 30 -f 0 -c OGstrain.sam

sort:
	samtools sort SF_ann.sam -o SF_ann.sorted.bam
	samtools sort SF_aer.sam -o SF_aer.sorted.bam
	samtools sort OGstrain.sam -o OGstrain.sorted.bam

index:
	samtools index SF_ann.sorted.bam
	samtools index SF_aer.sorted.bam
	samtools index OGstrain.sorted.bam

image:
	align_map.png
clean:
	rm -f *.fq.*
	rm -rf refs
