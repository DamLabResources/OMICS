## Wk10 homework

- first I created a Makefile with the following contents:

```make
REF=/data/share/refs/SGD/salmonindex
SOURCE=/data/share/OMICS/wk10/mini

FASTQ_FILES := $(wildcard $(SOURCE)/*_1.fastq.gz)
QUANT_DIRS := $(patsubst $(SOURCE)/%_1.fastq.gz,quants/%,$(FASTQ_FILES))

all: merged/merged.sf
	echo "complete"

clean:
	rm -r quants
	rm -r merged
	echo "complete2"

merged/merged.sf: $(QUANT_DIRS)
	echo "Merging: $(QUANT_DIRS)"
	mkdir -p merged
	salmon quantmerge --quants $^ -o merged/merged.sf
	echo "complete3"

quants/%: $(SOURCE)/%_1.fastq.gz $(SOURCE)/%_2.fastq.gz
	mkdir -p quants
	echo "Salmon on $*"
	salmon quant -i $(REF) -l A -1 $(SOURCE)/$*_1.fastq.gz -2 $(SOURCE)/$*_2.fastq.gz --validateMappings -o $@
	echo "complete4"
```

- then I simply ran this with "make"
- to generate the expression matrix I used

```bash
salmon quantmerge --quants quants/* -o expression_matrix.mini.sf
```

- then I replaced "mini" with "full" in the source variable and used quantmerge to put out expression_matrix.full.sf
- however I don't think this actually worked because nothing seemed to change in my directory... however mini did work!