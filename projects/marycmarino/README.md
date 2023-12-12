# Mary's Project README
### Last updated: 2023-12-11

### My Data
* Name: RDSLR
* Received from: Leanie Williams and the Mell Lab at Drexel University
* Subject: examining RNA seq data relating to expression of genes in *Haemophilus influenzae* strains containing or not containing Sel1-like repeats
* For more information: [data.md](data.md)

## Important Commands Used in This Project
* cd - change directories
* . = stay where you are
*  .. = move up one directory
* cd ~/ (start typing) (hit tab) —> it will autocomplete!
* clear = delete everything in your terminl
* pwd - path to working directory
* ls - list
* man - manual for your command
* wc - word counts
* history - view your command history from that terminal (but don't count on it to check what you've worked on, keep thorough notes!)
* clear - delete everything in your terminal
* more - read a file in another window, read only (good for large files)
* less - read a file in another window, scroll through bit by bit, read only (good for large files)

## Other Vocab
* upstream: original github page on Will's account
* origin: my copy of Will's github page

## History
* 2023-08-29: first push
* 2023-09-19: week 4 assignment, added details about project data
* 2023-10-03: concatenated my reads together, using a script provided by Leanie Williams
* 2023-10-09: aligned my reads to the reference genome
* 2023-10-17: created a makefile and a salmonindex (NOTE: I made my index wrong, see entries on 2023-11-07 and 2023-12-06)
* 2023-10-31: fiddled with GOATOOLS
* 2023-11-07: fixed my salmon index (I used the wrong reference before)
* 2023-12-06: re-did my salmon index again because it was still wrong, then quantified my RNA seq data

## Concatenating my Reads
* Before I can do my alignment, I need to combine the lanes of my samples together (lanes 4, 5, and 6):
	* RdKW20bio24hr 4 files
	* RdKW20bio24hr 5 files
	* RdKW20bio24hr 6 files
	* RdKW20plklog 4 files
	* RdKW20plklog 5 files
	* RdKW20plklog 6 files
	* GC594bio24hr 4 files
	* GC594bio24hr 5 files
	* GC594bio24hr 6 files
	* GC594plklog 4 files
	* GC594plklog 5 files
	* GC594plklog 6 files
* Leanie Williams provided me with the following script: [concat_files.sh]
* To create the script: `touch concat_files.sh`
* To make it executable: `chmod +x concat_files.sh`
* Breaking down the script and what it does:
	* `fqsDir="$1"` defines the directory that is storing the reads I want to concatenate
	* `for fq in $(ls $fqsDir/*.fastq.gz | cut -d '_' -f 1,2 | sort -u)` cuts out parts of the file name for clarity purposes
	* `do prefix=$ (basename $fg .fastg.gz | cut -d '_' -f 1,2)` calls this shortened file name the "prefix"
	* `cat "Sfg *.fastq.qz >> "Sprefix.concat. fastq.gz"` concatenates the files together and creates a new file using the prefix name
	* `echo $prefix` displays the prefix name on the command line (helpful to know that the file was created)
	* `done` signifies end of script
* Before running the script, I copied all of the files I needed to concatenate into a separate directory that the script could access (it wouldn't work on just the files in the RDSLR directory – the script needed to be given a directory containing the files)
	* Rdbio4: `mkdir Rdbio4` then `cp RdKW20bio24hr4*fastq.gz Rdbio4` to copy all files starting with "RdKWbio24hr4" to the new directory
	* Rdbio5: `mkdir Rdbio5` then `cp RdKW20bio24hr5*fastq.gz Rdbio5` to copy all files starting with "RdKWbio24hr5" to the new directory
	* Rdbio6: `mkdir Rdbio6` then `cp RdKW20bio24hr4*fastq.gz Rdbio6` to copy all files starting with "RdKWbio24hr6" to the new directory
	* Rdlog4: `mkdir Rdlog4` then `cp RdKW20plklog4*fastq.gz Rdlog4` to copy all files starting with "RdKWplklog4" to the new directory
	* Rdlog5: `mkdir Rdlog5` then `cp RdKW20plklog5*fastq.gz Rdlog5` to copy all files starting with "RdKWplklog5" to the new directory
	* Rdlog6: `mkdir Rdlog6` then `cp RdKW20plklog6*fastq.gz Rdlog6` to copy all files starting with "RdKWplklog6" to the new directory
	* GC594biolog: `mkdir GC594biolog` then `cp GC594*fastq.gz GC594biolog` to copy all
		* since the only GC594 files I was given were samples 4, 5, and 6, I could combine everything all at once!
* To run the script:
	* `source scripts/concat_files Rdbio4`
	* `source scripts/concat_files Rdbio5`
	* `source scripts/concat_files Rdbio6`
	* `source scripts/concat_files Rdlog4`
	* `source scripts/concat_files Rdlog5`
	* `source scripts/concat_files Rdlog6`
	* `source scripts/concat_files GC594biolog`
* Finally, to get more organized, I created a directory called "concat_files" and moved all of the concatenated files there
* I also moved the directories "Rdlog4" and so on to the "refs" directory that already existed

## Alignments
* Align reads:
	* Using script provided by Leanie - align Rd and then GC594 reads
	* Saved as `align_Rd_files` ```
	ref="$1"
	fqs="$2"
	for fq in $fqs/Rd*.fastq.gz
	do
	echo $fq
	prefix=$(basename $fq .fastq.gz)
	sam="@RG\tID:$prefix\tSM:$prefix"
	bwa mem -M -t 4 -R $sam $ref $fq | samtools view -hb - | samtools sort -m 3G - > ~/share/courses/OMICS/RDSLR/aligned_files/$prefix.bam
	done 
	```
	* Repeat but change line 3 to `for fq in $fqs/GC594*.fastq.gz`
	* Saved as `align_GC594_files`
* Find size of reference genome: `seqkit stats RdKW20.fasta`
* Generate coverage estimates (in wk05 directory): `python cov_estimate.py --genome 1.8m --bases #g` 
	* # = 1.2g: mean coverage of 666.67
	* # = 7.5g: mean coverage of 4166.67
	* # = 15g: mean coverage of 8333.33
	* # = 120g: mean coverage of 66666.67
* Measuring coverage and making histograms: 
```
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ samtools coverage --histogram aligned_files/RdKW20bio24hr4_S187.concat.bam 
samtools: /opt/tljh/user/bin/../lib/libtinfow.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
Hflu_RdKW20_ctg1 (1.83Mbp)
>  90.00% │▅▆█▆██▆▆▇█▇▇▄▇▇▇▆▇▅▃▇▇▆█▁▆▆▆▇▇▇▇▆▅▇█▇█▆█▆▇█▇▅▅▇█▇█▇▇▆▄▆▅▇█▇▆▄▆█▇▆▇▇▅█▆▄▇▇▃ ▅▅ ▃▅▇█▆█▇▆▅▅▆▇▇█▆▇█▅▂▇▆▇▇▇▇│ Number of reads: 4241644
>  80.00% │█████████████████████████████████████████████████████████████████████████████▇█████████████████████████│     (1715 filtered)
>  70.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Covered bases:   1.79Mbp
>  60.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 97.74%
>  50.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   176x
>  40.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      33.7
>  30.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       56.3
>  20.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 17.8Kbp
>   0.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   100%
          1       177.7K    355.4K    533.0K    710.7K    888.4K    1.07M     1.24M     1.42M     1.60M        1.83M  
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ samtools coverage --histogram aligned_files/RdKW20bio24hr5_S188.concat.bam 
samtools: /opt/tljh/user/bin/../lib/libtinfow.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
Hflu_RdKW20_ctg1 (1.83Mbp)
>  90.00% │▅▇█▇██▇▆███▇▆▆▇▇▆▇▄▃▇▇▆█▁▅▆▆▇█▆▇▇▇█▇██▇█▆▇█▇▆▆▇█▇█▇█▅▄▅▆▇█▇▇▄▅██▇▇▆▄▇▅▄▆▇  ▅▅ ▃▅▇█▆▇▆▆▃▇▆▇▇█▆▆█▅▃█▆▇▆▇▇│ Number of reads: 3703958
>  80.00% │█████████████████████████████████████████████████████████████████████████▇▇██▆█████████████████████████│     (1290 filtered)
>  70.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Covered bases:   1.79Mbp
>  60.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 97.73%
>  50.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   153x
>  40.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      33.7
>  30.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       55.7
>  20.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 17.8Kbp
>   0.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   100%
          1       177.7K    355.4K    533.0K    710.7K    888.4K    1.07M     1.24M     1.42M     1.60M        1.83M  
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ samtools coverage --histogram aligned_files/RdKW20bio24hr6_S189.concat.bam 
samtools: /opt/tljh/user/bin/../lib/libtinfow.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
Hflu_RdKW20_ctg1 (1.83Mbp)
>  89.98% │▂▆▆▃▇▇▅▄▆▆▆▆▁▅▅▅▆▇▂▂▅▄▆▆ ▅▅▆▇▇▄▆▆▂▇▇▆▇▃█▂▇▇▆▅▂▅▇▆█▅▅▄▁▄▄▅▇▆▆▂▃▇▇▆▆▅ ▆▃▂▅▃  ▃▃ ▁▄▃▇▃▇▅▃▁▅▅▆▆█▅▆█▄ ▇▅▅▅▇▃│ Number of reads: 1822420
>  79.98% │█████████████████████████████████████████████████████████████████████████▂ ██ ██████████████████▄██████│     (653 filtered)
>  69.98% │██████████████████████████████████████████████████████████████████████████▄████████████████████████████│ Covered bases:   1.75Mbp
>  59.99% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 95.47%
>  49.99% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   75.4x
>  39.99% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      33.8
>  29.99% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       49.3
>  20.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 17.8Kbp
>   0.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   99.977%
          1       177.7K    355.4K    533.0K    710.7K    888.4K    1.07M     1.24M     1.42M     1.60M        1.83M  
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ samtools coverage --histogram aligned_files/RdKW20plklog4_S181.concat.bam 
samtools: /opt/tljh/user/bin/../lib/libtinfow.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
Hflu_RdKW20_ctg1 (1.83Mbp)
>  90.00% │▆▇▇▇██▆▇▇▇██▆▇▇▇▇▇▆▄█▇▇█▄█▆▆▇█▆█▇▆██▇█▇█▇█▇▇▇▆████▇▇▆▄▅▆▆█▇▆▅▆██▆▇▆▆█▅▅▆██▇▅▆ ▂▆▇█▆█▇▅▅▆▆▇▇▇▆▆█▅▄▇▆▇▆█▆│ Number of reads: 7908345
>  80.00% │█████████████████████████████████████████████████████████████████████████████▆█████████████████████████│     (3452 filtered)
>  70.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Covered bases:   1.80Mbp
>  60.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 98.18%
>  50.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   328x
>  40.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      33.7
>  30.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       57.9
>  20.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 17.8Kbp
>   0.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   100%
          1       177.7K    355.4K    533.0K    710.7K    888.4K    1.07M     1.24M     1.42M     1.60M        1.83M  
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ samtools coverage --histogram aligned_files/RdKW20plklog5_S182.concat.bam 
samtools: /opt/tljh/user/bin/../lib/libtinfow.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
Hflu_RdKW20_ctg1 (1.83Mbp)
>  90.00% │▅▇▇▇▇▇▅▆▇▇█▇▅▇▇█▇▇▅▄██▇█▄▇▇▇█▇▇▇▇▇▇▇▇█▇█▆█▇██▆▇█▇█▇▇▆▃▅▅▆█▇▇▅▆█▇▆▇▆▃▇▆▅▇██▇▃▅ ▂▅▆▇▆█▆▆▃▇▆▇▆▇▆▇█▄▅▇▅▇▅█▇│ Number of reads: 7332768
>  80.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│     (3105 filtered)
>  70.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Covered bases:   1.79Mbp
>  60.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 97.99%
>  50.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   304x
>  40.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      33.7
>  30.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       57.8
>  20.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 17.8Kbp
>   0.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   100%
          1       177.7K    355.4K    533.0K    710.7K    888.4K    1.07M     1.24M     1.42M     1.60M        1.83M  
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ samtools coverage --histogram aligned_files/RdKW20plklog6_S183.concat.bam 
samtools: /opt/tljh/user/bin/../lib/libtinfow.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
Hflu_RdKW20_ctg1 (1.83Mbp)
>  90.00% │▇▇▇▅▇█▅▇▇█▇█▅▇▇▇▆▇▆▄█▇▅█▄█▇▇▇█▆▇▆▆▇▇▇█▆▇▇██▇▇▇▇███▇▆▅▁▅▅▆█▇▆▄▅█▇▆▇▆▃▇▅▅▇▇█▆▃▅ ▂▆▆█▆█▆▅▃▆▇▆▇▇▅▆█▅▅▆▅▇▅█▇│ Number of reads: 5860791
>  80.00% │█████████████████████████████████████████████████████████████████████████████▂█████████████████████████│     (2760 filtered)
>  70.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Covered bases:   1.79Mbp
>  60.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 97.79%
>  50.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   243x
>  40.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      33.7
>  30.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       58.1
>  20.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 17.8Kbp
>   0.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   100%
          1       177.7K    355.4K    533.0K    710.7K    888.4K    1.07M     1.24M     1.42M     1.60M        1.83M  
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ samtools coverage --histogram aligned_files/GC594bio24hr4_S190.concat.bam 
samtools: /opt/tljh/user/bin/../lib/libtinfow.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
Hflu_RdKW20_ctg1 (1.83Mbp)
>  90.00% │▆▇█▇▇█▆▆▇▇▇▇▄▇▇▇▆▇▅▄█▇▆█▂▆▇▇▇▇▆▆▇▆▇█▇█▆█▇▇█▇▆▅▆███▇▇▅▆▄▆███▇▃▆▇▇▆▇▇▅▇▅▅▆▇  ▅▅ ▅▅▆█▇█▆▇▃▆▆█▇█▇▇█▅▄▇▆▇▇█▇│ Number of reads: 2579944
>  80.00% │█████████████████████████████████████████████████████████████████████████▇▃██▆█████████████████████████│     (1203 filtered)
>  70.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Covered bases:   1.79Mbp
>  60.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 97.73%
>  50.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   107x
>  40.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      33.7
>  30.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       56.2
>  20.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 17.8Kbp
>   0.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   100%
          1       177.7K    355.4K    533.0K    710.7K    888.4K    1.07M     1.24M     1.42M     1.60M        1.83M  
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ samtools coverage --histogram aligned_files/GC594bio24hr5_S191.concat.bam 
samtools: /opt/tljh/user/bin/../lib/libtinfow.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
Hflu_RdKW20_ctg1 (1.83Mbp)
>  90.00% │▄▇▆▇▇█▅▆▆██▇▄▆▆▆▇▇▃▃▇▇▆▇▁▅▅▆▇▇▄▇▇▄▇█▇█▅█▅▆▇▇▆▄▆█▇▇▆▆▃▃▅▆▇█▆▆▃▅▆▇▆▆▆▄▆▅▄▆▆  ▂▃ ▄▄▆█▅▇▆▆▂▆▄▇▆▇▅▅█▄ ▇▅▅▇▇▆│ Number of reads: 2518451
>  80.00% │██████████████████████████████████████████████████████████████████████████▁██▄██████████████████▆██████│     (938 filtered)
>  70.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Covered bases:   1.77Mbp
>  60.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 96.8%
>  50.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   104x
>  40.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      33.7
>  30.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       53
>  20.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 17.8Kbp
>   0.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   100%
          1       177.7K    355.4K    533.0K    710.7K    888.4K    1.07M     1.24M     1.42M     1.60M        1.83M  
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ samtools coverage --histogram aligned_files/GC594bio24hr6_S192.concat.bam 
samtools: /opt/tljh/user/bin/../lib/libtinfow.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
Hflu_RdKW20_ctg1 (1.83Mbp)
>  89.99% │ ▆▅▆▆▇▅▃▆▆▇▆▁▆▆▅▆▇▂ ▆▅▅▅▁▄▆▆▆▆▃▆▆▃▆▆▆▇▆▇▂▅▇▆▄▂▄▇▆█▆▅▁▁▄▃▄█▆▅▂▃▆▅▆▆▅▁▇▂▁▆▄   ▃ ▃▃▅█▃▇▄▆ ▃▄▇▄▇▄▅█▃ ▅▅▄▅▆▄│ Number of reads: 1784464
>  79.99% │█████████████████████████████████████████████████████████████████████████  ██ ██████████████████▂██████│     (537 filtered)
>  69.99% │█████████████████████████████████████████████████████████████████████████▅▃████████████████████████████│ Covered bases:   1.74Mbp
>  59.99% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 95.21%
>  49.99% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   73.9x
>  40.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      33.7
>  30.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       49.3
>  20.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 17.8Kbp
>   0.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   99.989%
          1       177.7K    355.4K    533.0K    710.7K    888.4K    1.07M     1.24M     1.42M     1.60M        1.83M  
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ samtools coverage --histogram aligned_files/GC594plklog4_S184.concat.bam 
samtools: /opt/tljh/user/bin/../lib/libtinfow.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
Hflu_RdKW20_ctg1 (1.83Mbp)
>  90.00% │▅▇▆▅▇▇▆▇▇▇█▇▆▇▇█▇▇▆▃█▇██▅▇▇▇▇█▅▇▇▇██▇█▆█▅██▇▇▆▇█▇█▇▆▅▂▆▆▇██▇▅▆▇█▆▇▇▃█▆▅▇█▇▅▅▆ ▃▄▇▇▅█▇▆▄▇▆▇▇█▆▇█▅▄▇▅▇▆█▇│ Number of reads: 6430080
>  80.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│     (2427 filtered)
>  70.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Covered bases:   1.80Mbp
>  60.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 98.08%
>  50.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   267x
>  40.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      33.7
>  30.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       57.5
>  20.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 17.8Kbp
>   0.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   100%
          1       177.7K    355.4K    533.0K    710.7K    888.4K    1.07M     1.24M     1.42M     1.60M        1.83M  
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ samtools coverage --histogram aligned_files/GC594plklog5_S185.concat.bam 
samtools: /opt/tljh/user/bin/../lib/libtinfow.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
Hflu_RdKW20_ctg1 (1.83Mbp)
>  90.00% │▄▆▇▅▇▇▆▇▇▇██▄▆▇█▆▇▆▃█▇▇▇▂█▇▇▇█▆▇▆▆▇▇▇█▇█▅██▇▆▆▇█▆▇▆▆▆▂▅▅▇█▇▇▄▆██▆▆▇▃▇▆▅▆▇▇▄▁▅ ▂▄▆█▅▇▇▅▅▇▅▆▆▇▆▆█▅▂▇▆▇▆▇▆│ Number of reads: 5497436
>  80.00% │█████████████████████████████████████████████████████████████████████████████▅█████████████████████████│     (1778 filtered)
>  70.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Covered bases:   1.79Mbp
>  60.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 97.55%
>  50.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   228x
>  40.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      33.8
>  30.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       56.7
>  20.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 17.8Kbp
>   0.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   100%
          1       177.7K    355.4K    533.0K    710.7K    888.4K    1.07M     1.24M     1.42M     1.60M        1.83M  
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ samtools coverage --histogram aligned_files/GC594plklog6_S186.concat.bam 
samtools: /opt/tljh/user/bin/../lib/libtinfow.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
samtools: /opt/tljh/user/bin/../lib/libncursesw.so.6: no version information available (required by samtools)
Hflu_RdKW20_ctg1 (1.83Mbp)
>  90.00% │▆▇▇▆▇▇▅▆▆▇█▇▅▆▇▇▆▇▅▃▇▆▇█▃▇▆▇▇█▆▇▇▆▇███▇█▅▇▇▆▇▇▇█▇█▆▇▇▃▅▅▆█▇▆▅▅█▇▇▇▆▂▇▅▄▆▇▇▅▁▅ ▂▅▄█▆█▆▅▄▇▅▇▆▇▅▇█▅ ▇▆▇▅█▅│ Number of reads: 5011880
>  80.00% │█████████████████████████████████████████████████████████████████████████████▄█████████████████████████│     (1651 filtered)
>  70.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Covered bases:   1.78Mbp
>  60.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Percent covered: 97.52%
>  50.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean coverage:   208x
>  40.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean baseQ:      33.8
>  30.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Mean mapQ:       56.3
>  20.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ 
>  10.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo bin width: 17.8Kbp
>   0.00% │███████████████████████████████████████████████████████████████████████████████████████████████████████│ Histo max bin:   100%
          1       177.7K    355.4K    533.0K    710.7K    888.4K    1.07M     1.24M     1.42M     1.60M        1.83M 
```

## Variant Calling
* [methods.md]
* `bcftools mpileup -f refs/RdKW20.fasta aligned_files/RdKW20bio24hr5_S188.concat.bam | bcftools call -mv -Ob -o Rdbio5_calls.bcf`
* `bcftools view Rdbio4_calls.bcf | less -S`
* `bcftools stats Rdbio4_calls.bcf | less -S`
* Repeat for all 12 samples
* Also, made a .bcf file that combined all of the .bam files: `bcftools mpileup -f refs/RdKW20.fasta aligned_files/*.concat.bam | bcftools call -mv -Ob -o combined_calls.bcf`

## Salmon
* Create a salmon index:
```
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ seqkit seq --name ~/share/courses/OMICS/RDSLR/refs/RdKW20.fasta | cut -f1 -d ' ' > decoys.txt
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ cat refs/RdKW20.fasta
RdKW20.fasta      RdKW20.fasta.amb  RdKW20.fasta.ann  RdKW20.fasta.bwt  RdKW20.fasta.fai  RdKW20.fasta.pac  RdKW20.fasta.sa
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ cat refs/RdKW20.fasta
RdKW20.fasta      RdKW20.fasta.amb  RdKW20.fasta.ann  RdKW20.fasta.bwt  RdKW20.fasta.fai  RdKW20.fasta.pac  RdKW20.fasta.sa
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ cat refs/RdKW20.annot.gff refs/RdKW20.fasta > transcripts_decoys.fa
jupyter-marycmarino@Mistake-Not:~/share/courses/OMICS/RDSLR$ salmon index -t transcripts_decoys.fa -i salmonindex --decoys decoys.txt -k 31
```
* Create a project makefile:
```
jupyter-marycmarino@Mistake-Not:~/repos/OMICS/projects/marycmarino$ touch makefile
jupyter-marycmarino@Mistake-Not:~/repos/OMICS/projects/marycmarino$ nano makefile
```
* [makefile]: my makefile for my project

* Re-making my salmon index because the one above didn't work:
```
seqkit seq --name refs/RdKW20.fasta | cut -f1 -d ' ' > decoys4.txt
cat refs/RdKW20.annot.cds.fasta refs/RdKW20.fasta > transcripts_decoys4.fasta
salmon index -t transcripts_decoys4.fasta -i RdKW20_salmon_index --decoys decoys4.txt -k 31
```
	* NOTE: This took four tries, hence "decoys4.txt" and 
	* My final salmon index is called: `RdKW20_salmon_index`
* Quantifying my data using salmon quant
`salmon quant -l A -i RdKW20_salmon_index -r concat_files/GC594bio24hr4_S190.concat.fastq.gz -o final_salmon_quant`
	* Repeated for all 12 samples' concatenated fastq.gz files
	* Results can be found in `final_salmon_quant` in the RDSLR repo
