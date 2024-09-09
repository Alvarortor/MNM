#Remake flipper

#Imports
import os #So it can search through device
import re #Regexes
import sys #Accept input from command line but without needing to type
import datetime

#Blank statements sthat get overwritten later
myFile = "none"


#Error file holder for app
myEF = "Error.log"
errpath = os.path.abspath(myEF)

#Clear errors
open(errpath, "w+").close()
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


#Potential errors
Error = "Error: "
noIn = "Error: Did not define input file."
noExist = " does not exist."
getHelp = "Use the -h option for help"
use = "Flipper.py <file.txt>"
noData =" is blank."


#input arguments
try:
    myFile = sys.argv[1]
except IndexError:
    if myFile == "-h":  
        print("Purpose: Returns reverse complement of specified sequence")
        sys.exit()    
    elif myFile == "none":
        print (noIn, getHelp)
        
        errFile = open(errpath, "w+");
        errFile.write(now + "\n" + noIn)
        errFile.close
        sys.exit()
    elif myFile == "":
        print (noIn, getHelp)
        
        errFile = open(errpath, "w+");
        errFile.write(now + "\n" + noIn)
        errFile.close
        sys.exit()

#Get path to the file
try:
    inpath = os.path.abspath(myFile)
    file = open(inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    
    errFile = open(errpath, "w+");
    errFile.write(now + "\n" + Error + myFile + noExist)
    errFile.close()
    sys.exit()



#Mini check to look for blank files
if (file.readline() == ""):
    print (noData, getHelp, use)
    
    errFile = open(errpath, "w+");
    errFile.write(now + "\n" +Error + myFile + noData)
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
        line = line[::-1].translate(line.maketrans("ATCGatcg", "TAGCtagc")) #Translates and then flips
    outFile.write(line)

print ("!enoD")
