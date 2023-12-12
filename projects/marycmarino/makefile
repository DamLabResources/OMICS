REF=~/share/courses/OMICS/RDSLR/salmonindex
SOURCE=~/share/courses/OMICS/RDLSR/reads

FASTQ_FILES := $(wildcard $(SOURCE)/*.fastq.gz)
QUANT_DIRS := $(patsubst $(SOURCE)/%.fastq,quants/%,$(FASTQ_FILES))

all: merged/merged.sf
        echo "complete"

clean:
        rm -r quants
        rm -r merged

merged/merged.sf: $(QUANT_DIRS)
        echo "Merging: $(QUANT_DIRS)"
        mkdir -p merged
        salmon quantmerge --quants $^ -o merged/merged.sf

quants/%: $(SOURCE)/%_1.fastq $(SOURCE)/%_1.fastq
        mkdir -p quants
        echo "Salmon on $*"
        salmon quant -i $(REF) -l A -1 $(SOURCE)/$*_1.fastq -2 $(SOURCE)/$*_2.fastq --validateMappings -o $@
