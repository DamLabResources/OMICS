# Demultiplex Samples

## Introduction

For this assignment I have multiplexed data from the [Snowflake Yeast Datset](/datasets/PRJNA943273-snowflake-yeast.md) by adding 3' and 5' indexes and shuffling the reads back together.
Your task is to split them back into their individual sample files using `seqkit` tools.

## Goals

Create a directory structure as follows:

A set of statistics about the multiplexed data.
```bash
solution/muxed.stats.tsv
```

Files demultiplexed by barcode.
```bash
solution/SRR23803536.fastq
solution/SRR23803537.fastq
solution/SRR23803538.fastq
solution/SRR23803539.fastq
```

Sequences after removing the barcode.
```bash
solution/SRR23803536.trimmed.fastq.gz
solution/SRR23803537.trimmed.fastq.gz
solution/SRR23803538.trimmed.fastq.gz
solution/SRR23803539.trimmed.fastq.gz
```

Summary of the demultiplexed data.
```bash
solution/demux.stats.tsv
```

## Datasets

 - `data/multiplexed.fq` - A fastq file containing a subset of reads.
 - `data/sample_sheet.csv` - A csv file indicating the 3' and 5' barcodes _as they appear on the read_.

## Walkthrough

Utitlizing the dataset provided, complete the following tasks.
Create a `content/wk03/solution/notes_{user}.md` and, take notes, copy commands, and answer questions within that file document.

### Mux statistics

Use `seqkit stats` to generate basic statistics about about the multiplexed data.
Note the command and number of reads before demultiplexing in your solution document.


### Demulitplex the samples

Using the `data/sample_sheet.csv` file as a sample sheet, demultiplex the reads in `wk03/data/multiplexed.fq` into individual files.
The sample sheet defines the barcodes on the 3' and 5' ends as they appear on the sequence.
Save the files to `solution/{sample_name}.fastq` (but do not commit it).

There are a number of strategies for doing this:
 - `seqkit grep` utilizing regular expression
 - Utilizing multiple `seqkit grep` statements
 - _something else ..._
 
However, they will all end up with the same information. 

You should end with the following directory structure:
```bash
solution/SRR23803536.fastq
solution/SRR23803537.fastq
solution/SRR23803538.fastq
solution/SRR23803539.fastq
```

In your notes document include the commands you used and a description of how you figured out the commands.

### Trim the barcodes

Now that we know which sample each read belongs to, the barcode is now extranious information.
We should remove it from the read before downstream processing or it may lead to spurrious alignments.

Explore the seqkit toolbox through the website, the help-file, google search, Biostars posts, etc.
Then, utilize seqkit to create _gzipped_ fastq files that only contained the trimmed sequence.

You should end with the following directory structure:

```bash
solution/SRR23803536.trimmed.fastq.gz
solution/SRR23803537.trimmed.fastq.gz
solution/SRR23803538.trimmed.fastq.gz
solution/SRR23803539.trimmed.fastq.gz
```

In your notes document include the commands you used and a description of how you figured out the commands.

### Demux statistics

Use `seqkit stats` to generate basic statistics about about the demultiplexed and _trimmed_ data.
Save this summary as a tsv formatted file at the path `solution/demuxed.stats.tsv`.

In your notes document include the command you used, a markdown formatted version of the table, and a description of the results.


### Reflection Questions

Write a brief (~1 paragraph) reflecting on the results.
Consider the following questions.
 - Are there an equal number of reads from each sample?
 - Are the read lengths the same between each sample?