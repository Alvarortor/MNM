#Remake Zelda first

#imports
import re
import os
import sys

#Error holders
myIsoList = "none"
myMod = "none"



#Error file holder for app
myEF = "ZeldError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Potential errors
noIn = "Error: Did not define input file."
noExist = "Error: File does not exist."
getHelp = "Use the -h option for help"
myOption = "none"
use = "Zelda.py <Isolate_file.txt> <file_modifier>"

#Inputs
try:
    myIsoList = sys.argv[1]
    myMod = sys.argv[2]
except IndexError:
    if myIsoList == "none":
        print (noIn + getHelp)
        errFile.write(noIn)
        errFile.close()
        sys.exit()


#Get path to the file


#lists
IsoID = list()

#Pass isolates to list
for line in file:
    IsoID.append(line.strip())
    
for entry in IsoID: #Check for modifiers on files
    if myMod == "none":
        isoFile = entry + "_pulled.txt"
        print(isoFile)
        isoOut =  entry + "_concat.txt"
    elif myMod != "none":
        isoFile = entry + myMod + "_pulled.txt"
        isoOut = entry + myMod + "_concat.txt"
    #open inputs and outputs for each
    isoIn = os.path.abspath(isoFile)
    isoFile = open(isoIn)
    outpath = os.path.abspath(isoOut)
    OF = open(outpath,"w")
    
    #Nice little header
    OF.write(">" + entry + "\n")
    
    #Combine all lines
    for line in isoFile:
        if ">" not in line:
            OF.write(line.strip())
        
        
print("Done!")  
   