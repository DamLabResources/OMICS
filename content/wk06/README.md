# Week 6 - Alignment

1. [Introduction](#introduction)
2. [Learning Objectives](#learning-objectives)
3. [Lecture Material](lecture.md)
4. [Assignment](assignment.md)

## Introduction

This week, we will focus on aligning reads to a reference.
This is a crucial first step in almost all OMICS procedures.
Upon completion, we will have an alignment file that indicates where each read aligns to a reference genome and how it does so.

We will continue to use the [Snowflake Yeast Datset](/datasets/PRJNA943273-snowflake-yeast.md).

## Learning Objectives

By the end of this week, students should be able to:

* Understand the Burroughs-Wheeler Alignment (BWA) algorithm and its applications.
* Differentiate between BWA and other alignment algorithms (like BLAST).
* Understand why we **should not** put large result-files into git repos.
* Understand the purpose of generating alignment indexes.
* Use `samtools` to view and count the number of aligned reads.
* Use `samtools flagstat` to summarize an alignment result.
* Understand the important fields of a `SAM` format.

## Assignment

For this assignment, you will use BWA to align Illumina reads from a sequencing of multi-cellular snowflake yeast.
In future weeks these results will be identify variants that may be associated with multicellularity.
Finally, you will interpret the results of the alignment.