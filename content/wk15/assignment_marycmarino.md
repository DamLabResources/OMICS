## Mary Marino Week 15 Assignment

1. Using the utax table, count the number of each species found among the OTUs. What species happens most frequently? If it is more than one, why would multiple OTUs be classified as the same species?
- Command used and result: 
```
sort -u -c otus.utax 
sort: otus.utax:3: disorder: OTU_4;size=14940;  d:Bacteria(95.6),p:Firmicutes(95.6),c:Bacilli(95.6),o:Lactobacillales(95.6),f:Carnobacteriaceae(71.8),g:Dolosigranulum(65.2),s:Dolosigranulum_pigrum(65.2)       *       +
```
- The species that occur most frequently are *Firmicutes*, *Bacilli*, *Lactobacillales*, *Carnobacteriacaeae*, and *Dolosigranulum*.
- Multiple OTUs could be classified as the same species if there is a less than 3% difference in the gene examined for the purposes of constructing this tree, but more differences in other areas of the genome.

2. Using the same file, calculate the number of each genera found. What is the most abundant genus?
- The genus that occurs most frequently when looking at the genera in the `otus.utax` file is *Dolosigranulum*.

3. Pull out all the OTUs from the most abundant genus from the otus.fa file. Now get all the species from that genus from the 16S_db.fa file.
- Examine the tree - Where would you expect the OTU sequences to be placed in the tree, relative to the database sequences?
	- Followed steps to organize and align sequences according to Walkthrough instructions.
	- I would expect the OTU sequences to cluster relatively closely together, since the species listed are all part of the same genus (compared to the first phylogenetic tree we made which included several genera).
- Does the tree appear as you expected? If there are differences, what may be happening?
	- Sort of – there is more variation than I expected. This could be due to genetic differences between strains in the *Dolosigranulum* genus.

4. Plot the Unifrac distance matrix using either PCA or a heatmap. Compare this to the euclidean distance you calculated last class.
- Do the matrices agree with each other? Compare/contrast the methods and explain what you observe.
	- I plotted the data as a heatmap using Google Colab.
	- The euclidean distance that I calculated during the Week 14 exercises was comparing two genetically identical strains, resulting in a distinct matrix pattern.
	- Since I am not comparing two identical strains in this heat map, the matrices do not exactly agree with each other.
