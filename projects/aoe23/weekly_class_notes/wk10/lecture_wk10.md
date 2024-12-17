# 2024-10-23 Week 10: In Class Assignment

***
# *From Will's Lecture Notes*
# Transcriptomics

There are two general strategies for performing transcriptomics:
 1. Alignment based methods:
   0. Create an index of the genome.
   1. Align the reads to the genome.
   2. "Count" the number of reads that overlap any known transcript.
   3. Normalize.
   4. Profit.
 2. Psuedo-alignment based methods:
   0. Create a **much smaller** index of just the transcripts.
   1. Align the reads to the transcripts.
   2. Normalize.
   3. Profit. 

If you check out the `nfcore/rnaseq` pipeline, there are two paths:
![nfcore rnaseq pipeline](https://raw.githubusercontent.com/nf-core/rnaseq/3.14.0//docs/images/nf-core-rnaseq_metro_map_grey.png)

One using `kalisto` or `salmon`, one using `STAR` or `HISTAT`.

What are some advantages and disadvantages of each?

For simplicity, we'll be using Salmon to perform RNA sequence quantification today.

This will boil down into two main steps:

1. Index generation
2. Sample quantification
3. Multi-sample merging

## Index generation

Salmon, like all good linux tools has a help message.

```bash
salmon -h

salmon v1.10.1

Usage:  salmon -h|--help or 
        salmon -v|--version or 
        salmon -c|--cite or 
        salmon [--no-version-check] <COMMAND> [-h | options]

Commands:
     index      : create a salmon index
     quant      : quantify a sample
     alevin     : single cell analysis
     swim       : perform super-secret operation
     quantmerge : merge multiple quantifications into a single file
```

We obviously want `salmon index`.
Refering to their [documentation](https://salmon.readthedocs.io/en/latest/salmon.html#preparing-transcriptome-indices-mapping-based-mode).

> If you want to use Salmon in mapping-based mode, then you first have to build a salmon index for your transcriptome. 
> Assume that transcripts.fa contains the set of transcripts you wish to quantify.
> We generally recommend that you build a decoy-aware transcriptome file.

> There are two options for generating a decoy-aware transcriptome:
> The first is to compute a set of decoy sequences by mapping the annotated transcripts you wish to index against a hard-masked version of the organism’s genome.
> This can be done with e.g. MashMap2, and we provide some simple scripts to greatly simplify this whole process.
> Specifically, you can use the generateDecoyTranscriptome.sh script, whose instructions you can find in this README.

> The second is to use the entire genome of the organism as the decoy sequence.
> This can be done by concatenating the genome to the end of the transcriptome you want to index and populating the decoys.txt file with the chromosome names.
> Detailed instructions on how to prepare this type of decoy sequence is available here.

> This scheme provides a more comprehensive set of decoys, but, obviously, requires considerably more memory to build the index.
> Finally, pre-built versions of both the partial decoy and full decoy (i.e. using the whole genome) salmon indices for some common organisms are available via refgenie here.

> If you are not using a pre-computed index, you run the salmon indexer as so:
> `./bin/salmon index -t transcripts.fa -i transcripts_index --decoys decoys.txt -k 31`

Which I did using the following commands:

```
cd  /data/share/courses/OMICS/SGD/

# Get names of each chromosome into a text file.
seqkit seq --name bwaindex/R64.fasta | cut -f1 -d ' ' > annotations/decoys.txt

# Add the whole chromosomes to the end as a decoy.
cat annotations/rna.fna bwaindex/R64.fasta > annotations/transcripts_decoys.fa

# Create the index, providing the decoy-aware fasta and the decoy names
salmon index -t annotations/transcripts_decoys.fa -i salmonindex --decoys annotations/decoys.txt -k 31
```

Which now makes a `/data/share/refs/SGD/salmonindex/` directory ready for quantification.

# Quantification

As you might have guessed, we'll use `salmon quant`.

Instead of simply typing the commands, we're going to use this as an oppurtunity to learn `Makefile`s.
These are like scripts (in that they contain commads that the terminal will run) but they are significantly more powerful.

***


## Basic Structure of a Makefile



A Makefile consists of a set of "rules".
Each rule defines how to produce an output (or "target") from one or more inputs.

A rule looks like this:
```makefile
target: dependencies
	commands to produce target from dependencies
```
Important tip: It is important that you use `TAB` and not 4-`spaces`.
The `TAB` is critical to the syntax.

***

# AE notes from what Will Says in Class

- advantages of a make file: you can tell the computer the order of these commands 
- the make file actually weaves all of the commands together!!
- format: 
    target : things that the target depends on
- example: if want to make a fasta from fastq, we need to say that we WANT a fasta , so that will go ahead fo the colon and then after we do fastq to tell it that the fasta file being made will reply on the fastq provided. 
- THEN do a TAB: below that and write the actual code of what you want.


then the final step is make the last item in the pipeline. 




### Jupyter Notebook to start Commands used in class

- git pull
- mkdir wk10 in omicsaoe23 home directory
- mkdir quants ##in week 10 folder

make the makefile in wk10 folder

- nano makefile

### now in the makefile nano

in nano past the following from the lecture.md will made: a full commpand and info that we can now paste in to the makefile which is below: 




```makefile
REF=/data/share/refs/SGD/salmonindex/
SOURCE=/data/share/OMICS/wk10/mini


sample:
	salmon quant -i $(REF) -l A -1 $(SOURCE)/SRR24466374_1.fastq -2 $(SOURCE)/SRR24466374_2.fastq --validateMappings -o quants/SRR24466374

```


Note: that first we define our variables which are 'REF' and 'SOURCE' at the top


to get out of the nano 
ctl +O: write
ctl +X: to exit 

### Back to Jupyter Notebook

now we are doing the first command back in juptyter notebook: 

- make sample


let this run....

### Back into make file nano and paste this for quants 


REF=/data/share/refs/SGD/salmonindex/
SOURCE=/data/share/OMICS/wk10/mini


quants/%: $(SOURCE)/%_1.fastq $(SOURCE)/%_1.fastq
	salmon quant -i $(REF) -l A -1 $(SOURCE)/$*_1.fastq -2 $(SOURCE)/$*_2.fastq --validateMappings -o $@
    
    
### Back into jupyter 

to test it with the next SRR

### final way to update everything in make file nano: 



REF=/data/share/refs/SGD/salmonindex
SOURCE=/data/share/OMICS/wk10

FASTQ_FILES := $(wildcard $(SOURCE)/*_1.fastq)
QUANT_DIRS := $(patsubst $(SOURCE)/%_1.fastq,quants/%,$(FASTQ_FILES))

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



- note we put this into chat gpt to clean it up so that it runs properly. 

