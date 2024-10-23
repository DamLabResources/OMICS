REF := /data/share/refs/SGD/saccharomyces_cerevisiae.fa
DIR_READS := /data/share/OMICS/wk06/reads
SEED := 1234

hello:
	find $(DIR_READS) | xargs ls -o
	ls -l $(REF)

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


s3_align:
	bwa mem $(REF) SF_ann_R?_100k.fq.gz > SF_ann.sam
	bwa mem $(REF) SF_aer_R?_100k.fq.gz > SF_aer.sam
	bwa mem $(REF) OGstrain_R?_100k.fq.gz > OGstrain.sam

s4_sort:
	samtools sort SF_ann.sam -o SF_ann.sorted.sam
	samtools sort SF_aer.sam -o SF_aer.sorted.sam
	samtools sort OGstrain.sam -o OGstrain.sorted.sam

s5_count:
	samtools view -q 30 -f 0 -c SF_ann.sam
	samtools view -q 30 -f 0 -c SF_aer.sam
	samtools view -q 30 -f 0 -c OGstrain.sam

s6_convert:
	samtools view -bS SF_ann.sorted.sam > SF_ann.sorted.bam
	samtools view -bS SF_aer.sorted.sam > SF_aer.sorted.bam
	samtools view -bS OGstrain.sorted.sam > OGstrain.sorted.bam
s7_depth:
	samtools depth SF_ann.sorted.bam > SF_ann.depth.txt
	samtools depth SF_aer.sorted.bam > SF_aer.depth.txt
	samtools depth OGstrain.sorted.bam > OGstrain.depth.txt
s8_index:
	samtools index SF_ann.sorted.bam
	samtools index SF_aer.sorted.bam
	samtools index OGstrain.sorted.bam
