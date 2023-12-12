# Mary Marino Method# Mary Marino Project Data
### Last updated: 2023-10-09 for Week 6 Assignments

## Example Commands
`example command`

## File Hierarchy and Links
* Main Project README: [README.md]
* Original files shared with me by Leanie: [RDSLR]
* Reference genome, bwa index, and copies of the original files that I actually plan to use: [refs]
* Concatenated files: [concat_files]
* Aligned files: [aligned_files]
* Scripts that allowed me to concatenate and align my files: [scripts]

## Analysis Steps
1. Concatenate desired files together
2. Align files to reference genome
3. Calculate coverage estimations
4. Variant calling – make a .bcf file from my .bam files
	```
	bcftools mpileup -f refs/RdKW20.fasta aligned_files/RdKW20bio24hr5_S188.concat.bam | bcftools call -mv -Ob -o Rdbio5_calls.bcf
	bcftools view Rdbio4_calls.bcf | less -S
	bcftools stats Rdlog6_calls.bcf | less -S
	```
5. Try making a pipeline
