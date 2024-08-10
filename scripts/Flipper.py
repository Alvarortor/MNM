#Remake flipper

#Imports
import os #So it can search through device
import re #Regexes
import sys #Accept input from command line but without needing to type

#Blank statements sthat get overwritten later
myFile = "none"


#Error file holder for app
myEF = "FlipError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Potential errors
noIn = "Error: Did not define input file."
noExist = "Error: File does not exist."
getHelp = "Use the -h option for help"
use = "Flipper.py <file.txt>"


#input arguments
try:
    myFile = sys.argv[1]
except IndexError:
    if myFile == "-h":  
        print("Purpose: Returns reverse complement of specified sequence")
        sys.exit()    
    elif myFile == "none":
        print (noIn, getHelp)
        errFile.write(noIn)
        errFile.close
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
myOF ="RevCom.txt" #Reverse complement
outpath = os.path.abspath(myOF)
outFile = open(outpath, "w");

#open input file
for line in file:
    if ">" in line: #leave lines with headers alone
        line = line
    else:
        #line = line.upper()
        line = line[::-1].translate(line.maketrans("ATCGatcg", "TAGCtagc")) #Translates and then flips
    outFile.write(line)

print ("!enoD")
