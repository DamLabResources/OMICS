## Mary Marino Week 14 Assignment

1. I often use '.tsv' as the extension for many of the above files. Linux doesn't care what extensions files have, unlike windows and other operating systems. Why do you think I add '.tsv' instead of just '.txt' to my input/output files? (or even leave it off?)
- A table format is much easier to view and extrapolate data from.

2. Calculate the number of samples in your otu table
- i.e. how many columns are there? (minus the first OTU ID column)
	- There are 148 columns (aka samples) in my OTU table.
	- Command: `head -n 1 otutab.tsv | tr -s '\t' '\n' | wc -l` (via ChatGPT)

3. Alpha Diversity
- Fix this command so it orders the table correctly: `cut -f1,10 alpha.txt|sort -k2 |column -ts $'\t'|less -S` (Don't worry about the column header for this)... hint: man sort
	- New command: `cut -f1,10 alpha.tsv | sort -n -k2,2 -t$'\t' | column -ts $'\t' | less -S`
- Sort the whole table by the 'reads' column (the number of reads belonging to that sample)
	- New command: `cut -f1,9 alpha.tsv | sort -n -k2,2 -t$'\t' | column -ts $'\t' | less -S`
- Examine the 'richness' - is there any correlation between the number of reads ('observations') a sample has and the species richness? What is it and why? What test might you perform to see if there is a significant correlation? Why might a correlation be a problem in this kind of analysis?
	- Samples with higher numbers of reads seem to also have higher species richness… This is not the case for all samples, however.
	- This is because richness constitutes the total number of species within a sample – this number is affected by the sampling number. If there are more total numbers of species in a sample, you will get a higher number of reads!
	- Source: https://www.sciencedirect.com/science/article/pii/S2001037021005456
		- "As a higher overall read count (sequencing depth) increases the chance of detecting rare sequences, richness is positively correlated with sequencing depth.” → aka, richness is positively correlated with overall read count!
- Shannon_e's diversity takes into account both the number of species, but also the relative abundance of each species. You can think of it as 'If this sample were evenly composed of THIS NUMBER of species it would give you this value'.
	- Pull out the richness, reads, and shannon_e columns. Compare these values. Would you have expected to see what you do? What is your conclusion about the samples given the richness vs shannon_e values in regards to how consistent richness and shannon's correlate with one another?
		- Richness, reads, and shannon_e columns were pulled out of the table using Google Colab.
		- When comparing the values, it shows that richness and the shannon_e's diversity are also positively correlated!

4. Gamma Diversity
- Calculate the gamma diversity (richness) for this dataset
	- There are 305 total OTU's, which corresponds to the gamma diversity.

5. Beta Diversity
- Examine the 'pretty' version of the sorted euclidean distance file - what is striking about the diagonal values? Explain why this phenomenon exists. (diagonal == starting in the top left and moving down-one, over-one)
	- The diagonal values are equal to zero. This is because we are comparing two samples that are exactly the same. The number zero reflects that there are no differences between the two samples as they intersect on the graph, forming the diagonal line.
- What are two ways to present this data graphically?
	- This data can be presented graphically as a heatmap or a phylogenetic tree.
- Make a graph! import either the euclidean or bray-curtis matrix into your favorite spreadsheet editor and calculate some representation of that measure.
	- Graph created in Excel.
- Do the samples create separate groups? Do they not? What does it say about the underlying sample data?
	- The samples create separate groups, but there are both similarities and differences between the samples in them.
