#Get a word file and break up the sentence into words


#info
#Purpose:
#Converts .MUMs format for whole genome into .bed or PhenoGram input format.
#Uses Chromosome name and position relative to that chromosome
#IMPORTANT: Specify reference for absolute phenogram

#Imports
import os #So it can search through device
import re #Regemaxes
import sys #Accept input from command line but without needing to type
import math #For calculations



#input arguments
myFile = sys.argv[1]
myOption = input("Specify an option:\n-c for Circos\n-p for Phenogram relative\n-a for Phenogram absolute\n-b for Bedtools\n")



#Get path to the file and open
inpath = os.path.abspath(myFile)
file = open(inpath);

#Small counter to see how many lines there are
#Exits if line number emaxceeds mamaximum supported by circos
lineCount = 0
for line in file:
    lineCount += 1
if lineCount> 25000 and myOption == '-c':
    print("ERROR\nYour output file will be", lineCount, "lines.\nThe mamaximum input allowed for Circos is 25000.\nReduce the MUMs by filtering for genes (use -b option and convert into Bedtools format.\n")
    sys.exit() 
   
#Close and then reopen to restart the program   
file.close()  
file = open(inpath);

#Chromosome sizes for CBS138
Amax = 527800;
Bmax = Amax + 512655;
Cmax = Bmax + 594526;
Dmax = Cmax + 667900;
Emax = Dmax + 707423;
Fmax = Emax + 957515;
Gmax = Fmax + 1010292;
Hmax = Gmax + 1057388;
Imax = Hmax + 1142525;
Jmax = Imax + 1247563;
Kmax = Jmax + 1307090;
Lmax = Kmax + 1528264;
Mmax = Lmax + 1465272;

#BG2 Chromosome sizes
Ay = 510173;
By = Ay + 514772;
Cy = By + 554850;
Dy = Cy + 702307;
Ey = Dy + 708771;
Fy = Ey + 940328;
Gy = Fy + 1010829;
Hy = Gy + 1058141;
Iy = Hy + 759829;
Jy = Iy + 1244406;
Ky = Jy + 1310637;
Ly = Ky + 1895715;
My = Ly + 1486080;


#Subroutine section
def RefPosition (RefStart):
    if int(RefStart) < int(Amax):
        myStartCoord = int(RefStart)
        return (myStartCoord)
    elif(int(RefStart) < int(Bmax)):
        myStartCoord = int(RefStart)- int(Amax)
        return (myStartCoord)
    elif(int(RefStart) < int(Cmax)):
        myStartCoord = int(RefStart)- int(Bmax)
        return (myStartCoord)
    elif(int(RefStart) < int(Dmax)):
        myStartCoord = int(RefStart)- int(Cmax)
        return (myStartCoord)
    elif(int(RefStart) < int(Emax)):
        myStartCoord = int(RefStart)- int(Dmax)
        return (myStartCoord)
    elif(int(RefStart) < int(Fmax)):
        myStartCoord = int(RefStart)- int(Emax)
        return (myStartCoord)
    elif(int(RefStart) < int(Gmax)):
        myStartCoord = int(RefStart)- int(Fmax)
        return (myStartCoord)
    elif(int(RefStart) < int(Hmax)):
        myStartCoord = int(RefStart)- int(Gmax)
        return (myStartCoord)
    elif(int(RefStart) < int(Imax)):
        myStartCoord = int(RefStart)- int(Hmax)
        return (myStartCoord)
    elif(int(RefStart) < int(Jmax)):
        myStartCoord = int(RefStart)- int(Imax)
        return (myStartCoord)
    elif(int(RefStart) < int(Kmax)):
        myStartCoord = int(RefStart)- int(Jmax)
        return (myStartCoord)
    elif(int(RefStart) < int(Lmax)):
        myStartCoord = int(RefStart)- int(Kmax)
        return (myStartCoord)
    elif(int(RefStart) < int(Mmax)):
        myStartCoord = int(RefStart)- int(Lmax)
        return (myStartCoord)

def QuePosition(QueStart):
    if int(QueStart) < int(Ay):
        myStartCoord = int(QueStart)
        return (myStartCoord)
    elif(int(QueStart) < int(By)):
        myStartCoord = int(QueStart)- int(Ay)
        return (myStartCoord)
    elif(int(QueStart) < int(Cy)):
        myStartCoord = int(QueStart)- int(By)
        return (myStartCoord)
    elif(int(QueStart) < int(Dy)):
        myStartCoord = int(QueStart)- int(Cy)
        return (myStartCoord)
    elif(int(QueStart) < int(Ey)):
        myStartCoord = int(QueStart)- int(Dy)
        return (myStartCoord)
    elif(int(QueStart) < int(Fy)):
        myStartCoord = int(QueStart)- int(Ey)
        return (myStartCoord)
    elif(int(QueStart) < int(Gy)):
        myStartCoord = int(QueStart)- int(Fy)
        return (myStartCoord)
    elif(int(QueStart) < int(Hy)):
        myStartCoord = int(QueStart)- int(Gy)
        return (myStartCoord)
    elif(int(QueStart) < int(Iy)):
        myStartCoord = int(QueStart)- int(Hy)
        return (myStartCoord)
    elif(int(QueStart) < int(Jy)):
        myStartCoord = int(QueStart)- int(Iy)
        return (myStartCoord)
    elif(int(QueStart) < int(Ky)):
        myStartCoord = int(QueStart)- int(Jy)
        return (myStartCoord)
    elif(int(QueStart) < int(Ly)):
        myStartCoord = int(QueStart)- int(Ky)
        return (myStartCoord)
    elif(int(QueStart) < int(My)):
        myStartCoord = int(QueStart)- int(Ly)
        return (myStartCoord)

def RefChr(RefStart):
    if int(RefStart) <= int(Amax):
        return ("ChrA_C_glabrata_CBS138")
    elif(int(RefStart) < int(Bmax)):
        return ("ChrB_C_glabrata_CBS138")
    elif(int(RefStart) < int(Cmax)):
        return ("ChrC_C_glabrata_CBS138")
    elif(int(RefStart) < int(Dmax)):
        return ("ChrD_C_glabrata_CBS138")
    elif(int(RefStart) < int(Emax)):
        return ("ChrE_C_glabrata_CBS138")
    elif(int(RefStart) < int(Fmax)):
        return ("ChrF_C_glabrata_CBS138")
    elif(int(RefStart) < int(Gmax)):
        return ("ChrG_C_glabrata_CBS138")
    elif(int(RefStart) < int(Hmax)):
        return ("ChrH_C_glabrata_CBS138")
    elif(int(RefStart) < int(Imax)):
        return ("ChrI_C_glabrata_CBS138")
    elif(int(RefStart) < int(Jmax)):
        return ("ChrJ_C_glabrata_CBS138")
    elif(int(RefStart) < int(Kmax)):
        return ("ChrK_C_glabrata_CBS138")
    elif(int(RefStart) < int(Lmax)):
        return ("ChrL_C_glabrata_CBS138")
    elif(int(RefStart) < int(Mmax)):
        return ("ChrM_C_glabrata_CBS138")
    
#Gets chromosome name through above method
def QueChr(QueStart):
    if int(QueStart) <= int(Ay):
        return ("ChrA_C_glabrata_BG2")
    elif(int(QueStart) < int(By)):
        return ("ChrB_C_glabrata_BG2")
    elif(int(QueStart) < int(Cy)):
        return ("ChrC_C_glabrata_BG2")
    elif(int(QueStart) < int(Dy)):
        return ("ChrD_C_glabrata_BG2")
    elif(int(QueStart) < int(Ey)):
        return ("ChrE_C_glabrata_BG2")
    elif(int(QueStart) < int(Fy)):
        return ("ChrF_C_glabrata_BG2")
    elif(int(QueStart) < int(Gy)):
        return ("ChrG_C_glabrata_BG2")
    elif(int(QueStart) < int(Hy)):
        return ("ChrH_C_glabrata_BG2")
    elif(int(QueStart) < int(Iy)):
        return ("ChrI_C_glabrata_BG2")
    elif(int(QueStart) < int(Jy)):
        return ("ChrJ_C_glabrata_BG2")
    elif(int(QueStart) < int(Ky)):
        return ("ChrK_C_glabrata_BG2")
    elif(int(QueStart) < int(Ly)):
        return ("ChrL_C_glabrata_BG2")
    elif(int(QueStart) < int(My)):
        return ("ChrM_C_glabrata_BG2")

def RefColor(RefColor):
    if int(RefStart) < int(Amax):
        return (1)
    elif(int(RefStart) < int(Bmax)):
        return (2)
    elif(int(RefStart) < int(Cmax)):
        return (3)
    elif(int(RefStart) < int(Dmax)):
        return (4)
    elif(int(RefStart) < int(Emax)):
        return (5)
    elif(int(RefStart) < int(Fmax)):
        return (6)
    elif(int(RefStart) < int(Gmax)):
        return (7)
    elif(int(RefStart) < int(Hmax)):
        return (8)
    elif(int(RefStart) < int(Imax)):
        return (9)
    elif(int(RefStart) < int(Jmax)):
        return (10)
    elif(int(RefStart) < int(Kmax)):
        return (11)
    elif(int(RefStart) < int(Lmax)):
        return (12)
    elif(int(RefStart) < int(Mmax)):
        return (13)

def QueColor(QueColor):
    if int(RefStart) < int(Ay):
        return (1)
    elif(int(RefStart) < int(By)):
        return (2)
    elif(int(RefStart) < int(Cy)):
        return (3)
    elif(int(RefStart) < int(Dy)):
        return (4)
    elif(int(RefStart) < int(Ey)):
        return (5)
    elif(int(RefStart) < int(Fy)):
        return (6)
    elif(int(RefStart) < int(Gy)):
        return (7)
    elif(int(RefStart) < int(Hy)):
        return (8)
    elif(int(RefStart) < int(Iy)):
        return (9)
    elif(int(RefStart) < int(Jy)):
        return (10)
    elif(int(RefStart) < int(Ky)):
        return (11)
    elif(int(RefStart) < int(Ly)):
        return (12)
    elif(int(RefStart) < int(My)):
        return (13)

#Make file output and name based on specified option
def outName (myOption):
    if myOption == '-b':
        print("Coverting into bedtools format")
        return ("OutMUMs.bed")
    elif myOption == '-c':
        print("Coverting into circos format")
        return ('MUMlinks.txt')
    elif myOption == '-p' or '-a':
        print("Coverting into phenogram format")
        return('MUMMap.txt')
       
#Will create file if it doesn't emaxits, but overwrite any with same name if it is present      
try:
    myOF = outName(myOption)
    OF = open(myOF, "x");
except FileExistsError:
    OF = open(myOF, "w");
except TypeError:
    print ("Option does not exist")
    sys.exit()

myStrain = input("Specify strain used as reference CBS138 or BG2\n")  
    

    
#Create headers for the specific outfiles
if myOption == '-p' or '-a':
    OF.write("Chr\tPos\tEnd\tPoscolor\tPhenotype\n")
elif myOption == '-b':
    OF.write("chrom\tchromStart\tchromEnd\tname\n")


#Time to actually start to work on this program
if myOption == ('-b' or '-c'):  
    for line in file:
        data = line.split()
        RefStart = data[0]
        QueStart = data[1]
        Len = data[2]
        Rchr = RefChr(RefStart)
        Rpos = RefPosition(RefStart)
        Rend = int(Rpos) + int(Len)
        Qchr = QueChr(QueStart)
        Qpos = QuePosition(QueStart)
        Qend = int(Qpos) + int(Len)
        
        
        #Combine everything into one string
        RefData = str(Rchr) + "break1" + str(Rpos) + "break2" + str(Rend) + "\t"
        QueData = str(Qchr) + "break1" + str(Qpos) + "break2" + str(Qend) + "\t"
        
        if myStrain == "CBS138":
            finalRef = RefData.replace("break1","\t")
            finalRef = finalRef.replace("break2","\t")
            finalQue = QueData.replace("break1",":")
            finalQue = finalQue.replace("break2","-")
            output =  (finalRef + finalQue)
        elif myStrain == "BG2":
            finalRef = RefData.replace("break1",":")
            finalRef = finalRef.replace("break2","-")
            finalQue = QueData.replace("break1","\t")
            finalQue = finalQue.replace("break2","\t")
            output = (finalQue + finalRef)
        
        #Write to output
        OF.write(output)
elif myOption == '-p': #Phenogram relative
        for line in file:
            data = line.split()
            RefStart = data[0]
            QueStart = data[1]
            Len = data[2]
            Rchr = RefChr(RefStart)
            Rpos = RefPosition(RefStart)
            Rend = int(Rpos) + int(Len)
            Rcol = RefColor(RefStart)
            Qchr = QueChr(QueStart)
            Qpos = QuePosition(QueStart)
            Qend = int(Qpos) + int(Len)
            Qcol = QueColor(QueStart)
        
            RefData = str(Rchr) + "\t" + str(Rpos) + "\t" + str(Rend) + "\t" + str(Rcol)
            QueData = str(Qchr) + "\t" + str(Qpos) + "\t" + str(Qend) + "\t" + str(Qcol)
        
            if myStrain == "CBS138":
                OF.write(RefData + "\n")
            elif myStrain == "BG2":
                OF.write(QueData + "\n")
elif myOption == '-a': #Phenogram absolute
    for line in file:
        data = line.split()
        RefStart = data[0]
        QueStart = data[1]      
        Len = data[2]
        Rchr = RefChr(RefStart)
        Rpos = RefPosition(RefStart)
        Rend = int(Rpos) + int(Len)
        Rcol = RefColor(RefStart)
        Qchr = QueChr(QueStart)
        Qpos = QuePosition(QueStart)
        Qend = int(Qpos) + int(Len)
        Qcol = QueColor(QueStart)
        Qabspos = int(QueStart) + int(Len)
        Rabspos = int(RefStart) + int(Len)
        
        RefData = str(Rchr) + "\t" + str(Rpos) + "\t" + str(Rend) + "\t" + str(Rcol) + "\t"
        QueData = str(Qchr) + "\t" + str(Qpos) + "\t" + str(Qend) + "\t" + str(Qcol) + "\t"
        
        if myStrain == "CBS138":
            OF.write(RefData + str(QueStart) + ":" + str(Qabspos) + "\n")
        elif myStrain == "BG2":
            OF.write(QueData + str(RefStart)  + ":" + str(Rabspos) + "\n")


        
      
