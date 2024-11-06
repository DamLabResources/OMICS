Now that we have MACS properly installed.
Explore the documentation at https://macs3-project.github.io/MACS/index.html.

Task (45 minutes):
 - Use `macs3` to get the following things for the CLL1 & ELF1 pulldown experiment.
   - When running `macs3`, ensure you are using "paired end" mode and include the notag sample as a control.
   - A `bedGraph` file showing the coverage across the genome.
   - A `bed` file of peaks where TFs bind binds more than expected.
   - Download these for IGV.
 - Are any genes modulated by both CCL1 and ELF1.
   - Use `bedtools` and `saccharomyces_cerevisiae.gff` to find all hits within the 1000 bp upstream of a gene.
   - Intersect the list of genes between the two sets.
   - Export a `bed` file for IGV.



Updates from some of the commands that were used in class:

bedools window -l 1000 -r -0 -a ~share/refs/...gfffile -b ~share/....peaksfile 




this is how you look at either CCL1 or ELF1 

you can make your peaks file, or bed graph and load these into IGV and you can look around and see what 
- treatment pile up 
- control pile up 
- peaks file 
- narrow peaks 
- summits 

LOAD all of these into IGV
- bam file is not required for this 


