## Notes for Week 5 assignment

seqkit stats multiplexed.fq
num_seqs = 1900

## Generating fastq files

seqkit grep -C -s -p 'ACCT.CCAG' multiplexed.fq -- yields number 0
seqkit grep -C -s -p 'ACCT.CCAG' multiplexed.fq > ~/repos/OMICS2024/content/wk05/solution/SRR23803536.fastq
saving to file just shows 0

seqkit grep -s -p 'ACCT.CCAG' multiplexed.fq -- yields nothing
saving to file is blank

seqkit seq multiplexed.fq -- yields full sequence... getting closer!

seqkit grep -s -r -p 'ACCT,CCAG' multiplexed.fq > ~/repos/OMICS2024/content/wk05/solution/SRR23803536.fastq
-r makes it read the thingy as a regular expression
it NEEDS to be a comma or it gets confused
repeat for all samples and copy to according fastq

## Generating fastq files correctly
The above stuff straight up does not work LOL disregard
per regan's help:
seqkit grep -s -r -i -p ^ACCT multiplexed.fq | seqkit grep -s -r -i -p CCAG$ -o solution/SRR23803536.fastq

## Trimming the sequences
per regan's help:


	sample_name
1	SRR23803536
2	SRR23803537
3	SRR23803538
4	SRR23803539