## in-class work

## Copy the reads and reference files to a working directory in your home.

cp ~/share/OMICS/wk07/refs/* refs
cp ~/share/OMICS/wk07/reads/* reads

## Use seqkit stats to describe the reads.
seqkit stats T78276-MFG.small.fq.gz
seqkit stats T78276-SPL.small.fq.gz

## Use minimap2 to align the reads from each sample to the K03455 genome.

minimap2 -ax sr refs/K03455.fasta reads/T78276-MFG.small.fq.gz > aligned_T78276-MFG.sam

minimap2 -ax sr refs/K03455.fasta reads/T78276-SPL.small.fq.gz > aligned_T78276-SPL.sam

## Use samtools to convert to a sorted bam file with an index.
samtools view -b aligned_T78276-MFG.sam > aligned_T78276-MFG.bam
samtools view -b aligned_T78276-SPL.sam > aligned_T78276-SPL.bam
samtools index refs/K03455.fasta 
samtools sort aligned_T78276-MFG.bam > aligned_T78276-MFG.sorted.bam
samtools sort aligned_T78276-SPL.bam > aligned_T78276-SPL.sorted.bam

samtools view -b -q 20 aligned_T78276-MFG.sorted.bam > aligned_T78276-MFG.sorted.filtered.bam
samtools view -b -q 20 aligned_T78276-SPL.sorted.bam > aligned_T78276-SPL.sorted.filtered.bam


samtools index aligned_T78276-MFG.sorted.filtered.bam
samtools index aligned_T78276-SPL.sorted.filtered.bam


## Count the number of aligned records that map to the genome with at least a MAPQ>20.

samtools view -q 20 -c aligned_T78276-MFG.sorted.bam > aligned_T78276-MFG.sorted.filtered.bam
samtools view -b -q 20 -c aligned_T78276-SPL.sorted.bam > aligned_T78276-SPL.sorted.filtered.bam

# exclude the secondary and supplemental reads
samtools view -c -F 256 aligned_T78276-MFG.sorted.filtered.bam

samtools view -c -F 2048 aligned_T78276-MFG.sorted.filtered.bam
 
samtools view -c -F 256 aligned_T78276-SPL.sorted.filtered.bam

samtools view -c -F 2048 aligned_T78276-SPL.sorted.filtered.bam

