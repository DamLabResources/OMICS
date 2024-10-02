# Long Read Alignment

Utlizing long reads during genomic sequencing provides numerous benifits when searching for structural re-arrangements.
Deletions, insertions, re-arrangements, and repeat length are easier to measure when your read spans the entire event.
However, these alignments look _different_ compared to short read alignments due to each read aligning to multiple places.

## Dataset

The files are at: `~/share/OMICS/wk07`

```bash
/home/jupyter-will/share/OMICS/wk07
├── reads
│   ├── T78276-MFG.small.fq.gz
│   └── T78276-SPL.small.fq.gz
└── refs
    └── K03455.fasta
```

We will use HIV proviral sequencing as an easy edge-case for long-read alignment.
The directory contains reads generated using two overlapping ~8.5kb PCR products.
After PCR, these were barcoded by ligation and sequenced on our nanopore sequencer.

I've pulled out a small subset of reads from the MidFrontal Gyrus and Spleen of an individual who lived with HIV.

## Self Exploration

First we want to align the reads to the reference.
This project is nearly identical to last week, except using the `minimap2` aligner.

For this first part, accomplish the following:

 - Copy the reads and reference files to a working directory in your `home`.
 - Use `seqkit stats` to describe the reads.
 - Use `minimap2` to align the reads from each sample to the `K03455` genome.
 - Use samtools to convert to a sorted bam file with an index.
 - Count the number of aligned records that map to the genome with at least a MAPQ>20.
 - Download the appropriate files and open them in IVG.
 
Work on your own or in groups.
We'll alot ~30 minutes for this section.


## IGV exploration

Go here: https://www.ncbi.nlm.nih.gov/nuccore/K03455.1
and follow along with Will on how to download the GFF files for genomes.

Look at the reads in IGV.
* Try sorting the reads by size, alignment start, and MapQ
* Note that there are some reads that are 'clear', what does that mean?
* Try turning on 'Link by supplemental alignment', what does that do?
* Which regions seem deleted. Are they the same between the two samples?


## Terminal exploration


When we look at long reads we need to consider 3 classes of alignments.

 - Primary Alignments
 - Secondary alignments
 - Supplemental Alignments

### Primary vs Secondary alignments

Imagine a read completely within the LTR.
Because it can align to either site, the aligner will create a line for each.
One will be marked _primary_, all others are _secondary_.
_not-primary_ reads are marked in the SAM flags at the 9th bit.
You will usually see these as `256` (forward) or `272` (reverse).
Primary alignments are _not marked_ in the SAM flags; only non-primary alignments are marked.

Nicely, samtools can filter based on SAM flags.

```bash
samtools view -h

...
  -f, --require-flags FLAG   ...have all of the FLAGs present
  -F, --excl[ude]-flags FLAG ...have none of the FLAGs present
...
```

```bash
# Exclude alignments with the 'secondary' flag ticked
samtools view -F 256 alns/T78276-SPL.sorted.bam | less -S


# Count them
samtools view -c -F 256 alns/T78276-SPL.sorted.bam 
```

### Supplemental Alignments

Supplemental alignments are _different_ from the primary/not-primary alignment.

Imagine a read that spans a joining of two chromosomes.
One part of the read will align to one part of the genome, the other part of the read will align to a different chromosome.
Each of those alignments will be output as an individual record.
The first one on the read stays as the primary alignment, all others are marked as 'supplemental' in the 12th bit of the SAM flags.

They will also have a special field on their optional fields at the end called an `SA` tag.
These indicate where the other parts of this read align.

I've pulled out one below to discuss:


```
957828d8-c3b7-4590-9767-4335fb96cb87_66-2450    2048    K03455.1        1167    ...

SA:Z:K03455.1,1167,+,686M2I1697S,60,24;K03455.1,9083,+,1864S497M23I1S,29,81;
```

These tags are used by downstream tools like `sniffles` and `cutesv` to detect structural variants.

```bash
# Exclude alignments with the 'not-primary' flag ticked
samtools view -F 2048 alns/T78276-SPL.sorted.bam | less -S


# Count them
samtools view -c -F 2048 alns/T78276-SPL.sorted.bam 


# We can also exlude both secondary and supplemental
samtools view -c -F 2304 alns/T78276-SPL.sorted.bam 
```