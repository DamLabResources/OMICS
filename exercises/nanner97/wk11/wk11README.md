## Week 11 hw

- I chose to look at Hmt1 because it is relevant to my thesis :)

- activate macs
```bash
conda activate ~/envs/macs
```
- pull SRR files from accession viewer
```bash
fasterq-dump -p SRR11467231
gzip SRR*
```

- then align to the reference genome
```bash
bwa mem /data/share/refs/SGD/saccharomyces_cerevisiae.fa SRR11467231_1.fastq.gz SRR11467231_2.fastq.gz | samtools sort > alnHMT1.sorted.bam
```

- then use macs3 to call peaks (make sure macs is activated!!)
```bash
macs3 callpeak -t alnHMT1.sorted.bam -c ~/share/OMICS/wk11/aligns/chip_notag_rep1.sorted.bam -f BAMPE -B --outdir output -n HMT1_peaks -g 12e6
```

-find peaks within the 1000bp region upstream
```bash
bedtools window -l 1000 -r 0 -a /data/share/refs/SGD/saccharomyces_cerevisiae.gff -b output/HMT1_peaks_peaks.narrowPeak -u > output/hits/HMT1_hits.gff
```
