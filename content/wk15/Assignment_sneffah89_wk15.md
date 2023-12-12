  ## Question 1
**i** count the number of each species found among the OTUs

Using the command `cut -d',' -f8 otus.utax.csv | sed 's/[^a-zA-Z ]//g' | tr ' ' '\n' | sort | uniq -c | sort -nr | head -n10` This command helped generate a list of species found among the OTUs and their counts (number to the left)
      7 sAnaerococcusoctavius
      
      4 sStaphylococcusepidermidis
      
      3 sPorphyromonascatoniae
      
      2 sStanieriacyanosphaera
      
      2 sSnodgrassellaalvi
      
      2 sSegetibacteraerophilus
      
      2 sPrevotellahisticola
      
      2 sPeptoniphilusgrossensis
      
      2 sPeptoniphiluscoxii
      
      2 sParvimonasmicra

**ii** What species happens most frequently? If it is more than one, why would multiple OTUs be classified as the same species?

Using `cut -d',' -f8 otus.utax.csv | sed 's/[^a-zA-Z ]//g' | tr ' ' '\n' | sort | uniq -c | sort -nr | head -n1` the most abundant specie is `Anaerococcus octavius`

classification of multiple OTUs as the same species can result from the closely of related strains or species, the methods used for OTU clustering, the quality and completeness of reference databases

## Question 2
**I** Calculate the number of each genera found 

Using the command `cut -d',' -f7 otus.utax.csv | sed 's/[^a-zA-Z ]//g' | tr ' ' '\n' | sort | uniq -c | sort -nr | head -n10`. Below are the top 10  genera and their numbers/count beside it on the left
     14 gPrevotella
     
     14 gAnaerococcus
     
     13 gCorynebacterium
     
      9 gActinomyces
      
      8 gStaphylococcus
      
      8 gPeptoniphilus
      
      6 gStreptococcus
      
      6 gPorphyromonas
      
      6 gLactobacillus
      
      6 gClostridium
      
**ii** The most abundant genus 

Using the command `cut -d',' -f7 otus.utax.csv | sed 's/[^a-zA-Z ]//g' | tr ' ' '\n' | sort | uniq -c | sort -nr | head -n2` the most abundant genus is tied between `Prevotella` and `Anaerococcus`

## Question 3
**i** OTUs from the most abundant genus from the otus.fa file.
In order to get all the OTUs of the most abundunct genus from the otus.fa file , i generated a list of all the OTUs in the genus `Prevotella`using the command below

`cut -d',' -f1,7 otus.utax.csv | grep 'Prevotella'`. Then i generated a `my_genus.txt file` which contains the OTUs of Prevotella.

Using the command `usearch11 -fastx_getseqs otus.fa -labels my_genes.txt  -label_substr_match -fastaout Prevotella_otus.fa` i obtained all the OTUs from the most abundant genus from the otus.fa file. `14` OTUs were found

**ii** Get all the species from that genus from the 16S_db.fa file.
In order to do this i generated a `species.txt` file which has a list of species names beginning with `s:Prevotella `then used the command below.

`usearch11 -fastx_getseqs 16S_db.fa -labels species.txt  -label_substr_match -fastaout New_Prevotella.fa`. 
`4` species from the genus `Prevotella` was found.

**iii** Fix the headers so they do not have semicolons, but do have the species name for both OTU file and database file.
In order to do this the commands below was used 

`perl -pi.bak -e 's/;[^;]+;//' Prevotella_otus.fa` for the OTU file 

For the databse file two commands were used                                                                                                                                                                                                                                                                                                                                                                             `perl -pi.bak -e 's/;[^;]+g:Prevotella//' New_Prevotella.fa`  and 

`perl -pi.bak -e 's/;[^;]+;//' New_Prevotella.fa`


**iv** Align all sequences. Make a phylogenetic tree
In order to align the sequences from OTU file and the database file i used the following commands

`mafft Prevotella_otus.fa > Prevotella_otus.aln`
`mafft New_Prevotella.fa > New_Prevotella.aln`

To actually generate the phylogenetic tree i used the following commands 

`fasttree -nt Prevotella_otus.aln >Prevotella_otus.tree`

Tree is attached 

`fasttree -nt New_Prevotella.aln >New.Prevotella.tree`

Tree is attached

**v** Examine the tree - Where would you expect the OTU sequences to be place in the tree, relative to the database sequences?
Does the tree appear as you expected? If there are differences, what may be happening?

Of all the 14 Prevotella species in the OTU file only 4 were found/receognized by the database. Therefore creating 4 sequences in the databse file. Again, of the four sequences in the database file two of them were given the species name Prevotella bivia. The other two Prevotella shahii (OTU_44) and Prevotella Salivae (OTU_275) from the database sequence were relatively at the same position in the phylogenetic tree as the OTU sequences. One of the  Prevotella bivia from the database sequence was also in the same relative position compared to the OTU sequence, however for the other Prevotella bivia, it looked like the OTU sequence had sub OTU classifications that is alien or not known to the database. 

## Question 4
Alter the fasta headers for the OTUs so that they include both a. the OTU designation, i.e. otu_1 b. the species assignment of utax?
The command below was still used 

`paste -d ' ' <(grep '^>' Prevotella_otus.fa) <(cut -d',' -f1,8 otus.utax.csv) | awk '/Prevotella/ {print $1" "$2" "$4}' > otu_with_species.fasta`

## Question 5
**i** Plot the Unifrac distance matrix using either PCA or a heatmap
To do this i created a Unifrac csv file using the command 

`tr '\t' ',' < unifrac.sorted.txt > unifrac.csv`

Then i used `seaborn and matplotlib.pyplot` in google colab to generate a heatmap
Figure is attached 

**ii** compare this to the compare this to the euclidean distance you calculated last class.
Do the matrices agree with each other? Compare/contrast the methods and explain what you observe

The euclidean distance matrix generated four separated/ distinct clusteres, However, for the unifrac distance matirx it generated two separated/distinct clusters 

The euclidean diastance matrix can use a varying type of numerical data making it fit for general purpose. This therefore makes it require normalization if variables have different units or scales. However, Unifrac is designed specifically for microbiome data and considers phylogenetic relationships







