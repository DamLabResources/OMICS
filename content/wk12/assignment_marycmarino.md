
## Mary Marino Wk12 Assignment

1. What is the output of this command: `usearch --version` ?
	- usearch v8.1.1861_i86linux64
2. Softlink the data file ~/share/courses/OMICS/wk12_dataset/sequences_for_clustering.fq so that it is ~/share/omics_sandbox/wk12/user/seqs.fq
	- `ln -s ~/share/courses/OMICS/wk12_dataset/sequences_for_clustering.fq ~/share/omics_sandbox/wk12/jupyter-marycmarino/seqs.fq`
	- Testing the run: `ls -lh ~/share/omics_sandbox/wk12/jupyter-marycmarino/`
	- seqs.fq is represented in the directory by: `seqs.fq -> /home/jupyter-marycmarino/share/courses/OMICS/wk12_dataset/sequences_for_clustering.fq`
3. There are 168255 sequences in the seqs.fq file. I used `head seqs.fq` to determine how each sequence was labeled and then `grep -c '^@m'` to search for the number of sequences.
4. After running the dereplicate command (step 5 in the walkthrough), a 'size' variable is added to the fasta header in the file seqs_derep.fa ...
	- This represents the size of the sequences as we dereplicate them.
	- This is relevant to our OTU clustering step because it allows us to determine the unique sequences of each sample, which allows us to tell the differences in their abundance.
5. After running the dereplicate command (step 5 in the walkthrough), how many sequences exist in the output fasta file seqs_derep.fa?
	- The commands I used: `head seqs_derep.fa` followed by `grep -c '^>m' seqs_derep.fa`
	- The result: 157474
6. After clustering OTUs (step 6 in the walkthrough), how many sequences exist in the output fasta file otu.fa?
	- There are 310 sequences in the output fasta file otu.fa.
7. What is a 'chimera' and how many were found in this dataset after step 6?
	- A chimera is a DNA sequence comprised of several DNA sequences that were erroneously joined together.
	- There were 1170 chimeras found in the data set after step 6.
8. After step 7 how many additional Chimeras were found?
	- There were 5 more chimeras found in the data set after step 7.
9. After step 8, what are the top 20 organisms found in this dataset?
	- The top 20 organisms are:
		1. Staphylococcus
		2. Peptoniphilus
		3. Corynebacterium
		4. Gordonia
		5. Prpionivibrio
		6. Simonsiella
		7. Anaerococcus
		8. Streptococcus
		9. Stenoxybacter
		10. Actinobacillus
		11. Haemophilus
		12. Neisseria
		13. Clostridium
		14. Anaerosphaera
		15. Granulicatella
		16. Actinomyces
		17. Halomonas
		18. Exiguobacterium
		19. Barnesiella
		20. Rikenella
