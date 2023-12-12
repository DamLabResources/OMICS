# Intro to Microbiome Analysis

## Introduction

Microbiome analysis is the study of the composition of microbial organisms that 
make up a community in some region. The region can be anything from lake beds, atmosphere,
soil, tap water, to oral swabs.  There are many organisms that can be measured in a microbiome
however we will be focusing on bacteria.  This requires us to identify a 'marker gene', in 
our case we will be using the whole 16S subunit of the Ribosome

## Learning Objectives

### Microbiome Sequence Clustering

By the end of class today you should be able to comfortably answer these questions:
1. _Apply_ linux to create even more shortcuts
1. _Define_ the steps required to create an OTU table.
1. _Differentiate_ alpha, beta, and gamma diversity metrics and discuss what they attempt to measure?
1. _Apply_ your knowledge of linux to calculate gamma diversity
1. _Apply_ usearch to calculate two alpha diversity metrics
1. _Apply_ usearch to calculate two beta diversity metrics

### Linux Skillz

We will continue to use *linux* to shorten commands, and look at data
1. Soflinks! What are they? Why are they great and you should always use them? `man ln`
1. `grep` search files for strings of characters, incredibly useful `man grep`
1. `cut`  cut can slice columns out of a table. `man cut`
1. `column` column is a command in linux that formats tables 'nicely' `man column`
1. `alias` Alias allows you to create your own custom commands (run alone to list all aliases) `man alias`
1. `id` id shows your current id, and the numerical value associated with it by the linux system `man id`
1. `type` Check if a command name you want to use is already taken by the system `man type`
1. `head` and `tail` get lines from the top and bottom of a file, respectively
1. `wc` Count characters, words, and lines in your files "word count"
1. `sort` Sort elements in a file

## Datasets and Binaries

* Data is located here:
	- `~/share/courses/OMICS/wk12_dataset/sequences_for_clustering.fq`
	- `ln -s ~/share/courses/OMICS/wk15_dataset/16sMicrobial_ncbi_lineage.fasta`

* New Binaries needed for this assignment are located here:
	- `~/share/courses/OMICS/wk15_dataset/muscle5.1.linux_intel64`
	- `~/share/courses/OMICS/wk15_dataset/FastTreeDbl`

# Walkthrough

Some of the data we are going to be using takes long paths, and it is a pain to write those over and over.
Let's fix that with a few steps.

1. Continual linux:
	- Do the github dance, pull down the most recent changes enter the content/wk15 directory, then `make mk_sandbox`
		- This creates the directory `~/share/omics_sandbox/wk15/$USER` 
		- FYI the above path will work for every student as written - `$USER` is an environment variable set when you log in!
		- set an alias called `wk15` to a command that will chnage directory to the above directory
	- in your sandbox directory softlink the datafiles:
		- `ln -s ~/share/courses/OMICS/wk15_dataset/16sMicrobial_ncbi_lineage.fasta 16S_db.fa`
		- `ln -s ~/share/omics_sandbox/wk14/$USER/seqs.fq .`
		- `ln -s ~/share/omics_sandbox/wk14/$USER/no_chimera_otu.fa otus.fa`
		- `ln -s ~/share/omics_sandbox/wk14/jupyter-jpe39/otutab.tsv .`
	- Finally, lets link the new binaries we have for this week to our bin folders:
		- `ln -s ~/share/courses/OMICS/wk15_dataset/muscle5.1.linux_intel64 ~/bin/muscle`
		- `ln -s ~/share/courses/OMICS/wk15_dataset/FastTreeDbl ~/bin/fasttree`
		- `ln -s ~/share/courses/OMICS/wk15_dataset/mafft-linux64/mafft.bat ~/bin/mafft`
		- `cd ~/bin && ln -s ~/share/courses/OMICS/wk15_dataset/mafft-linux64/mafftdir`

1. Assign taxonomy to your OTUs, or link the otus.utax file from week 12:
	- `usearch -utax otus.fa -db 16S_db.fa -utaxout otus.utax -utax_cutoff 0.8 -strand both`

1. Create a multiple sequence alignment (MSA) of all your OTU sequences
	- We learned about a new way to incorporate phylogenetic information into our beta diversity statistic
	- In order to do that, we need to align each OTU together, so we can build a tree first.
		- `mafft otus.fa > otus.aln`
	- NOTE: This aligns our sequences very fast!  Almost... suspiciously fast.  This is because mafft relies on 
	- several heuristics to speed things up.  We don't have a lot of time in class to wait for a 'good' alignment
	- so we are going with the 'rough and ready'.  If you wanted a more accurate alignment, there are much better options.
	- Meanwhile we have an alignment!  We could build a tree at this point, but it would be incomprehensible once made.
	- The reason for this is that the headers have ';' characters.  These are 'special' characters in the newick string
	- format - which we will be using.  So we need to get rid of those.  Don't think about this too much, but run this command:
		- `perl -pi.bak -e 's/;[^;]+;//' otus.aln`
		- BONUS: figure out how that command works.  HINT: Ask Deb, I hear she likes perl ;-)

1. Create a phylogenetic tree
	- Now that we have a MSA that doesn't have pesky semicolons in the headers we can make a tree.
	- `fasttree -nt otus.aln >otus.tree`

1. Lets view the tree
	- Download your tree file locally
	- A handy tree viewer program is figtree - download it for your OS of choice 
	- https://github.com/rambaut/figtree/releases
	- As long as you have java installed (and you aren't using linux) this should amount to downloading it and double-clicking
	- If you don't have java installed you can get it here (you need the JRE)
		- https://www.java.com/en/
		- if you are using linux, talk to a prof
	- finally, midpoint root your tree by clicking on the 'Trees' dropdown, click the checkmark next to 'Root tree', then next to 'Rooting:' select 'Midpoint'
	- Export the tree as `otus_figtree.tree` and upload it back to the jupyter server. File->Export Trees->Newick-Save as currently displayed->OK


1. Beta Diversity 2.0
	- We talked about unifrac distance and how it incorporates phylogenetic information into community comparison
	- Let's calculate it on our samples:
		- `usearch11 -beta_div otutab.tsv -metrics unifrac -tree otus_figtree.tree`

1. Subsetting
	- sometimes it is very useful to pull out subsets of our sequences/otus.  
	- Usearch makes this fairly easy with the command [fastx_getseqs](https://www.drive5.com/usearch/manual/cmd_fastx_getseqs.html)
	- Lets pull out every sequence from the database from the genus Staphylococcus
	- create a file called 'my_species.txt' add one line to it which is just the word 'Staphylococcus' save the file
	- `usearch11 -fastx_getseqs 16S_db.fa -labels my_species.txt  -label_substr_match -fastaout staph.fa`
	- tada! a fasta file with just the staph species.

# Tests
1. Using the utax table, count the number of each species found among the OTUs
	- hint: linux commands `sort`, `uniq -c` 
Command I used: 'cut -f2 otus.utax | cut -d ',' -f7 | cut -d '(' -f1 | sort| uniq -c| sort| less -S'

	- What species happens most frequently? If it is more than one, why would multiple OTUs be classified as the same species?
7 OTUs classified as Anaerococcus_octavius 
4 OTUs classified as Staphylococcus_epidermidis and 3 OTUs classified as Porphyromonas_catoniae

Species classification is not based solely on 16S sequence identity, but that was how we made the OTUs
Bacteria with different 16S sequences but similar other traits might be different OTUs but classified as the same species

1. Using the same file, calculate the number of each genera found
	- What is the most abundant genus?
cut -f2 otus.utax | cut -d ',' -f6 | cut -d '(' -f1 | sort| uniq -c| sort| less -S
14 g:Anaerococcus, 14 g:Prevotella, and 13 g:Corynebacterium

1. Pull out all the OTUs from the most abundant genus from the otus.fa file.  
grep 'Anaerococcus' otus.utax  > Anaerococcus_otus.utax

1. Now get all the species from that genus from the 16S_db.fa file.
usearch11 -fastx_getseqs 16S_db.fa -labels my_species.txt  -label_substr_match -fastaout Anaerococcus.fa
18 species found in 16S database by 'grep 's:' Anaerococcus.fa' 
>gi|636559445|ref|NR_115504.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_hydrogenalis;strain=GIFU_7662;complete=no;16sDatabaseName=same;
>gi|636559447|ref|NR_115506.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_tetradius;strain=GIFU_7672;complete=no;16sDatabaseName=same;
>gi|636559454|ref|NR_115513.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_lactolyticus;strain=GIFU_8586;complete=no;16sDatabaseName=same;
>gi|636559444|ref|NR_115503.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_prevotii;strain=GIFU_7658;complete=no;16sDatabaseName=same;
>gi|636559449|ref|NR_115508.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_vaginalis;strain=GIFU_12669;complete=no;16sDatabaseName=same;
>gi|219846768|ref|NR_026360.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_octavius;strain=NCTC_9810;complete=no;16sDatabaseName=same;
>gi|343201181|ref|NR_041937.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_vaginalis;strain=CCUG_31349;complete=no;16sDatabaseName=same;
>gi|343201183|ref|NR_041939.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_prevotii;strain=CCUG_41932;complete=no;16sDatabaseName=same;
>gi|343201184|ref|NR_041940.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_lactolyticus;strain=CCUG_31351;complete=no;16sDatabaseName=same;
>gi|343201185|ref|NR_041941.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_tetradius;strain=CCUG_46590;complete=no;16sDatabaseName=same;
>gi|636559827|ref|NR_115887.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_murdochii;strain=WAL_17230;complete=no;16sDatabaseName=same;
>gi|631251831|ref|NR_113029.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_hydrogenalis;strain=JCM_7635;complete=no;16sDatabaseName=same;
>gi|672238984|ref|NR_125573.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_pacaensis;strain=9403502_16S;complete=no;16sDatabaseName=same;
>gi|645321194|ref|NR_118220.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_senegalensis;strain=JC48_16S;complete=no;16sDatabaseName=same;
>gi|631252367|ref|NR_113565.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_lactolyticus;strain=JCM_8140;complete=no;16sDatabaseName=same;
>gi|645321332|ref|NR_118323.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_obesiensis;strain=ph10_16S;complete=no;16sDatabaseName=same;
>gi|631253116|ref|NR_114314.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_vaginalis;strain=JCM_8138;complete=no;16sDatabaseName=same;
>gi|444304151|ref|NR_074575.1;tax=d:Bacteria,p:Firmicutes,c:Tissierellia,o:Tissierellales,f:Peptoniphilaceae,g:Anaerococcus,s:Anaerococcus_prevotii;strain=DSM_20548;complete=yes;16sDatabaseName=same;

Note multiple reference sequences for vaginalis, prevotii, lactolyticus, hydrogenalis, and tetradius

	- Fix the headers so they do not have semicolons, but do have the species name for both OTU file and database file.
Did 'perl -pi.bak -e 's/;/_/' Anaerococcus_otus.utax' twice until I didn't see semicolons by 'head', then confirmed lack of semicolons with grep 
Did 'perl -pi.bak -e 's/;/_/' Anaerococcus.fa' (16S database) about five times until I didn't see semicolons by 'head', then confirmed lack of semicolons with grep 

Made Anaerococcus_otus_list.txt:
OTU_10_size=7032_
OTU_11_size=2688_
OTU_16_size=432_
OTU_33_size=53_
OTU_70_size=984_
OTU_97_size=9_
OTU_106_size=3_
OTU_123_size=8_
OTU_137_size=13_
OTU_176_size=19_
OTU_177_size=11_
OTU_178_size=1_
OTU_239_size=3_
OTU_305_size=10_

Then 'usearch11 -fastx_getseqs otus.fa -labels Anaerococcus_otus_list.txt -label_substr_match -fastaout AnaerococcusOtusSeqs.fa'

	- Align all sequences
OTU sequences: 
'mafft AnaerococcusOtusSeqs.fa > Anaerococcus.aln'

16S database sequences: (where Anaerococcus.fa was a subset of the 16S database similar to the staph.fa described above)
'mafft Anaerococcus.fa > AnaerococcusDB.aln'

Combining them: cat did not produce a file recognized as aligned by fasttree but did produce a file with sequences in it recognized by seqkit stats. 
'cat Anaerococcus.aln AnaerococcusDB.aln > allAnaerococcus.aln' 
followed by 
'mafft allAnaerococcus.aln > allAnaerococcusAligned.aln' 

	- Make a phylogenetic tree
	- Examine the tree - Where would you expect the OTU sequences to be place in the tree, relative to the database sequences?
OTU sequences and database sequences overlap and are similar to each other

	- Does the tree appear as you expected?  If there are differences, what may be happening?
Tree appears as I expected

1. Plot the Unifrac distance matrix using either PCA or a heatmap
	- hint: excel has 'conditional formatting' that might make this easy. 
Added to git repository in OMICS/content/wk15 as unifrac_sorted.png
	- compare this to the euclidean distance you calculated last class. 
order after sorting is different; degree of clustered similarities and differences is comparable
	- Do the matrices agree with each other?  Compare/contrast the methods and explain what you observe

Combining them: cat did not produce a file recognized as aligned by fasttree but did produce a file with sequences in it recognized by s>
'cat Anaerococcus.aln AnaerococcusDB.aln > allAnaerococcus.aln'
followed by
'mafft allAnaerococcus.aln > allAnaerococcusAligned.aln'

        - Make a phylogenetic tree
        - Examine the tree - Where would you expect the OTU sequences to be place in the tree, relative to the database sequences?
OTU sequences and database sequences overlap and are similar to each other

        - Does the tree appear as you expected?  If there are differences, what may be happening?
Tree appears as I expected; some OTUS are more similar to each other than to any reference sequence because they might not be well-characterized

1. Plot the Unifrac distance matrix using either PCA or a heatmap
        - hint: excel has 'conditional formatting' that might make this easy.
Added to git repository in OMICS/content/wk15 as unifrac_sorted.png
        - compare this to the euclidean distance you calculated last class.
order after sorting is different; degree of clustered similarities and differences is comparable
        - Do the matrices agree with each other?  Compare/contrast the methods and explain what you observe
some similarities and some differences; both have the property that things are zero difference from themselves; I tried plotting euclidean distance (from each other sample) for a few randomly selected samples and euclidean distance seemed to have weak positive correlations to unifrac distance