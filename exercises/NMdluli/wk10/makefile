REF=/data/share/refs/SGD/salmonindex
SOURCE=/data/share/OMICS/wk10/full

FASTQ_FILES := $(wildcard $(SOURCE)/*_1.fq.gz)
QUANT_DIRS := $(patsubst $(SOURCE)/%_1.fq.gz,quants/%,$(FASTQ_FILES))

all: merged/merged.sf
	echo "complete"
    
clean:
	rm -r quants
	rm -r merged 

merged/merged.sf: $(QUANT_DIRS)
	echo "Merging: $(QUANT_DIRS)"
	mkdir -p merged
	salmon quantmerge --quants $^ -o merged/merged.sf

quants/%: $(SOURCE)/%_1.fq.gz $(SOURCE)/%_2.fq.gz
	mkdir -p quants
	echo "Salmon on $*"
	salmon quant -i $(REF) -l A -1 $(SOURCE)/$*_1.fq.gz -2 $(SOURCE)/$*_2.fq.gz --validateMappings -o $@
