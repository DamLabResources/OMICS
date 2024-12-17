bwa mem ~/share/refs/SGD/saccharomyces_cerevisiae.fa ~/share/ts3576/OMICS/wk11/SRR11466111_1.fastq ~/share/ts3576/OMICS/wk11/SRR11466111_2.fastq > ~/share/ts3576/OMICS/wk11/ace_rep1.sam
bwa mem ~/share/refs/SGD/saccharomyces_cerevisiae.fa ~/share/ts3576/OMICS/wk11/SRR11466112_1.fastq ~/share/ts3576/OMICS/wk11/SRR11466112_2.fastq > ~/share/ts3576/OMICS/wk11/ace_rep2.sam
samtools view -b ~/share/ts3576/OMICS/wk11/ace_rep1.sam > ~/share/ts3576/OMICS/wk11/ace_rep1.bam
samtools view -b ~/share/ts3576/OMICS/wk11/ace_rep2.sam > ~/share/ts3576/OMICS/wk11/ace_rep2.bam
samtools sort ~/share/ts3576/OMICS/wk11/ace_rep1.bam > ~/share/ts3576/OMICS/wk11/ace_rep1.sorted.bam
samtools sort ~/share/ts3576/OMICS/wk11/ace_rep2.bam > ~/share/ts3576/OMICS/wk11/ace_rep2.sorted.bam
conda activate ~/envs/macs
macs3 callpeak -t ~/share/ts3576/OMICS/wk11/ace_rep1.sorted.bam -c ~/share/OMICS/wk11/aligns/chip_notag_rep1.sorted.bam -f BAMPE -B --outdir macs_output/ -n ace_rep1 -g 12e6
macs3 callpeak -t ~/share/ts3576/OMICS/wk11/ace_rep2.sorted.bam -c ~/share/OMICS/wk11/aligns/chip_notag_rep1.sorted.bam -f BAMPE -B --outdir macs_output/ -n ace_rep2 -g 12e6
bedtools window -l 1000 -r 0 -a ~/share/refs/SGD/saccharomyces_cerevisiae.gff -b macs_output/ace_rep1_peaks.narrowPeak -u> ~/share/ts3576/OMICS/wk11/ace_rep1_hits.gff
bedtools window -l 1000 -r 0 -a ~/share/refs/SGD/saccharomyces_cerevisiae.gff -b macs_output/ace_rep2_peaks.narrowPeak -u> ~/share/ts3576/OMICS/wk11/ace_rep2_hits.gff
bedtools intersect -a ~/share/ts3576/OMICS/wk11/ace_rep1_hits.gff -b ~/share/ts3576/OMICS/wk11/ace_rep2_hits.gff | less -S