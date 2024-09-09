#Remake Zelda first

#imports
import re
import os
import sys
import datetime

#Error holders
myIsoList = "none"
myMod = "none"

#Error file holder for app
myEF = "Error.log"
errpath = os.path.abspath(myEF)

#Clear errors
open(errpath, "w+").close()
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#Potential errors
Error ="Error: "
noIn = "Error: Did not define input file."
noExist = " does not exist."
getHelp = "Use the -h option for help"
myOption = "none"
use = "Link.py <Isolate_file.txt> <file_modifier>"
noData = " is empty."


#Inputs
try:
    myIsoList = sys.argv[1]
    myMod = sys.argv[2]
except IndexError:
    if myIsoList == "none":
        print (noIn)
        errFile = open(errpath, "w+");
        errFile.write(now + "\n" + noIn)
        sys.exit()


try:
    inpath = os.path.abspath(myIsoList)
    file = open(inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    errFile = open(errpath, "w+");
    errFile.write(now + "\n" + Error + myIsoList + noExist)
    errFile.close()
    sys.exit()
    
 #Checks to see if file is empty 
if (file.readline() == ""):
    print (noData, getHelp, use)
    errFile = open(errpath, "w+");
    errFile.write(now + "\n" + Error + myIsoList +  noData)
    errFile.close()
    sys.exit()    
#Creates one big fasta output    
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
    elif myMod == "_Example":
        isoFile = "Main\examples\\" + entry + myMod + "_concat.txt"
    elif myMod != "none":
        isoFile = entry + myMod + "_concat.txt"
    #open inputs and outputs for each
    isoIn = os.path.abspath(isoFile)
    isoFile = open(isoIn)
    if (isoFile.readline() == ""):
        print (noData, getHelp, use)
        errFile = open(errpath, "w+");
        errFile.write(now + "\n" + Error + entry +  noData)
        errFile.close()
        sys.exit() 
    #Combine all lines
    for line in isoFile:
        if ">" in line:
            OF.write(line)
        else:
            OF.write(line + "\n")
        
        
print("Done!")  
   