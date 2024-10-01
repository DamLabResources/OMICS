REF := ~/share/refs/SGD/saccharomyces_cerevisiae.fa
SEED := 100
READ_DIR := ~/share/OMICS/wk06/reads/

stats:
	seqkit stats $(READ_DIR)/SF_ann_*.fq.gz
	seqkit stats $(READ_DIR)/SF_aer_*.fq.gz
	seqkit stats $(READ_DIR)/OGstrain*.fq.gz

subsample:
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/SF_ann_R1.fq.gz |seqkit head -n 100000 -o SF_ann_R1_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/SF_ann_R2.fq.gz |seqkit head -n 100000 -o SF_ann_R2_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/SF_aer_R1.fq.gz |seqkit head -n 100000 -o SF_aer_R1_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/SF_aer_R2.fq.gz |seqkit head -n 100000 -o SF_aer_R2_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/OGstrain_R1.fq.gz |seqkit head -n 100000 -o OGstrain_R1_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(READ_DIR)/OGstrain_R2.fq.gz |seqkit head -n 100000 -o OGstrain_R2_100k.fq.gz

align: 
	bwa mem $(REF) SF_ann_R* > SF_ann.sam

clean:
	rm -rf *.fq.*
