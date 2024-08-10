#MultiSeqstracter
#Purpose: Extracts regions from a single or multiFastA input file
#Usage Seqstracter.py <file.coords> <isolate>

#Imports
import os #So it can search through device
import re #Regexes
import sys #Accept input from command line but without needing to type
from collections import Counter

#Temporary errors
myIso= "none"
myMod = "none"

#Error file holder for app
myEF = "MSeqError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Potential errors
noIn = "Error: Did not select iso."
noIsoFind = "Error: Could not find specified isolate"
noExist = "Error: File does not exist."
getHelp = "Use the -h option for help"
use = "MultiSeqStracter <Isolate> <file_modifier>"



try:
    myIso= sys.argv[1] #input file
    myMod = sys.argv[2]   #specify modifier
except IndexError:
    if myIso == "-h" or myMod == "-h":
        print(use)
        sys.exit()
    elif myIso == "none":
        print(noIn, getHelp)
        errFile.write(noIn)
        sys.exit()


#Modifier check
if myMod == "none":
    myFile = myIso + ".coords"
    myOF = myIso + "_genes.txt"
    
else:
    myFile = myIso + myMod + ".coords"
    myOF = myIso + myMod + "_genes.txt"


print("Running MultiSeqStracter on " + myFile)


#lists
myData = list()   
myDups = list()
myErrs = list()
duplicates = list()
        

try:
    inpath = os.path.abspath(str(myFile))
    file = open(inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    errFile.write(noExist)
    errFile.close()
    sys.exit()


#Make output file
outpath = os.path.abspath(myOF)
outFile = open(outpath, "w");


#Functions
#1 Check for flip
def FlipCheck(flipscore):
    if geneStart > geneEnd: 
        return 1
    else:
        return 0
        
#2 Get rough sequence
def Puller(roughSeq):
    shortstart = int(seqStart) - 10
    longLen = (int(seqEnd) + 10 ) - shortstart
    fileName = myIso + "_chomp.txt"
    seqpath = os.path.abspath(fileName)
    SF = open(seqpath);
    flipScore = FS;
    for sqline in SF:
        sqline = sqline.strip()
        if str(sqline) == str(">"+scaffold): #automatically loops
            next_line = SF.readline()
            substr = next_line[shortstart:][:longLen]
            return(substr)
            
 #3 Finalize length           
def Trimmer(finalSeq):
    startPos = roughSeq.find("ATG")
    if startPos < 10:
        data = roughSeq[int(startPos):][:int(LEN)]
    elif startPos > 10:
        comp = roughSeq[::-1].translate(roughSeq.maketrans("ATCG", "TAGC"))
        revstart = comp.find("ATG")
        data = comp[int(revstart):][:int(LEN)]
    return(data)
    



#start to process the files
with open(myFile) as file:
    current_line = 0
    while int(current_line) < 4:
        line = file.readline()
        current_line += 1
        if int(current_line) == 4:
            break                       #Skips until actual data line
    for line in file:
        x = line.split()#Split whenever there is a tab
        seqStart = x[0]
        seqEnd = x[1]
        geneStart = x[2]
        geneEnd = x[3]
        LEN =x[4]
        scaffold = x[7]
        gene = x[8]
        
        flipscore = [geneStart, geneEnd]
        FS = (FlipCheck(flipscore))
        
        roughSeq = Puller([FS, geneStart, geneEnd, scaffold, seqStart, seqEnd])      
        finalSeq = Trimmer([roughSeq, LEN])
        myDups.append(gene)
        myData.append(">" + myIso +"_" + gene + "_" + seqStart+ "_"+ seqEnd + "_LEN:" + LEN+ "\n" + finalSeq + "\n")

for entry in myData:
    outFile.write(entry)
    
#Checks for duplicates
if len(myDups) != len(set(myDups)):
    ErPath = os.path.abspath("ExtractionErrors.txt")
    ErrorFile = open(ErPath, "w");
    myErrs.append({x for x in myDups if myDups.count(x) > 1})
    print ("Some errors detected, creating extraction error file")
    
else:
    print ("Done!")
for errors in myErrs:
    counter = Counter(myDups)
    duplicates = [item for item, count in counter.items() if count > 1]

err_signal = 0
for item in duplicates:
    n = myDups.count(item)
    error_tag = str(item) + " appears in " + str(n) + " MUMs, check to make sure it extracted correctly"
    errors = str(error_tag) #Removes little bracket and commas
    ErrorFile.write(errors)
    err_signal += 1
    print ("Check output error file")
   
if err_signal > 0:
    os.startfile("ExtractionErrors.txt")
