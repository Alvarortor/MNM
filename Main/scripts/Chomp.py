#Chomp
#Purpose: Converts FastA and multiFastA into a .txt format readable by Seqstracter. Allows for extraction of genomic regions. 
#Usage:  Chomp.py <File.fastA> <OutputName>

#Imports
import os #So it can search through device
import re #Regexes
import sys #Accept input from command line but without needing to type
import datetime #To get accurate timeframes for errors


#Blank statements sthat get overwritten later
myFile = "none"
myStrain = "none"



#Error file holder for app
myEF = "Error.log"
errpath = os.path.abspath(myEF)
#Clear errors
open(errpath, "w+").close()
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


#Potential errors
Error = "Error: "
noStrain = "Error: Did not define strain name for output."
noIn = "Error: Did not define input file."
noExist = " does not exist."
getHelp = "Use the -h option for help"
use = "Chomp.py <file.txt>"
noData = " is blank."

print(myFile)
#input arguments
try:
    myFile = sys.argv[1]
    print(myFile,"test")
    myStrain = sys.argv[2]
except IndexError:
    if myFile == "none":
        print("test")
        print (noIn, getHelp)
        errFile = open(errpath, "w+");
        errFile.write(now + "\n" + noIn)
        errFile.close
        sys.exit()

    elif myStrain == "none" or myStrain == "": #need to include blanks to help with program since blank entries may be possible
        print (noStrain,getHelp, use)
        errFile = open(errpath, "w+");
        errFile.write(now + "\n" + noStrain)
        errFile.close()
        sys.exit()

#Catches -h in strain spot  
if myFile == "-h" or myStrain == "-h":  
    print("Purpose: Converts FastA and multiFastA into a .txt format readable by Seqstracter.\nAllows for extraction of genomic regions.\nUsage:  Chomp.py <File.fastA> <OutputName>")
    sys.exit()    

#Get path to the file
try: 
    inpath = os.path.abspath(myFile)
    file = open(inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp)
    errFile = open(errpath, "w+");
    errFile.write(now + "\n" + Error + myFile + noExist)
    errFile.close()
    sys.exit()

#Mini check to look for blank files
if (file.readline() == ""):
    print (noData, getHelp, use)
    
    errFile = open(errpath, "w+");
    errFile.write(now + "\n" + Error + myFile + noData)
    errFile.close()
    sys.exit()
    
    
#Create outputs
myOF = myStrain + "_chomp.txt"
outpath = os.path.abspath(myOF)
outFile = open(outpath, "w");

#small count to help me keep track
count = 0


#Open our input


for line in file:
    if ">" in line:
        if count == 0:
            count += 1
            line = line
        else:
            line = "\n" + line #separates second header if its a multifastA
    else:
        line = line.replace('\n','')
    outFile.write(line)
file.close

print("Done!")
