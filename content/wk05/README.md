# Week 3 - Demultiplexing

1. [Introduction](#introduction)
2. [Learning Objectives](#learning-objectives)
3. [Review Material](#review-material)
4. [Lecture Material](lecture.md)
4. [Assignment](assignment.md)
5. [Project](#project)

## Introduction

This week we will begin our command line analysis training.

Due to the design of most NGS systems each flowcell is single-use and produces a constant number of sequence reads.
`Multiplexing` is a common technique in NGS sequencing practice to get the most out of each run.
If you don't need all 5M reads for a single sample, you can `multiplex` multiple samples into the same sequencing run.

This is accomplished by adding a short & unique _barcode_ to each sample during the library preparation stage.
Then, each sample is pooled in equimolar ratios and sequenced on the same flowcell.
After sequencing, one can examine the _barcode_ and attribute each read to the specific sample.
This process is called `demultiplexing`. 

I have created a multiplexed fastq from the samples in the [Snowflake Yeast Datset](/datasets/PRJNA943273-snowflake-yeast.md).
We will use a tool called [`seqkit`](https://bioinf.shenwei.me/seqkit/) to split the samples and explore the results.

## Learning Objectives

 - Relate the reason for multiplexing multiple samples in a single run.
 - Describe how multiplexing is commonly accomplished in NGS.
 - Recognize and describe `fasta` & `fastq` files.
 - Practice basic terminal commands like `mkdir`, `mv`, `rm`, `less`, `head`.
 - Employ `seqkit grep` to find reads matching a pattern.
 - Employ `seqkit stats` to describe the contents of sequencing files.
 - Interpret `seqkit stats` across demultiplexing results.
 - Exporting data from the SRA using `sra-tools`.

## Reading Material

 - [Video](https://www.youtube.com/watch?v=_olpuoicdII) - Multiplexing and molecular barcodes (indexes) in NGS (Next Gen Sequencing). the bumbling biochemist

## Project

For your project.
 - Download sequencing data from the short read archive using `fasterq-dump`. Due to the bandwidth and computational requirements of this process, we may need to schedule this asynchronously.
 - Use `seqkit stats` to generate a report.
 - Write a markdown file that describes your dataset. Include that seqkit stats table as a markdown table.
 - Describe the number of reads per sample in your study. Does it tell you anything interesting?
