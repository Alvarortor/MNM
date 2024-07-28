#Remake Zelda first

#imports
import re
import os
import sys

#Error holders
myIsoList = "none"
myMod = "none"

#Error file holder for app
myEF = "LinkError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Potential errors
noIn = "Error: Did not define input file."
noExist = "Error: File does not exist."
getHelp = "Use the -h option for help"
myOption = "none"
use = "Link.py <Isolate_file.txt> <file_modifier>"


#Inputs
try:
    myIsoList = sys.argv[1]
    myMod = sys.argv[2]
except IndexError:
    if myIsoList == "none":
        print (noIn)
        errFile.write(noIn)
        sys.exit()


try:
    inpath = os.path.abspath(myIsoList)
    file = open(inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    errFile.write(noExist)
    errFile.close()
    sys.exit()
    
    
outpath = os.path.abspath("IsoConcat.fasta")
OF = open(outpath,"w")

#lists
IsoID = list()

#Pass isolates to list
for line in file:
    IsoID.append(line.strip())
    
for entry in IsoID: #Check for modifiers on files
    if myMod == "none":
        isoFile = entry + "_concat.txt"
    elif myMod != "none":
        isoFile = entry + myMod + "_concat.txt"
    #open inputs and outputs for each
    isoIn = os.path.abspath(isoFile)
    isoFile = open(isoIn)

    #Combine all lines
    for line in isoFile:
        if ">" in line:
            OF.write(line)
        else:
            OF.write(line + "\n")
        
        
print("Done!")  
   