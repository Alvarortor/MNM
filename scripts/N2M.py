#Make N2M but in python

#Purpose: Parse output from NCBIs search feature so sequence numbers can be called from console
#Usage:  N2M <file.txt>

#Holder statements
myFile = "none"
myRename = "none"



#Error file holder for app
myEF = "CleanError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Potential errors
noIn = "Error: Did not define input file."
noExist = "Error: File does not exist."
getHelp = "Use the -h option for help"
use = "MUMCleaner.py <file.mums>"

#Imports
import os #So it can search through device
import re #Regexes
import sys #Accept input from command line but without needing to type



#input arguments
try:
    myFile = sys.argv[1]
except IndexError:
    if myFile == "-h":  
        print("Purpose:Parse output from NCBIs search feature so sequence numbers can be called from console.\nUsage: N2M <file.txt>")
        sys.exit()    
    elif myFile == "none":
        print (noIn, getHelp)
        errFile.write(noIn)
        errFile.close()
        sys.exit()
#Get path to the file
inpath = os.path.abspath(myFile)

#Create outputs
myOF =" Nums.txt" #Reverse complement
outpath = os.path.abspath(myOF)
outFile = open(outpath, "w");

#open input file
file = open(inpath);

for line in file:
    if "ID:" in line: #Hunts for lines with ID tag in them
        line = (line[4:])
        outFile.write(line.strip() + "\n") #Removes trailing newline
print("Done!")

