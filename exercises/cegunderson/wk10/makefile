REF=/data/share/refs/SGD/salmonindex
SOURCE=/data/share/OMICS/wk10/mini

FASTQ_FILES := $(wildcard $(SOURCE)/*_1.fastq.gz)
QUANT_DIRS := $(patsubst $(SOURCE)/%_1.fastq.gz,quants/%,$(FASTQ_FILES))

all: merged/merged.sf
	echo "complete"
    
clean:
	rm -r quants
	rm -r merged 

merged/merged.sf: $(QUANT_DIRS)
	echo "Merging: $(QUANT_DIRS)"
	mkdir -p merged
	salmon quantmerge --quants $^ -o merged/merged.sf

quants/%: $(SOURCE)/%_1.fastq.gz $(SOURCE)/%_1.fastq.gz
	mkdir -p quants
	echo "Salmon on $*"
	salmon quant -i $(REF) -l A -1 $(SOURCE)/$*_1.fastq.gz -2 $(SOURCE)/$*_2.fastq.gz --validateMappings -o $@


