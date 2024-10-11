DIR_READS := /data/share/OMICS/wk06/reads
SEED := 1234

hello:
	find $(DIR_READS) | xargs ls -o

s0_stats:
	seqkit stats $(DIR_READS)/*.fq.gz

s1_subsample:
	seqkit sample -p 0.02 -s $(SEED) $(DIR_READS)/SF_ann_R1.fq.gz | seqkit head -n 100000 -o SF_ann_R1_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(DIR_READS)/SF_ann_R2.fq.gz | seqkit head -n 100000 -o SF_ann_R2_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(DIR_READS)/SF_aer_R1.fq.gz | seqkit head -n 100000 -o SF_aer_R1_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(DIR_READS)/SF_aer_R2.fq.gz | seqkit head -n 100000 -o SF_aer_R2_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(DIR_READS)/OGstrain_R1.fq.gz | seqkit head -n 100000 -o OGstrain_R1_100k.fq.gz
	seqkit sample -p 0.02 -s $(SEED) $(DIR_READS)/OGstrain_R2.fq.gz | seqkit head -n 100000 -o OGstrain_R2_100k.fq.gz

s2_stats:
	seqkit stats *_100k.fq.gz



