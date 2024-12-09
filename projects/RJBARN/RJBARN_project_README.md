# Introduction 
I will be working on a project that is analyzing HIV provirus data.
The data for this project is located: /home/jupyter-jb4622/share/jordan/OMICS/data. 
The files contain HIV provirus sequencing data from two individuals (T78276, T96768). Tissue samples include right middle fontal gyrus (MFG), spleen (SPL), and cerebrum (CER). 
# Literature Review 

# Methodology

## Stats for the data samples:
|file|    format|  type|    num_seqs|        sum_len| min_len| avg_len| max_len| Q2|      Q2|      Q3|      sum_gap| N50|     Q20(%)|  Q30(%)|  GC(%)|
|---|-----------|------|------------|--------------|--------|--------|---------|----|-------|--------|--------------|----|---------|--------|-------|
|T78276-MFG.fq.gz|        FASTQ|   DNA|     5175|    4342958| 200|             839.2|   4896|    410.0|   665.0  | 979.0  | 0 |      972 |    69.37 |  18.16 |  43.58|
|T78276-SPL.fq.gz|        FASTQ|   DNA|     112008|  100002604|       200|     892.8|   9413|    593.0|   607.0  | 1012.0 | 0 |      1008 |   71.72 |  8.33  |  46.91|
|T96768-CER.fq.gz|        FASTQ|   DNA|     2777 |   2684381| 200|             966.6|   8589|    258.0|   352.0  | 515.0  | 0 |      6921 |   64.80 |  8.75  |  45.22|
|T96768-MFG.fq.gz|        FASTQ|   DNA|     99337|   100000365|       200|     1006.7|  3306|   550.0 |  560.0  | 1961.0 | 0  |     1959  |  71.79  | 7.33   | 47.44|
|T96768-SPL.fq.gz|        FASTQ|   DNA|     17908|   100000208|       200|     5584.1|  7772|    4259.0|  7055.0 | 7087.0 | 0 |      7071 |   71.56 |  9.35  |  41.63|

## Aligning and Indexing
### index the genome
These are long read data, so we will use minimap. Minimap creates its own index as part of the command so there is no need to separately index the genome. 
### create a sym link to the ref genome
ln -s ~/share/refs/HXB2F/hxb2f.fasta ./
### map long reads to reference genome
minimap2 -a ./refs/hxb2f.fasta data/T78276-MFG.fq.gz | samtools view -b | samtools sort > aligns/T78276-MFG.sorted.bam
minimap2 -a ./refs/hxb2f.fasta data/T78276-SPL.fq.gz | samtools view -b | samtools sort > aligns/T78276-SPL.sorted.bam
minimap2 -a ./refs/hxb2f.fasta data/T96768-CER.fq.gz | samtools view -b | samtools sort > aligns/T96768-CER.sorted.bam
minimap2 -a ./refs/hxb2f.fasta data/T96768-MFG.fq.gz | samtools view -b | samtools sort > aligns/T96768-MFG.sorted.bam
minimap2 -a ./refs/hxb2f.fasta data/T96768-SPL.fq.gz | samtools view -b | samtools sort > aligns/T96768-SPL.sorted.bam
### create a bam.bai index file
samtools index T78276-MFG.sorted.bam
(repeated for each of the samples)

## Create snpEFF database for HXB2F HIV genome (directory: /home/jupyter-jb4622/share/jordan/OMICS/project)
### edit config file to match directory pathways and names. build genome from genbank file
snpEff build -genbank -v hxb2f

## Create vcf files for each sample:
### run the following command for each sample
sh bcf_command.sh ~/share/jordan/OMICS/project/data/aligns/T78276-MFG.sorted.bam  ./T78276-MFG.bcf
bcftools view T78276-MFG.bcf > T78276-MFG.vcf
bcftools view T78276-SPL.bcf > T78276-SPL.vcf
bcftools view T96768-CER.bcf > T96768-CER.vcf
bcftools view T96768-MFG.bcf > T96768-MFG.vcf
bcftools view T96768-SPL.bcf > T96768-SPL.vcf

## gz zip and index vcf files
bgzip T78276-MFG.vcf
bgzip T78276-SPL.vcf
bgzip T96768-CER.vcf
bgzip T96768-MFG.vcf
bgzip T96768-SPL.vcf

bcftools index T78276-SPL.vcf.gz
bcftools index T78276-MFG.vcf.gz
bcftools index T96768-CER.vcf.gz
bcftools index T96768-MFG.vcf.gz
bcftools index T96768-SPL.vcf.gz
 
## merge vcf files
bcftools merge T78276-MFG.vcf.gz T78276-SPL.vcf.gz T96768-CER.vcf.gz T96768-MFG.vcf.gz T96768-SPL.vcf.gz -o merged_all_samples.vcf.gz

## Run snpEFF (directory: /home/jupyter-jb4622/share/jordan/OMICS/project)
### no filter
snpEff -v -stats merged_all_samples.html hxb2f data/vcf/merged_all_samples.vcf.gz > merged_all_samples.ann.vcf

### remove up/downstream and introns in analysis
snpEff -ud 0 -no-intron -v -stats merged_all_samples_ud-0_no_intron.html hxb2f data/vcf/merged_all_samples.vcf.gz > merged_all_samples_ud-0_no_intron.ann.vcf

## Adjust and save variant files
### view the variants only and save as a new file
bcftools view -v snps data/snpEff_output/merged_all_samples/merged_all_samples_ud-0_no_intron.ann.vcf > merged_samples_ud-0_no_intron_var_only.ann.vcf

### install SnpSift
I added snpsift to my own venv by updating the macs.yaml file and then deleting the macs/ file and recreating the venv and then activated the environment using these two commands:
mamba env create -p macs --file macs.yaml
conda activate /home/jupyter-jb4622/venv/macs

### use SnpSift to save a file with samples that have HIGH impact and Quality >=20:
SnpSift filter "ANN[*].IMPACT has 'HIGH' && ( QUAL >= 20 )" data/snpEff_output/merged_all_samples/merged_all_samples_ud-0_no_intron_var_only.ann.vcf > merged_all_samples_ud-0_no_intron_var_only.ann.filter_HIGH_Q20.vcf


# Results

# Discussion

# Conclusion

# References
