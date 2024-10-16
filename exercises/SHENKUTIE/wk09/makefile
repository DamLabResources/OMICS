REF := /data/share/refs/SGD/saccharomyces_cervisiae.fa
BAMaer := /data/share/OMICS/wk06/alns/SF_aer.sorted.bam
BAMann := /data/share/OMICS/wk06/alns/SF_ann.sorted.bam
BAMOG := /data/share/OMICS/wk06/alns/OGstrain.sorted.bam

# bcftools mpileup -r chrIII -Ou -f
bam:
	find ../wk06 -name '*.sorted.bam'

hw01:
	sh variant_pipeline.sh $(BAMaer) calls_aer.bcf
	sh variant_pipeline.sh $(BAMann) calls_ann.bcf
	sh variant_pipeline.sh $(BAMOG) calls_OG.bcf
