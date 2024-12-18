Week 11 Homework Assignment:
Peak calling analysis for any other pull down from PRJNA622558.

1) Got files from website using fasterq dump

```bash
prefetch SRR11466111
prefetch SRR11466112

fasterq-dump -p SRR11466111
fasterq-dump -p SRR11466112
```

2) Aligned to reference genome, converted from .sam to .bam, and sorted it

```bash
bwa mem ~/share/refs/SGD/saccharomyces_cerevisiae.fa ~/OMICS/wk11hw/SRR11466111_1.fastq ~/OMICS/wk11hw/SRR11466111_2.fastq > ~/OMICS/wk11hw/ace2_rep1.sam

bwa mem ~/share/refs/SGD/saccharomyces_cerevisiae.fa ~/OMICS/wk11hw/SRR11466112_1.fastq ~/OMICS/wk11hw/SRR11466112_2.fastq > ~/OMICS/wk11hw/ace2_rep2.sam

samtools view -b ~/OMICS/wk11hw/ace2_rep1.sam > ~/OMICS/wk11hw/ace2_rep1.bam
samtools view -b ~/OMICS/wk11hw/ace2_rep2.sam > ~/OMICS/wk11hw/ace2_rep2.bam

samtools sort ~/OMICS/wk11hw/ace2_rep1.bam > ~/OMICS/wk11hw/ace2_rep1.sorted.bam
samtools sort ~/OMICS/wk11hw/ace2_rep2.bam > ~/OMICS/wk11hw/ace2_rep2.sorted.bam
```

3)  Used `macs3` to get the following things from the pulldown experiment.

```bash
conda activate ~/envs/macs

macs3 callpeak -t ~/OMICS/wk11hw/ace2_rep1.sorted.bam -c ~/share/OMICS/wk11/aligns/chip_notag_rep1.sorted.bam -f BAMPE -B --outdir macs_output/ -n ACE2_rep1 -g 12e6

macs3 callpeak -t ~/OMICS/wk11hw/ace2_rep2.sorted.bam -c ~/share/OMICS/wk11/aligns/chip_notag_rep1.sorted.bam -f BAMPE -B --outdir macs_output/ -n ACE2_rep2 -g 12e6
```

4) Use `bedtools` and `saccharomyces_cerevisiae.gff` to find all hits within the 1000 bp upstream of a gene. Intersect the list of genes between the two sets.

```bash
bedtools window -l 1000 -r 0 -a ~/share/refs/SGD/saccharomyces_cerevisiae.gff -b macs_output/ACE2_rep1_peaks.narrowPeak -u> ~/OMICS/wk11hw/ace2_rep1_hits.gff
bedtools window -l 1000 -r 0 -a ~/share/refs/SGD/saccharomyces_cerevisiae.gff -b macs_output/ACE2_rep2_peaks.narrowPeak -u> ~/OMICS/wk11hw/ace2_rep2_hits.gff

bedtools intersect -a ~/OMICS/wk11hw/ace2_rep1_hits.gff -b ~/OMICS/wk11hw/ace2_rep2_hits.gff | less -S
```
