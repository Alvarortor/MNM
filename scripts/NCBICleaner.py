#Remake cleaner but in puthon


import os
import sys
import re



#Usage:  NCBICleaner.py <file.txt>

#Holder statements
myFile = "none"
myRename = "none"



#Error file holder for app
myEF = "NCBICLeanError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Potential errors
noIn = "Error: Did not define input file."
noExist = "Error: File does not exist."
getHelp = "Use the -h option for help"
use = "NCBICleaner.py <file.txt> <output_name>"

#input arguments
try:
    myFile = sys.argv[1]
    myRename = sys.argv[2]
except IndexError:
    if myFile == "-h":  
        print("Purpose:Cleans up FastA sequences received from NCBI tool", use)
        sys.exit()    
    elif myFile == "none":
        print (noIn, getHelp)
        errFile.write(noIn)
        errFile.close()
        sys.exit()
        
#Get path to the file
try:
    inpath = os.path.abspath(myFile)
    file = open(inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    errFile.write(noExist)
    errFile.close()
    sys.exit()
    

#Create outputs based on user specification
if myRename == "none":
    myOF ="NCBI_Clean.fasta" #Reverse complement
else:
    myOF = myRename + "_NCBI_Clean.fasta" 
outpath = os.path.abspath(myOF)
outFile = open(outpath, "w");

count = 0
for line in file:
    if ">" in line:
        line = line.split(" ")
        if count != 1:
            data = ">" + line[1] + "\n"
            count += 1
        else:
            data = "\n" + ">" + line[1] + "\n"
    else:
        data = line.rstrip()
    outFile.write(data)