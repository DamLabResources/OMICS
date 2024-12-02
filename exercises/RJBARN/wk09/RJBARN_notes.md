sh variant_pipeline_chrVI.sh ~/share/OMICS/wk06/alns/OGstrain.sorted.bam ./OGstrain.bcf
bcftools view OGstrain.bcf > OGstrain.vcf
bgzip OGstrain.vcf
bcftools index OGstrain.vcf.gz
bcftools isec -p isec_output -n-1 -c all SF_aer.vcf.gz SF_ann.vcf.gz OGstrain.vcf.gz 
#I renamed the output files to contain the sample names 
bedtools intersect -a ../OGstrain_0002.vcf -b ~/share/refs/SGD/saccharomyces_cerevisiae.gff > OGstrain_gene_intersect.bam

