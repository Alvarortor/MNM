#Remaking genestracter


#Basically same as seqstracter, but need o look for specific line

#Imports
import os #So it can search through device
import re #Regexes
import sys #Accept input from command line but without needing to type

#Error checks
myFile= "none"
myGene = "none"
mydata = list()

#Error file holder for app
myEF = "GSError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Potential errors
noIn = "Error: Did not define input file."
noExist = "Error: File does not exist."
nogene = "Error: No gene selected."
getHelp = "Use the -h option for help"
myOption = "none"
use = "Genestracter.py <Isolate_chomp.txt> <gene>"

#Help and input errors
try:
    myFile= sys.argv[1] #input file
    myGene = sys.argv[2]   #specify scaffold number
except IndexError:
    if myFile == "-h" or myGene == "-h":
        print("help")
        sys.exit()
    elif myFile == "none":
        print(noIn,getHelp)
        errFile.write(noin)
        sys.exit()
    elif myGene == "none":
        print(nogene)
        errFile.write(nogene)
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



myFound = 0
#Get the gene from file
with open (myFile) as file:
    for line in file:
        line = line.strip()
        if myGene.lower() in line.lower(): #Uses lowercase to find so it doesn't need to be case perfect
            next_line = file.readline()
            next_line = next_line.strip() #Cleans it up a bit more
            myFound += 1
            mydata.append(line + "\n" + next_line + "\n")
            


        
        
#Create output
    if myFound > 0:
        myOF = myGene + ".txt"
        outpath = os.path.abspath(myOF)
        outFile = open(outpath, "w");
        for myitem in mydata:        
            outFile.write(myitem)
        print ("Found", myFound, "instance(s) of", myGene, "in", myFile)
    elif myFound == 0:
        print ("Could not find", myGene, "in", myFile)
        sys.exit()