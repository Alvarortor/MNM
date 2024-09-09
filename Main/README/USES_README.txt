README

Hello Reader!
This is a collection of programs I made during my thesis to assist the data extraction and processing from MUMmer. To help you out I decided to make a small list of ways that this can be used. While I'm providing some workflows, there are more ways to use these tools that I haven't explored so feel free to have fun. 

Uses:
1. Locating genes with associated functions:
	Search for phenotype on CGD.org and download entries>
		pass the gene IDs (ex: CAGLO121g) to BatchEntrez and get numerican gene IDs
			Run N2M on these to only get numbers
				Run "datasets download gene gene-id --inputfile Nums.txt --include gene" IN CONSOLE
					Run Cleaner on downloaded gene.fna
	Done! You now have a bunch of FastA sequences that can be passed to MUMmer
2. Calculate MUMi
	Run MUMmer -b -c -l 21 on reference and query
		input reference file, query file, and resulting .mums file into MUMi
	Done!

3. Convert MUMmer format into others
	Run MUMmer
		Run MUMCleaner on .mums file to avoid errors
			Enter info into respective slots on JAMS
	Done!
4. Extract genes from MUMmer to compare in MEGA(Connects with 1)
	Run Nucmer and show-coords in MUMmer
		Use any seqstracter format to pull the specified number of regions and genes
			Use randopuller and genestracter if you need a specific number of genes
				Use Zelda and Link programs to combine relevant genes
					Pass to MEGA for SNPS or other analysis
	Done!
5. Collect genes and analyze for SNPs (Proceeds from 1)
	Run NUCmer and show-coords in MUMmer to collect genes
		Use NameGet and MegaGeneStracter for your desired genes
			Run PROmer and show-snps on data
				Finish with SNProcesser on the resulting.snps files. 
	
			