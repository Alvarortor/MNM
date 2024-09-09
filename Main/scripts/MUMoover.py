#MUMoover

#Checks for a specified gene in extracted file and will remove any of that gene that are not the required size
#Cannot be done while its being read

#Imports
import os
import re
import sys



myGene = "none" #Add a gene name here
myFile = "none" #Pick the path to your file that needs to be removed
myIso = "none" #Also specify your isolate here for added safety when checking
mySize = "none" #Actual gene size you want, anything smaller than this will be deleted

#Errors
noGene = "Error: No gene specified"
noIso = "Error: No isolate specified"
noFile = "Error: No file selected"
noSize = "Error: No minimum size selected"
getHelp = "Use the -h option for help"
use = "MUMMoover <Gene> <File.txt> <Isolate> <Size>"
noExist = "Error: File does not exist."
wrongIso = "Error: Isolate not in file, check input."

#Preemptively create error file
#Error file holder for app
myEF = "MMError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");


try:
	myGene = sys.argv[1] #Add a gene name here
	myFile = sys.argv[2] #Pick the path to your file that needs to be removed
	myIso = sys.argv[3] #Also specify your isolate here for added safety when checking
	mySize = sys.argv[4] #Actual gene size you want, anything smaller than this will be deleted
except IndexError:
    if myGene == "none":
        print(noGene, use, getHelp)
        errFile.write(noGene)
        errFile.close()
        sys.exit()
    elif myIso == "none":
        print(noIso, use, getHelp)
        errFile.write(noIso)
        errFile.close()
        sys.exit()
    elif myFile == "none":
        print(noFile, use, getHelp)
        errFile.write(noFile)
        errFile.close()
        sys.exit()   
    elif mySize == "none":
        print(noSize, use, getHelp)
        errFile.write(noSize)
        errFile.close()
        sys.exit()   

#Find path to file
try:
    inpath = os.path.abspath(myFile)
    file = open(inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    errFile.write(noExist)
    errFile.close()
    sys.exit() 

outname = myIso + "_trimmed.txt"
outpath = os.path.abspath(outname)
OF = open(outpath, "w")    
with open(inpath, 'r') as file:
    for line in file:
        if myIso in line:
            if myGene in line:
                next_line = file.readline()
                line_len = (len(next_line))
                if line_len >= int(mySize):
                    OF.write(line)
                    OF.write(next_line)
            elif myGene not in line:
                next_line = file.readline()
                OF.write(line)
                OF.write(next_line)
        elif myIso not in line and ">" in line:
            print(wrongIso, getHelp, use)
            errFile.write(wrongIso)
            sys.exit()
        

file.close()