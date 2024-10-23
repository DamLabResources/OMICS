# This is my wk06 README
See the makefile for all commands used.

## Number of reads aligned at Q30 threshold:

File name   | Count
------------|-------
SF_ann.sam  | 184775
SF_aer.sam  | 184623
OGstrain.sam| 182351

## Calculated average depth across each chromosome for each sample:

Couldn't figure out how to add this command to the makefile as there was a syntax issue with the dollar signs, so I ran these commands separately in the terminal:
```bash
awk '{sum[$1] += $3; count[$1]++} END {for (chr in sum) {print chr, sum[chr] / count[chr]}}' SF_ann.depth.txt
awk '{sum[$1] += $3; count[$1]++} END {for (chr in sum) {print chr, sum[chr] / count[chr]}}' SF_aer.depth.txt
awk '{sum[$1] += $3; count[$1]++} END {for (chr in sum) {print chr, sum[chr] / count[chr]}}' OGstrain.depth.txt
```
##

SF_ann	|Depth	
--------|--------
chrIV	| 2.81443
chrX	| 2.93424
chrV	| 3.02555
chrI	| 2.94401
chrII	| 2.8689
chrXVI	| 2.80986
chrIX	| 3.39995
chrXV	| 2.81866
chrXII	| 3.35866
chrVI	| 3.27201
chrXIII	| 2.77233
chrVIII	| 3.36868
chrXIV	| 3.26016
chrXI	| 2.82763
chrIII	| 2.88209
chrVII	| 2.76509
chrmt	| 28.4954

SF_aer	| Depth
--------|--------
chrIV	| 2.59456
chrX	| 2.81824
chrV	| 3.03432
chrI	| 3.73935
chrII	| 2.80909
chrXVI	| 2.7824
chrIX	| 3.46135
chrXV	| 2.75818
chrXII	| 3.1065
chrVI	| 3.23044
chrXIII | 2.69495
chrVIII | 2.9023
chrXIV	| 2.80617
chrXI	| 2.81613
chrIII	| 3.14691
chrVII	| 3.24361
chrmt	| 15.3805

OGstrain|Depth
--------|--------
chrIV	| 2.65371
chrX	| 2.89911
chrV	| 2.91386
chrI	| 3.29367
chrII	| 2.81333
chrXVI	| 2.79893
chrIX	| 2.91536
chrXV	| 2.77355
chrXII	| 4.19153
chrVI	| 3.0728
chrXIII	| 2.76883
chrVIII	| 2.95502
chrXIV	| 2.83366
chrXI	| 2.80516
chrIII	| 3.1174
chrVII	| 2.74297
chrmt	| 10.0792

## See attached image from IGV:
