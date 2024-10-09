# Week 6: Notes
 
### Learning Objectives


##### - Understand the Burroughs-Wheeler Alignment (BWA) algorithm and its applications.
##### - Differentiate between BWA and other alignment algorithms (like BLAST).
##### - Understand why we should not put large result-files into git repos.
##### - Understand the purpose of generating alignment indexes.
##### - Use samtools to view and count the number of aligned reads.
##### - Use samtools flagstat to summarize an alignment result.
##### - Understand the important fields of a SAM format.








### Assignment


Create a `excercise/{user}/wk06/README.md`.
Use this to keep track of your commands and present your results.
Use the read files in `~/share/OMICS/wk06/reads`.

 - Sub-sample the first 100K from each set into a new file in your working directory. Remember to keep track of sample names and R1/R2s.
 - Use `bwa mem` to align these reads to the SGD genome.
 - Use `samtools view` to determine how many reads aligned from each sample at a Q30 threshold. Create a table in your README describing this.
 - Use `samtools depth` and determine the average depth across each chromosome in each sample. 
 - After alignment, sorting, and indexing, download them to your own computer and load them into IGV.
 - Use the IGV browser, find a region where there seems to be a amino-acid change between the three samples. Take a screenshot and add it to the Readme.
 - Do a brief search about the protein, is anything known? Write about it in the README.

#### Sub-sample the first 100K from each set into a new file in your working directory. Remember to keep track of sample names and R1/R2s.

1. I copied the data from the shared/OMICS/wk06/reads directory into my home directory. 
    `jupyter-aoe23@Mistake-Not:~/omics_aoe23/wk06/wk06_hw$ cp ~/share/OMICS/wk06/reads/* .`
    
2. then I took the first 100K of each by doing the following commands: 


      `seqkit head -n 100000 OGstrain_R1.fq.gz -o OGstrain_R1_100k.fq.gz`
      
      `seqkit head -n 100000 OGstrain_R2.fq.gz -o OGstrain_R2_100k.fq.gz`
      
      `seqkit head -n 100000 SF_aer_R1.fq.gz -o SF_aer_R1_100k.fq.gz` 
      
      `seqkit head -n 100000 SF_aer_R2.fq.gz -o SF_aer_R2_100k.fq.gz` 
      
      `seqkit head -n 100000 SF_ann_R2.fq.gz -o SF_ann_R2_100k.fq.gz` 
      
      `seqkit head -n 100000 SF_ann_R1.fq.gz -o SF_ann_R1_100k.fq.gz`


#### Use `bwa mem` to align these reads to the SGD genome.

 
3. note that first I had to copy the genome into this folder, to make it easier to use the full piped code so I did the first two steps: 

    `mkdir refs`
    
    
    
4. I already had the reference genome in my wk06 folder from working in class so I copied it to the new wk06/wk06hw file by doing this: 

    `cp ~/omics_aoe23/wk06/refs/* .`



5. I made an alns folder to push the alignments to before using bwa tool: 

    `mkdir alns`
    
    
    
6. Then I used the piped code to complete the alignment:

   `bwa mem refs/saccharomyces_cerevisiae.fa reads/OGstrain_R1_100k.fq.gz reads/OGstrain_R2_100k.fq.gz | samtools sort > alns/OGStrain100k.pipe.sorted.bam`
   
   `bwa mem refs/saccharomyces_cerevisiae.fa reads/SF_aer_R2_100k.fq.gz reads/SF_aer_R1_100k.fq.gz | samtools sort > alns/SF_aer_100k.pipe.sorted.bam`
   
   `bwa mem refs/saccharomyces_cerevisiae.fa reads/SF_ann_R2_100k.fq.gz reads/SF_ann_R1_100k.fq.gz | samtools sort > alns/SF_ann_100k.pipe.sorted.bam`
   
#### Use `samtools view` to determine how many reads aligned from each sample at a Q30 threshold. Create a table in your README describing this.   
   
   
7. I used the code to get the number of reads at Q30 (thank you ChatGPT)


    `samtools view -c -q 30 alns/OGStrain100k.pipe.sorted.bam`
    
    `samtools view -c -q 30 alns/SF_aer_100k.pipe.sorted.bam`
    
    `samtools view -c -q 30 alns/SF_ann_100k.pipe.sorted.bam`
    
    
    
8. Output from the reads aligned at each Q30 threshold: 



| OG Strain | SF Anaerobic | SF Aerobic |
|---|---|---|
|182307|184978|185103|


#### Use `samtools depth` and determine the average depth across each chromosome in each sample. 
10. I used the following code to use sam tools depth 

    `samtools depth -a alns/OGStrain100k.pipe.sorted.bam | awk '{sum[$1] += $3; count[$1]++} END {for (chr in sum) print chr, sum[chr] / count[chr]}'`
    
    `samtools depth -a alns/SF_ann_100k.pipe.sorted.bam | awk '{sum[$1] += $3; count[$1]++} END {for (chr in sum) print chr, sum[chr] / count[chr]}'`
    
    
    `samtools depth -a alns/SF_aer_100k.pipe.sorted.bam | awk '{sum[$1] += $3; count[$1]++} END {for (chr in sum) print chr, sum[chr] / count[chr]}'`



11. Then I pasted the readouts into ChatGPT to make a markdown table for me: 

| Chromosome | OG Strain | SF ann  | SF aer  |
|------------|-----------|---------|---------|
| chrI       | 2.2552    | 1.7537  | 2.6350  |
| chrII      | 2.0010    | 2.0316  | 1.8403  |
| chrIII     | 2.2957    | 2.0293  | 2.2956  |
| chrIV      | 1.8429    | 1.9549  | 1.5826  |
| chrV       | 2.1325    | 2.2670  | 2.0557  |
| chrVI      | 2.4013    | 2.6316  | 2.4847  |
| chrVII     | 1.9118    | 1.9273  | 2.4933  |
| chrVIII    | 2.0937    | 2.5820  | 1.9310  |
| chrIX      | 2.1484    | 2.7022  | 2.7124  |
| chrX       | 2.0692    | 2.1307  | 1.8229  |
| chrXI      | 2.1039    | 2.1251  | 1.9844  |
| chrXII     | 2.9006    | 1.9653  | 1.8713  |
| chrXIII    | 1.9471    | 1.9724  | 1.7696  |
| chrXIV     | 2.0814    | 2.5981  | 1.8829  |
| chrXV      | 1.9241    | 2.0537  | 1.7238  |
| chrXVI     | 1.9288    | 1.9566  | 1.6881  |
| chrmt      | 5.1878    | 0.6932  | 6.7219  |





#### After alignment, sorting, and indexing, download them to your own computer and load them into IGV.


12. First need to index each usign the code below: 


    `samtools index alns/OGStrain100k.pipe.sorted.bam`
    
    `samtools index alns/SF_aer_100k.pipe.sorted.bam`
    
    `samtools index alns/SF_ann_100k.pipe.sorted.bam`
    
    
13. Then downloaded them to my computer and put them in my Advanced Omics Folder/wk06hw

14. Copied over the .fa .fai .gff files from wk06 in class folder downloads and moved them over to wk06hw (because they were previously downloaded from in class assignment) 

15. Open IGV, and selected File > New session

16. ONCE IN IGV Follow these steps (from in class notes)

    ##### load genome
        - open igv
        - click genomes
        - click load genomes from file in the drop down
        - load .fa and .fai file at the same time using shift (make sure .fa is first)
 

    #### load track 
        - file
        - load from file 
        - select .gff file open 

    #### then load the rest of the data
        - file 
        - load from file
        - select .bam and .bam.bai file 


#### Use the IGV browser, find a region where there seems to be a amino-acid change between the three samples. Take a screenshot and add it to the Readme.


17. Once everything loaded in I zoomed in all the way and scrolled around using the bar at the top until I found something that didn't match with the rest. 

18. Then I took a screenshot with the snipping tool 

19. Then I renamed the screenshot and dragged it into my wk06 folder. 

20. Then I used this code to embed in my readme:

       ![Amino Acid Change Region](repos/OMICS/exercises/aoe23/wk06/wk06schreenshot.png)
       
21. To get info I clicked on the Gene Track in blue at the bottom and got the following info: 

        type: mRNA
        
        ID: YCR028C_id001
        
        Name: YCR028C_id001
        
        Parent: YCR028C
        
        transcript_id: SGD:S000293172
        
        -dbxref: RefSeq:NM_001178743.1
        
        conditions: YPD
        
---------------------------
        type: CDS
        
        Parent: YCR028C_id001,YCR028C_id002
        
        Name: YCR028C_CDS
        
        orf_classification: Verified
        
        protein_id: UniProtKB:P25621
    
 
        type: gene
        
        ID: YCR028C
        
        Name: YCR028C
        
        gene: FEN2
        
        so_term_name: protein_coding_gene
        
        Alias: FEN2
        
        Ontology_term: GO:0000324,GO:0000329,GO:0005886,GO:0006897,GO:0015233,GO:0015887,GO:0071944,SO:000023
        6
        Note: Plasma membrane H -pantothenate symporter 3B confers sensitivity to the antifungal agent fenpropimorph 3B relocalizes from vacuole to cytoplasm upon DNA replication stress
        
        display: Plasma membrane H -pantothenate symporter
        
        dbxref: SGD:S000000623
        
        orf_classification: Verified
        
        curie: SGD:S000000623
 
        type: chromosome
        
        ID: chrIII
        
        dbxref: NCBI:BK006937.2
        
        Name: chrIII



22. I used chat GPT to tell me what each item of the infomation above means. Again this helped me identify the function and the use of this protien: 

#### Breakdown of the Information:
##### Type: mRNA

- This indicates that the feature is an mRNA transcript. It’s the RNA copy of a gene that is translated into a protein.

##### ID: YCR028C_id001

- This is the unique identifier for this specific mRNA transcript. The "id001" suggests there may be multiple mRNA isoforms for the same gene.
##### Name: YCR028C_id001

- This is the human-readable name of the mRNA transcript, which corresponds to its ID.

##### Parent: YCR028C

- This indicates that this mRNA transcript is derived from the gene identified as YCR028C.

##### Transcript_id: SGD

- This provides a reference to the Saccharomyces Genome Database (SGD), linking to the specific transcript information for further details.

##### dbxref: RefSeq

- This is a cross-reference to the RefSeq database, providing a link to additional information about the mRNA in that database.

##### Conditions: YPD

- This indicates the conditions under which the mRNA was expressed, in this case, YPD (a rich yeast growth medium).

##### Type: CDS

- This indicates a Coding Sequence (CDS), which is the part of the mRNA that is translated into a protein.

##### Parent: YCR028C_id001,YCR028C_id002

- This suggests that this CDS is associated with multiple mRNA transcripts (at least two: id001 and id002).

##### Name: YCR028C_CDS

- This is the name of the coding sequence.

##### Orf_classification: Verified

- This indicates that the open reading frame (ORF) has been verified to encode a protein.

##### Protein_id: UniProtKB

- This is a cross-reference to the UniProt database, providing the protein identifier associated with this CDS.

##### Type: gene

- This indicates that the entry describes a gene.

##### ID: YCR028C

- This is the unique identifier for the gene, FEN2.

##### Name: YCR028C

- This is the human-readable name for the gene, corresponding to its ID.

##### Gene: FEN2

- This specifies the name of the gene, FEN2.

##### So_term_name: protein_coding_gene

- This indicates that the gene is classified as a protein-coding gene according to Sequence Ontology (SO) terminology.

##### Alias: FEN2

- This confirms that FEN2 is an alternate name for this gene.

##### Ontology_term: GO:0000324,GO:0000329,GO:0005886,GO:0006897,GO:0015233,GO:0015887,GO:0071944,SO:0000236

- These are Gene Ontology (GO) terms associated with the gene, indicating its biological processes, molecular functions, and cellular components. Each term can be looked up for more detailed functional annotation.

##### Note:

- A note summarizing the function of the protein, describing its role as a plasma membrane H-pantothenate symporter that is involved in conferring sensitivity to the antifungal agent fenpropimorph and relocalization during DNA replication stress.
##### Display: Plasma membrane H-pantothenate symporter

- This describes the function of the protein, indicating it’s involved in transporting pantothenate across the plasma membrane.

##### Dbxref: SGD

- A cross-reference to the Saccharomyces Genome Database, linking to more information about the gene.

##### Orf_classification: Verified

- This reaffirms that the open reading frame is verified.

##### Type: chromosome

- This indicates that the feature is a chromosome.

##### ID: chrIII

- This confirms the identifier for Chromosome III.

##### Dbxref: NCBI

- A cross-reference to NCBI that links to detailed information about Chromosome III.
##### Name: chrIII

- The name of the chromosome.


### Summary of the Protien of Interest: 
### UniProtKB:P25621


##### I looked up this gene, and found a summary of its function here: https://www.alliancegenome.org/gene/SGD:S000000623 I copied the details into Chat GPT to make a nice summary table in md format pasted below. 


| **Attribute**                      | **Details**                                                                                                                                                                                                                           |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Species**                        | Saccharomyces cerevisiae                                                                                                                                                                                                              |
| **Symbol**                        | FEN2                                                                                                                                                                                                                                   |
| **Name**                          | FENpropimorph resistance                                                                                                                                                                                                             |
| **Synonyms**                     | YCR028C                                                                                                                                                                                                                                 |
| **Biotype**                      | protein coding gene                                                                                                                                                                                                                   |
| **Automated Description**         | Enables pantothenate transmembrane transporter activity. Involved in endocytosis and pantothenate transmembrane transport. Located in plasma membrane. Human ortholog(s) of this gene implicated in autosomal dominant nonsyndromic deafness 25; gout; porokeratosis; and sialuria. Orthologous to several human genes including SLC17A1 (solute carrier family 17 member 1); SLC17A2 (solute carrier family 17 member 2); and SLC17A3 (solute carrier family 17 member 3). |
| **SGD Description**               | Plasma membrane H+-pantothenate symporter; confers sensitivity to the antifungal agent fenpropimorph; relocalizes from vacuole to cytoplasm upon DNA replication stress                                                                   |
| **Cross References**              | NCBI_Gene:850394, UniProtKB:P25621                                                                                                                                                                                                  |

