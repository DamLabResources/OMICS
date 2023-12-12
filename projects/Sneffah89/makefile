# Define the input BAM files and the output VCF file
BAM_FILES = ~/share/courses/OMICS/hivbrain/barcode10.rg.bam ~/share/courses/OMICS/hivbrain/barcode11.rg.bam ~/share/courses/OMICS/hivbrain/barcode12.rg.bam
OUTPUT_VCF = merged.vcf

# Rule to convert BAM files to VCF
$(OUTPUT_VCF): $(BAM_FILES)
	 bcftools mpileup -Ou -f ~/common/WKD/hg38hxb2f.fasta $^ | bcftools call --ploidy 1 -mv -Ob -o $@

# Rule to create an index for the VCF file
$(OUTPUT_VCF).csi: $(OUTPUT_VCF)
	 bcftools index $^

# Rule to clean up intermediate files
clean:
	 rm -f $(OUTPUT_VCF) $(OUTPUT_VCF).csi

# Make all the rules
all: $(OUTPUT_VCF) $(OUTPUT_VCF).csi

# Specify that the clean rule doesn't create a file named "clean"
.PHONY: clean
