REF := /data/share/refs/SGD/saccharomyces_cerevisiae.fa
GFF := /data/share/refs/SGD/saccharomyces_cerevisiae.gff
BAMaer := /data/share/OMICS/wk06/alns/SF_aer.sorted.bam
BAMann := /data/share/OMICS/wk06/alns/SF_ann.sorted.bam
BAMOG := /data/share/OMICS/wk06/alns/OGstrain.sorted.bam

headgff:
	head -100 $(GFF)

features:
	cut -f 3 $(GFF) |sort|uniq -c |sort -n

# https://samtools.github.io/bcftools/bcftools.html#query
# Make a BED file: chr, pos (0-based), end pos (1-based), id
t1:
	bcftools query -f'%CHROM\t%POS0\t%END\t%ID\n' calls_aer_only.bcf

# bcftools mpileup -r chrIII -Ou -f
bam:
	find ../wk06 -name '*.sorted.bam'

hw01:
	sh variant_pipeline.sh $(BAMaer) calls_aer.bcf
	sh variant_pipeline.sh $(BAMann) calls_ann.bcf
	sh variant_pipeline.sh $(BAMOG) calls_OG.bcf

# create index files
hw02a:
	bcftools index -f calls_aer.bcf	
	bcftools index -f calls_ann.bcf
	bcftools index -f calls_OG.bcf

# find variants that are unique to each of the three yeast strains
hw02b:
	bcftools isec -n-1 -c all calls_OG.bcf calls_aer.bcf calls_ann.bcf -p isec


hw03:
	bedtools intersect -a isec/calls_aer.vcf -b $(GFF)

clean:
	rm *.csi
	rm -f *_only.bcf
