
#Cleans MUM output since it likes to play willy nilly with spaces in output file
#Usage MUMCleaner.py <file.mums>



#Imports
import os #So it can search through device
import re #Regexes
import sys #Accept input from command line but without needing to type


#Blank statements sthat get overwritten later
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


#Blank statements sthat get overwritten later
myFile = "none"

#input arguments
try:
    myFile = sys.argv[1]
    myRename = sys.argv[2]
except IndexError:
    myRename = "none"
    if myFile == "-h":  
        print("Purpose: Cleans MUM output since it likes to play willy nilly with spaces in output file \nUsage MUMCleaner.py <file.mums>")
        sys.exit()    
    elif myFile == "none":
        print ("Error: Did not define input file. Use the -h option for help")
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
    


#Create outputs
if myRename == "none":
    myOF =" CleanMums.mums"
else:
    myOF = myRename + "_CleanMum.mums"
    
outpath = os.path.abspath(myOF)
outFile = open(outpath, "w");
#Just remove white spaces around numbers?

#open input file
for line in file:
    if ">" in line:
        clean = line
    else:
        clean = line.strip()
    outFile.write(clean + "\n")
    
print ("Done!")