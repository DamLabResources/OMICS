# Introduction

Transcriptomics is finding where reads overlap known exons.
Peak-calling is the reverse; finding intervals of interest based on where reads "pileup".
ChIP-Seq, ATAC-Seq, and most 'pull-down' style experiments fall into this category.
This week we will utlize the Model-based Analysis of ChIP-Seq (MACS) tool to analyze a Yeast Transcription factor compendium.

We will also cover computational 'environments'.
These are abstractions that allow us to maintain our own sets of software environments.
This allows you to install your own collection of tools without involving the sys-admin and maintain conflicting packages.
MACS, is not installable in the `base` environment on Mistake-Not; so we will cover environment management with `mamba`. 

# Learning Objectives

By the end of this week you should be able to:
 * Create and utilize environments in your home directory.
 * Run `macs3 callpeaks` on pre-aligned data.
 * Visualize bedgraph, bigWig, and bed files in IGV.
 
# Assignment

Complete a peak calling analysis for any other pull down from PRJNA622558.