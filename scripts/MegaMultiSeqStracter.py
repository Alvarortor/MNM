#Remake MegaMultiSeqstracter

#Purpose: Extract specific regions of interest from a show-coords output
#Usage: MegaMultiSeqstracter.pl <isolatefile.txt> <modifier> 
#One isolate per line in isolate file
#One gene per line in gene file")

#imports
import re
import os
import sys
from time import process_time
from collections import Counter


#Temporary errors
myIso= "none"
myMod = "none"

#Error file holder for app
myEF = "MMSeqError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Potential errors
noIn = "Error: Did not select iso."
noIsoFind = "Error: Could not find specified isolate"
noExist = "Error: File does not exist."
getHelp = "Use the -h option for help"
use = "MultiSeqStracter <Isolate> <file_modifier>"
purp = "Purpose: Extract specific regions of interest from a show-coords output\nUsage: MegaMultiSeqstracter.pl <isolatefile.txt> <modifier> \nOne isolate per line in isolate file\nOne gene per line in gene file"
print("Running...")
tot_start = process_time() 
#Holder errors



#Inputs and help
try:
    Iso_list = sys.argv[1]
    my_mod = sys.argv[2]
except IndexError:
    if Iso_list == "none":
        print("No isolate file specified")
        errFile.write(noIn)
        sys.exit()
        
if Iso_list == "-h" or my_mod == "-h":
    print(purp)
    sys.exit()
    

#Paths
try:
    inpath = os.path.abspath(str(Iso_list))
    inIso = open(inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    errFile.write(noExist)
    errFile.close()
    sys.exit()


#Lists
myData = list()   
myDups = list()
myErrs = list()

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
    fileName = iso + "_chomp.txt"
    seqpath = os.path.abspath(fileName)
    SF = open(seqpath);
    flipScore = FS;
    for sqline in SF:
        sqline = sqline.strip()
        if str(sqline) == str(">"+scaffold): #automatically loops
            next_line = SF.readline()
            next_line = next_line.upper()
            substr = next_line[shortstart:][:longLen]
            return(substr)
            
 #3 Finalize length           
def Trimmer(finalSeq):
    startPos = roughSeq.find("ATG")
    if startPos <= 10:
        data = roughSeq[int(startPos):][:int(LEN)]
        return(data)
    elif startPos > 10:
        comp = roughSeq[::-1].translate(roughSeq.maketrans("ATCGatgc", "TAGCtagc"))
        revstart = comp.find("ATG")
        data = comp[int(revstart):][:int(LEN)]
        return(data)


print("Isolate\t\tStatus\tProcessing time(s)")



#Adds modifier to help locate correct input file
for bug in inIso:
    
    t_start = process_time() 
    iso = bug.strip()
    if my_mod == "none":
        coord_file = (iso + ".coords")
        outFile = (iso + "_genes.txt")
    else:
        coord_file = (iso + my_mod + ".coords")
        outFile = (iso + my_mod + "_genes.txt")
        
    #Open inputs for each isolate
    coord_path = os.path.abspath(coord_file)
    errFile.write("Cannot find coord file.")

        
    out_path = os.path.abspath(outFile)
    incoord = open(coord_path) 
    OF = open(out_path, "w")
    
    with open(coord_path) as file:
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
            myDups.append(gene + "\t" + iso)
            
            OF.write(">" + iso +"_" + gene + "_" + seqStart+ "_"+ seqEnd + "_LEN:" + LEN + "\n" + finalSeq + "\n")
            t_stop = process_time()
        time_diff = str(t_stop - t_start)
        print((iso + '{:<5} '+ "\t" + "Done"+ "\t" + time_diff).format(''))
            
#Checks for duplicates
if len(myDups) != len(set(myDups)):
    ErPath = os.path.abspath("MMSSErrors.txt")
    ErrorFile = open(ErPath, "w");
    myErrs.append({x for x in myDups if myDups.count(x) > 1})
    print ("Some errors detected, creating extraction error file")
    
else:
    print ("Done!")
    

for errors in myErrs:
    counter = Counter(myDups)
    duplicates = [item for item, count in counter.items() if count > 1]

#Temporarily stores duplicated data
temp = list()

err_signal = 0    
for item in duplicates:
        labels = item.split()
        n = myDups.count(item)
        count = str(n)
        #error_tag = str(labels[0]) + " appears in " + str(n) + " MUMs for " + labels[1] +"\n"
        err_signal += 1
        #errors = str(error_tag) #Removes little bracket and commas
        gene = str(labels[0])
        iso = str(labels[1])
        a = [gene, iso, count]
        temp.append(a)
        

b = 0
a = sorted(temp)
for labels in a:
    n = myDups.count(item)
    error_tag = str(labels[0]) + " appears in " + labels[2] + " MUMs for " + labels[1] +"\n"    
    a.pop(0)
    ErrorFile.write(error_tag)


tot_end = process_time()
time_diff = str(tot_end - tot_start)
print("Total run time was : " + time_diff + "(s)")

if err_signal > 0:
    os.startfile("MMSSErrors.txt")