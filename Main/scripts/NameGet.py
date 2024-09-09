#Get the first name for each of the genes to make it easier to process

import sys
import os
import re


myFile = sys.argv[1]


#Get paths

#Find the file
path = os.path.abspath(myFile)
file = open(path, 'r')


#Extract first sequence and create file with that name
count = 0
for line in file:
    if count == 0:
        if ">" in line:
            next_line = file.readline()
            next_line = next_line.rstrip()
            Iso = line.index("_")
            geneend = line.index("g")
            genetag = line[1:][:geneend]
            outpath = os.path.abspath(genetag + ".txt")
            OF = open(outpath, 'w')
            OF.write(line)
            OF.write(next_line)
            
            count += 1

print("Done!)