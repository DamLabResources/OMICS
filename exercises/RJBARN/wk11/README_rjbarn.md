#make a bedfile

macs3 callpeak -t ~/share/OMICS/wk11/aligns/chip_CCL1.sorted.bam -c ~/share/OMICS/wk11/aligns/chip_notag_rep1.sorted.bam -f BAMPE -g 12e6 -B --outdir macs_output -n CCL1

macs3 callpeak -t ~/share/OMICS/wk11/aligns/chip_ELF1.sorted.bam -c ~/share/OMICS/wk11/aligns/chip_notag_rep1.sorted.bam -f BAMPE -g 12e6 -B --outdir macs_output -n ELF1

#use bedtools to make a file that shows peaks that intersect with regiosn near genes

bedtools window -l 1000 -r 0 -a ~/share/refs/SGD/saccharomyces_cerevisiae.gff -b macs_output/CCL1_peaks.narrowPeak -u > macs_output/hits/CCL1_hits.gff

bedtools window -l 1000 -r 0 -a ~/share/refs/SGD/saccharomyces_cerevisiae.gff -b macs_output/ELF1_peaks.narrowPeak -u > macs_output/hits/ELF1_hits.gff

#Find the intersect of the CCL1 and ELF1 genes

bedtools intersect -a CCL1_hits.gff -b ELF1_hits.gff > CCL1_ELF1_hits.gff
