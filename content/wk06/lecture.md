# Basic Alignment

Read alignment serves as the foundation for nearly all OMICS techniques.

In our current task of variant-calling, it lines each read up with the most likely genomic origin.
Then, we can compare the sequence of the read with the reference to find variants.

In transcriptomics, which we'll cover later, reads are generated only from expressed mRNAs, alignment allows us to _count_ the number of expressed transcripts.
In ChIP pull-down experiments, only DNA attached to the protein of interest is sequenced, alignment gives us the binding map the the protein.
In ATAC-seq a TN5 only cuts exposed DNA, aligment of the reads tells us where the genome is open.

Everything starts with an alignment.

## Indexing

Searching a giant genome for a short inexact match is a computational complex problem.

Modern techniques employ an _indexing_ step in which computationally efficient _lookup-table_ is created.
This step is often computationally expensive in both time and space.
However, it only needs to be performed _once_ per genome (per search setting).
Then, it is loaded and rapidly searched in subsequent runs.

Each alignment tool has a different indexing strategy, but they all use it.

There are two alignment tools installed on this server.
 - `minimap2` - designed for aligning long (possibly noisy) reads
 - `bwa` - designed for aligning short, nearly exact, reads
 
### Activity
 
 * Make a directory _outside of your repo_, ie. `~/OMICS/wk06/` to work in.
 * `cd` there.
 * Make a sub-directory called `refs` and copy the genome files in `~/share/refs/SGD/` to there.
 * Use the `--help` and `man` pages to learn how to create indexes for bwa.
 * Create an index of the SGD genome in that directory using `bwa index`.
 
## Alignment

Now that we have an index, we need to align our sequences to that reference.

Let's get some reads from the Snowflake Yeast dataset.

### Activity
 * Make a sub-directory called `reads` and the files.
 * Copy the files `~/share/OMICS/wk06/reads/OGstrain_R1.10K.fq` and `~/share/OMICS/wk06/reads/OGstrain_R2.10K.fq` into your directory.
 * Use `seqkit stats` to examine them.


Basic alignment command:

```bash
bwa mem ref.fa read_R1.fq read_R2.fq > aln.sam
```


command to try:
```bash
bwa mem ref/saccharomyces_cerevisiae.fa reads/OGstrain_R1.10K.fq reads/OGstrain_R2.10K.fq | tee test.sam
```

What we see on the terminal are the _alignments_ in a Sequence Alignment Maping `SAM` format.

In brief, it is a TSV file with the following columns:

1. `QNAME` - Query template NAME
2. `FLAG` - bitwise FLAG
3. `RNAME` - Reference sequence NAME
4. `POS` - 1-based leftmost mapping POSition
5. `MAPQ` - MAPping Quality
6. `CIGAR` - CIGAR string
7. `RNEXT` - Reference name of the mate/next read
8. `PNEXT` - Position of the mate/next read
9. `TLEN` - observed Template LENgth
10. `SEQ` - segment SEQuence
11. `QUAL` - ASCII of Phred-scaled base QUALity+33
12. `INFO` - A tab-split list of additional information.

The detailed specifications about the file can be found at [ht_specs](https://samtools.github.io/hts-specs/).
We'll cover relevant sections as needed.

`samtools` is a command-line program for performing various operations on sam/bam files.
Much like `seqkit`, it is a cli that has numerous sub commands for doing different things with sam files.

Type: `samtools` in your terminal to get a list of all of the operations.

Check out: `samtools view` and `samtools flagstat`

Useful commands to try:

 - `samtools view -q 20 {path}` - Find only reads that map at 99% threshold.
 - `samtools view -c {path}` - Count reads.
 - `samtools view -H {path}` - Only print out the header.


## Sorting and Using

SAM files are nice to read, but they are needlessly large and difficult for computers to search.
By nature, the alignment tool will output the SAM file sorted by read-name.
This may be useful for some cases, but, in general, it is much easier if the files are sorted by mapping position.
The SAM specification also includes an _index_ definition that allows programs to rapidly find reads by position within large files.

So. in nearly every case, after we align reads, we want to sort them and index them.

```bash
samtools sort test.sam > test.bam
```

or, combined with your alignment command:

```bash
bwa mem ref/saccharomyces_cerevisiae.fa reads/OGstrain_R1.10K.fq reads/OGstrain_R2.10K.fq | samtools sort > test.bam
```

Then to index:

```bash
samtools index test.bam
```

This will create a file called `test.bam.bai`, this file should always live next-to its source file.

Once you've position-sorted and indexed a file you can do MANY additional commands.

```bash
samtools view test.bam chrI # only reads from chrI
samtools coverage test.bam # count the coverage across chromosomes
```
and nearly all of the other cool commands under `samtools -h`

We'll talk more about quantifying these files in the next few weeks.
Let's look at them.

## IGV

Hopefully, you've all installed IGV on you computers.

For this excercise you need to download the following files:

 - `saccharomyces_cerevisiae.fa` - The genome.
 - `saccharomyces_cerevisiae.fa.fai` - An index of the genome.
 - `saccharomyces_cerevisiae.gff` - The genomic annotations.
 - `test.bam` - The aligned and sorted reads.
 - `test.bam.bai` - The index for the reads.
 
If you've installed `samtools` on your computer you could create some of these files locally.

```bash
samtools faidx saccharomyces_cerevisiae.fa
```