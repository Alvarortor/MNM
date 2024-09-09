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
Error = "Error: "
noIn = "Error: Did not define input file."
noExist = " does not exist."
getHelp = "Use the -h option for help"
myOption = "none"
use = "Zelda.py <Isolate_file.txt> <file_modifier>"
noData = " is empty."

#Inputs
try:
    myIsoList = sys.argv[1]
    myMod = sys.argv[2]
except IndexError:
    if myIsoList == "none":
        print (noIn + getHelp)
        errFile = open(errpath, "w+");
        errFile.write(now + "\n" + noIn)
        errFile.close()
        sys.exit()



#lists
IsoID = list()

#Open file
try:
    filePath = os.path.abspath(myIsoList)
    file = open(filePath)
except FileNotFoundError:
    print (noData, getHelp, use)
    errFile = open(errpath, "w+");
    errFile.write(now + "\n" + Error + myIsoList +  noExist)
    errFile.close()
    sys.exit()

#Pass isolates to list
for line in file:
    IsoID.append(line.strip())

    
#Check to see if the input file is empty
if (IsoID[0] == ""):
    print (noData, getHelp, use)
    errFile = open(errpath, "w+");
    errFile.write(now + "\n" +Error + IsoID +  noData)
    errFile.close()
    sys.exit()
    

for entry in IsoID: #Check for modifiers on files
    if myMod == "none":
        isoFile = entry + "_pulled.txt"
        #print(isoFile)
        isoOut =  entry + "_concat.txt"
    elif myMod == "_Example":
        isoFile = "Main\examples\\" + entry + myMod + "_pulled.txt"
        isoOut = entry + myMod + "_concat.txt"
    elif myMod != "none":
        isoFile = entry + myMod + "_pulled.txt"
        isoOut = entry + myMod + "_concat.txt"

    #open inputs and outputs for each
    isoIn = os.path.abspath(isoFile)
    isoFile = open(isoIn)
    
    #Checks if files are empty
    if (isoFile.readline() == ""):
        print (noData, getHelp, use)
        errFile = open(errpath, "w+");
        errFile.write(now + "\n" + noData + "for " + entry + ".")
        errFile.close()
        sys.exit()


    outpath = os.path.abspath(isoOut)
    OF = open(outpath,"w")
    
    #Nice little header
    OF.write(">" + entry + "\n")
    
    #Combine all lines
    for line in isoFile:
        if ">" not in line:
            OF.write(line.strip())
        
        
print("Done!")  
   