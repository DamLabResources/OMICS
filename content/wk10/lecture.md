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

A trivial example.

Imagine we have a `fastq` file that we want to turn into a `fasta` and then use `muscle` to do a multiple alignment.
Then we want to make a report from the alignment.

We'd build a `makefile` like this:

```makefile
sequence.fasta: sequence.fastq
	seqkit fq2fa sequence.fastq > sequence.fasta

alignment.fa: sequence.fasta
	muscle -in sequence.fasta alignment.fa

report.txt: alignment.fa
	generate_report alignment.fa report.txt
```

Then, we'd ask to `make` the _last item_ of the pipeline.

```bash
make report.txt
```

Internally, `make` will look for the dependancy of `report.txt`. 
If it doesn't exist, and there is rule to make it, it will make the file `alignment.fa`.
If `sequence.fasta` doesn't exist, it will make it.
Also, as it follows this chain, it will check the modification-times of the various targets and dependancies.
It will trigger re-runs if any dependency is newer than the target.

In this way, we can encapsulate a complex analysis DAG as a series of "transfomation rules" and allow `make` to determine which ones need to be rerun.

We'll build a `makefile` for this analysis together.

```bash
mkdir -p ~/OMICS/wk10
cd ~/OMICS/wk10
mkdir quants
nano makefile
```

You may want to open a second terminal and move it to `~/OMICS/wk10`.

```makefile
REF=/data/share/refs/SGD/salmonindex/
SOURCE=/data/share/OMICS/wk10/mini


sample:
	salmon quant -i $(REF) -l A -1 $(SOURCE)/SRR24466374_1.fastq -2 $(SOURCE)/SRR24466374_2.fastq --validateMappings -o quants/SRR24466374
```

After saving, use your other terminal to run.

```bash
make sample
```

You should see it start running `salmon`.

We could just copy-paste more commands under that line to run the other samples.
But ... that's not very _makey_.
We're not using dependencies or targets.

Let's change it to something like this.

```makefile
REF=/data/share/refs/SGD/salmonindex
SOURCE=/data/share/OMICS/wk10


quants/%: $(SOURCE)/%_1.fastq $(SOURCE)/%_1.fastq
	salmon quant -i $(REF) -l A -1 $(SOURCE)/$*_1.fastq -2 $(SOURCE)/$*_2.fastq --validateMappings -o $@
```

Now, the tool is called like this.

```bash
make quants/SRR24466374
```

Assuming the last command ran, this should actually be "up to date".

But, we can run the next sample easily.

```bash
make quants/SRR24466375
```

While it's running:

This `makefile` takes advantage of a handful of `make` things.

 - `%` is used as a wildcard that can _capture_ parts of a filename in targets and deps.
 - `$*` in the command refers to the part of the filename that was captured by `%`.
 - `$@` is the target of this make command.

There are a few other common replacements, that this didn't need but you might one day:
 - `$<` The name of the first prerequisite (dependency).
 - `$^` The names of all the prerequisites (dependencies), separated by spaces, and removing duplicates.
 
From this, you can see why filename discipline is important.
If everything follows a nice filename scheme, everything can be done with `make`.

Let's quickly look at the files `salmon quant` made for us.

```bash
tree quants
```

The one of most interest is this one: `quants/SRR24466374/quant.sf`

```bash
less quants/SRR24466374/quant.sf
```

Now, how do we make _all_ of the samples in the directory.
We need two more concepts.

`wildcard`
The wildcard function is used to get a list of filenames matching a specified pattern.

Syntax:
```make
$(wildcard pattern)
```

Usage:
If you have a directory with files named file1.txt, file2.txt, and image.jpg and you want to get a list of all .txt files, you would use:

```make
TXT_FILES := $(wildcard *.txt)
TXT_FILES would then be set to file1.txt file2.txt.
```

`patsubst`

The `patsubst` function performs pattern-based string substitution.
It's often used to transform lists of filenames.

Syntax:

```make
$(patsubst pattern,replacement,text)
```
* `pattern` specifies the string pattern to search for.
* `replacement` specifies the replacement string.
* `text` is the string (or list of strings) in which substitution should be performed.

Renaming extensions:
If you have a list of filenames like file1.c file2.c file3.c and you want to change their extensions to .o:
```make
OBJ_FILES := $(patsubst %.c,%.o,file1.c file2.c file3.c)
OBJ_FILES would then be set to file1.o file2.o file3.o.
```

Changing directories:
If you want to move a list of files from a src directory to a bin directory:
```make
BIN_FILES := $(patsubst src/%,bin/%,src/file1 src/file2)
BIN_FILES would then be bin/file1 bin/file2.
```
In these functions:

`%` is used as a wildcard that matches any number of any characters.
In patsubst, the matched content can be referred back in the replacement part.



Let's make a final `all` command in our `makefile` that will run the whole pipeline.

```makefile
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
```

Now, simply running:

```bash
make all -n
```

Will dry-run the _entire_ pipeline and show you each command it would run.

Then, if all is well, 

```bash
make all

# or just
make
```
Will run everything.

If any of the files are updated, or new files are added to the directory just re-run
`make all`.
It will only run the files that need to be updated.

This is the ideal Zen of any bioinformatics analysis.
Start to finish with a single command.