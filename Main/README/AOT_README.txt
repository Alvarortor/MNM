READ ME
---
Here are the general descriptions for each of the programs I developed/modified for use in the lab. We have three categories: String extraction, string manipulation, and data visualization. The first two are available in PERL or Python versions, and the data visualization is written in R. Each program has a help option "-h" if it can be run from the command line. 

Icon Attributions:
Tick and Prohibition icons by Yusuke Kamiyamane. Licensed under a Creative Commons Attribution 3.0 License.
(C) 2013 Yusuke Kamiyamane. All rights reserved.

######
+++String Extraction Tools+++
###  Repository for codes used to extract sequences from single or multiFastA files. All programs listed below contain a help section and usage information. Summary for each program is listed here. 


---

1. Seqstracter: Extracts sequence data from a file by specifying scaffold number, start, and end poisitions. Useful for extracting small sequences rapidly.
---

2. Multiseqstracter: Extracts sequence data by using the file.coords output from MUMmer. Set identity to 90% and Tabular format when extracting data through show-coords. Useful for extracting large amounts of sequences for a **single specified isolate**. 
---

3. MegaMultiSeqstracter: Extracts sequence data in the same way as MultiSeqstracter, but uses an **isolate file** where each isolate is listed on a single line within. Useful for extracting **multiple genes for many different strains**. Caution: Extremely time consuming (~2-3 min to run) try to limit these to under 100 genes per isolate. 
---

4. RandoPuller: Tool designed to pull genes at random from a specified gene file. Each line should only contain a single gene. Useful for situations where a large dataset limits analysis. User can specify a number of genes for the program to search for although it gets unreliable as the input number exceeds half of the genes in the file. 
---

5. GeneStracter: Allows extraction of specific genes from a MultiSeqstracter or greater output by manually specifying the gene. **Useful when the user wants to compare single genes to one another**.
---

6. MultiGeneStracter: Allows extraction of many genes as specified by a gene file. Pairs well with outputs from RandoPuller, **useful  to assist in making phylogenetic trees**. 
--
7. MegaMultiGeneStracters: Same as MultiGenestracter, but works with a specified isolate file

+++String Manipulation Tools+++
###  Repository for codes used to manipulate sequences from single or multiFastA files. All programs listed below contain a help section and usage information. Summary for each program is listed here. 
---
1. Chomp: Used to convert FastA files into text files for compatability with the other programs. 
---

2. Flipper: Used to produce the reverse complement of a specific sequence, useful when verifying extractions of unassembled programs. 
---

3. Zelda: Links together MultiFastA files for isolates specified within an isolate file for phylogenetic tree construction.  Does so by removing headers and trailing newlines. 
---

4. Joiner: Combines several  concatenated FastA files output by Zelda into a single MultiFastA. Useful in the generation of phylogenetic trees in MEGA. 
5. BunkBed: Compiles bedtools output by removing duplicated lines in file, useful when multiple MUMs are located within a single gene. Significantly condenses file size. 
---

6. JAMS: Takes output from MUMmer and converts it into differnent formats. Current outputs are .bed, phenogram, and circos. Able to account for chromosome size provided parental strains are used as reference. 
---

7. N2M (Num2MUM): Parses output from NCBI's BatchEntrez tool to automate gene extraction using the NCBI tools. Outputs a file with an amino acid ID on each line. 
---

8. MUMCleaner: Processes MUMmer output to remove empty columns since it will sometimes randomly add an empty column. 
---

+++Data Visualization+++
###  Respository for codes used to visualize data from 96-well plates. Summary for each program is listed here. See Larbarchives for sample inputs and outputs for the programs

---
1. Barplots.R: This code can be run in R to produce graphs to hep visualize the data. The biofilm file allows for the XTT and CV assays and automates most data analysis. The file also includes post-hoc analysis near the end.
---

2. Heatmap.R: Code to be used to create heatmaps from 96-well plate data. Helps to compare effectiveness of antifungal drugs among different isolates
---

3. GrowthCurve.R: Code to visualize growth curve, data must be sorted into columns to make analysis possible. 
---

4. CutoffPlot.R: Code to visualize results from 96-well plates on drug libraries. Assigns ID to each well and plots absorbance. Also allows user to specify cutoff and identify compounds above cutoff. 



