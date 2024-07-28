#Try to get a brick with clickable entries
#!/usr/bin/env python



#Imports
import sys
import os
import subprocess
import io
import webbrowser
import re
import time

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#Default state is no errors, gets changed when theres an issue
global error
global m
global w
global w1
error = False




#Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        app = QApplication(sys.argv) #Add a menubar with citations?
        widget = QWidget()
        
        
        #Hold QR code to github
        text = QPushButton(widget)
        image = QPixmap('assets\QR.png')
        image = image.scaled(175,175)
        text.move(200,50)
        text.setIcon(QIcon(image))
        text.setFixedSize(175,175)
        text.setIconSize(QSize(200,200))
        text.setToolTip("Alvaro's GitHub")
        text.clicked.connect(openGitHub)
        
        
        text1 = QLabel(widget)
        text1.setText("Select which type of analysis to perform:")
        text1.move(15,15)
        text1.setFont(QFont('Arial', 11))
        
        button1 = QPushButton(widget)
        button1.setText("String Manipulation")
        button1.setGeometry(15,60,150,40)
        button1.setFont(QFont('Arial',10))
        button1.clicked.connect(manip_options)

        button2 = QPushButton(widget)
        button2.setText("String Extraction")
        button2.setGeometry(15,120,150,40)
        button2.setFont(QFont('Arial', 10))
        button2.clicked.connect(ext_options)

        button3 = QPushButton(widget)
        button3.setText("Help")
        button3.setGeometry(15,180,150,40)
        button3.setFont(QFont('Arial', 10))
        button3.clicked.connect(help_options) #Just opens the ReadMe file
        
            
        widget.setGeometry(400,400,425,250)
        widget.setWindowTitle("MUM's n' More")

        widget.show()
        sys.exit(app.exec_())
        
class NotYet(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Working on it")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setGeometry(400,400,400,200)
        self.setWindowTitle("Sorry Homie")
        self.setFont(QFont('Arial', 10))

#Manipulation programs     
class ManipWindow(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()

        
        
        layout = QVBoxLayout()
        self.label1 = QLabel("Text/FastA Manipulation Tools")
        self.label1.setFont(QFont('Arial', 12))
        layout.addWidget(self.label1)

        
        self.btn1 = QPushButton("Chomp")
        self.btn1.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn1)
        self.btn1.clicked.connect(chomp_time)   
        
        
        self.btn2 = QPushButton("Flipper")
        self.btn2.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn2)
        self.btn2.clicked.connect(flip_time)   
        
        self.btn3 = QPushButton("BunkBed")
        self.btn3.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn3)
        self.btn3.clicked.connect(bunk_time)   
        
        self.btn4 = QPushButton("Zelda")
        self.btn4.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn4)
        self.btn4.clicked.connect(zelda_time)   
        
        self.btn5 = QPushButton("Link")
        self.btn5.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn5)
        self.btn5.clicked.connect(link_time)   
        
        self.label2 = QLabel("MUMmer Manipulation Tools")
        self.label2.setFont(QFont('Arial', 12))
        layout.addWidget(self.label2)
        
        
        self.btn6 = QPushButton("JAMS")
        self.btn6.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn6)
        self.btn6.clicked.connect(jam_time)   
        
        self.btn7 = QPushButton("MUMCleaner")
        self.btn7.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn7)
        self.btn7.clicked.connect(mumclean_time)   
        
        self.btn8 = QPushButton("MUMi")
        self.btn8.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn8)
        self.btn8.clicked.connect(mumi_time)   
        
        self.label3 = QLabel("NCBI Manipulation Tools")
        self.label3.setFont(QFont('Arial', 12))
        layout.addWidget(self.label3)
        
        
        self.btn12 = QPushButton("FastAFetcher")
        self.btn12.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn12)
        self.btn12.clicked.connect(fastA_time)
        
        self.btn12 = QPushButton("Back")
        self.btn12.setFont(QFont('Arial', 10))
        self.btn12.setFixedWidth(90)
        layout.addWidget(self.btn12)
        self.btn12.clicked.connect(selfhide)   
        
        
        self.setLayout(layout) 
        self.setGeometry(400,400,425,2)
        self.setWindowTitle("String Manipulation")
        self.show()    
       
class HelpWindow (QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        
        layout = QVBoxLayout()
        
        label1 = QPushButton("What does each program do?")
        label1.setFont(QFont('Arial',10))
        label1.clicked.connect(show_help)
        layout.addWidget(label1)
        
        label2 = QPushButton("How do I use these programs?")
        label2.setFont(QFont('Arial',10))
        label2.clicked.connect(show_use)
        layout.addWidget(label2)
        
        label3 = QPushButton("Where can I get help?")
        label3.setFont(QFont('Arial',10))
        label3.clicked.connect(openGitHub)
        layout.addWidget(label3)
        
        label4 = QPushButton("What else does your lab do?")
        label4.setFont(QFont('Arial',10))
        label4.clicked.connect(openLab)
        layout.addWidget(label4)
        
        self.btn12 = QPushButton("Back")
        self.btn12.setFont(QFont('Arial', 10))
        self.btn12.setFixedWidth(90)
        layout.addWidget(self.btn12)
        self.btn12.clicked.connect(selfhide)           
        
        self.setLayout(layout) 
        self.setGeometry(400,400,400,200)
        self.setWindowTitle("Help")
        self.show()    
#Extraction programs
class ExtracWindow(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        layout = QVBoxLayout()
        self.label1 = QLabel("Sequence Extraction Tools")
        self.label1.setFont(QFont('Arial', 12))
        layout.addWidget(self.label1)
        
        self.btn1 = QPushButton("SeqStracter")
        self.btn1.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn1)
        self.btn1.clicked.connect(seqstract_time)   
        
        self.btn2 = QPushButton("MultiSeqStracter")
        self.btn2.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn2)
        self.btn2.clicked.connect(mseqstract_time)   
        
        self.btn3 = QPushButton("MegaMultiSeqStracter")
        self.btn3.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn3)
        self.btn3.clicked.connect(mmseqstract_time)   
        
        self.label2 = QLabel("Gene Extraction Tools")
        self.label2.setFont(QFont('Arial', 12))
        layout.addWidget(self.label2)
        
        self.btn4 = QPushButton("GeneStracter") 
        self.btn4.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn4)
        self.btn4.clicked.connect(genestract_time)   
        
        self.btn5 = QPushButton("MultiGeneStracter")
        self.btn5.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn5)
        self.btn5.clicked.connect(mgenestract_time)   
        
        self.btn6 = QPushButton("MegaMultiGeneStracter")
        self.btn6.setFont(QFont('Arial', 10)) 
        layout.addWidget(self.btn6)
        self.btn6.clicked.connect(mmgenestract_time)   
        
        self.btn7 = QPushButton("RandoPuller")
        self.btn7.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn7)
        self.btn7.clicked.connect(randogene_time)  
        
        self.btn12 = QPushButton("Back")
        self.btn12.setFont(QFont('Arial', 10))
        self.btn12.setFixedWidth(90)
        layout.addWidget(self.btn12)
        self.btn12.clicked.connect(selfhide)   
        
        self.setLayout(layout) 
        self.setGeometry(400,400,425,250)
        self.setWindowTitle("String Extraction")
        self.show()    
  
#Checks for errors and creates message if any appear
class Error(QWidget):
    global error

    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Whoops!")
        msg.setInformativeText(errMess + " Specify path if not in the same directory.")
        msg.setFont(QFont('Arial',10))
        msg.setWindowTitle("Error!")
        msg.setGeometry(450,400,250,100)
        error = error_hold()
        
        msg.exec_()
        print(error)

class Working(QWidget): #Mayeb finalize later? I don't know how to make it work and I dont want to try rn
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        msg = QVBoxLayout()
        
        text = QLabel("This process takes some time.")
        text.setWordWrap(True)
        text.setFont(QFont('Arial',10))
        

        
        progress = QProgressBar(self)
        progress.setGeometry(200, 100, 300, 50)
        
        msg.addWidget(text)
        msg.addWidget(progress)
        
        self.setLayout(msg)
        self.setWindowTitle("In Progress")
        self.setGeometry(550,300,300,100)
 
        
        
        
#Mini program specifics
class Chomp(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        global usrin1
        global usrin2
        global marg1
        global infolbl
        


        #So you can pick an isolate
        layout = QGridLayout()


        tb = QToolBar();
        ex_btn = QAction("Example",self)
        tb.addAction(ex_btn);
        ex_btn.triggered.connect(chomp_ex)
        infolbl = QLabel(" ")
        layout.setMenuBar(tb)
        layout.addWidget(infolbl,2,1)
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        
        layout.addWidget(backbtn,2,0)

        usrin1 = QLineEdit()
        self.usrin1 = usrin1
        self.usrin1.setFont(QFont('Arial',10))
        
        prompt1 = QLabel("Enter File:")
        prompt1.setFont(QFont('Arial', 10)) 
        prompt1.setWordWrap(True)
        prompt1.setFixedWidth(100)
        
        layout.addWidget(prompt1,0,0)
        layout.addWidget(self.usrin1,0,1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
   
   
        usrin2 = QLineEdit()
        self.usrin2 = usrin2
        self.usrin2.setFont(QFont('Arial',10))
        
        prompt2 = QLabel("Output prefix:")
        prompt2.setFont(QFont('Arial', 10)) 
        prompt2.setWordWrap(True)
        prompt2.setFixedWidth(100)
        layout.addWidget(prompt2,1,0)
        layout.addWidget(self.usrin2,1,1)
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
        
        
        pickFile = QPushButton("Browse for file")
        pickFile.setFont(QFont('Arial',10))
        fn1 = pickFile.clicked.connect(file1_find)
        layout.addWidget(pickFile,0,2)
               
               
        Go = QPushButton("CHOMP!")
        Go.setFont(QFont('Arial',10))
        self.Go = Go
        Go.pressed.connect(chomp)
        Go.pressed.connect(finished_Process)
        
        

        layout.addWidget(Go,2,2)
        self.setLayout(layout)
        self.setGeometry(850,400,450,200)
        self.setWindowTitle("Chomp")
        
class Flipper(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()    
        global usrin1
        global infolbl
        global marg1
        
        layout = QGridLayout()
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)
        tb.addAction(ex_btn);
        ex_btn.triggered.connect(flip_ex)
        infolbl = QLabel(" ")
        layout.setMenuBar(tb)
        layout.addWidget(infolbl,2,1)
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        layout.addWidget(backbtn,2,0)
        
        usrin1 = QLineEdit()
        usrin1.setFont(QFont('Arial',10))
        self.usrin1 = usrin1
        
        prompt1 = QLabel("Select File:")
        prompt1.setFont(QFont('Arial', 10)) 
        prompt1.setFixedWidth(100)
        prompt1.setWordWrap(True)
        layout.addWidget(prompt1,0,0)
        layout.addWidget(self.usrin1,0,1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
        
        start = QPushButton("Flip!")
        start.setFont(QFont('Arial',10))
        start.clicked.connect(flip)
        start.clicked.connect(finished_Process)
        
        pickFile = QPushButton("Browse")
        pickFile.setFont(QFont('Arial',10))
        fn1 = pickFile.clicked.connect(file1_find)
        layout.addWidget(pickFile,0,2)

        
        layout.addWidget(start,2,2)
        self.setLayout(layout)
        self.setGeometry(850,400,450,200)
        self.setWindowTitle("Flipper")

class BunkBed(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()    
        global usrin1
        global marg1
        global opt1
        global opt2
        global infolbl
        

        layout = QGridLayout()
        
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)
        tb.addAction(ex_btn);
        ex_btn.triggered.connect(bunk_ex)
        infolbl = QLabel(" ")
        layout.setMenuBar(tb)
        layout.addWidget(infolbl,2,1)
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(90)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        
        layout.addWidget(backbtn,2,0)        
        
        
        buttons = QVBoxLayout()
        
        usrin1 = QLineEdit()
        self.usrin1 = usrin1
        self.usrin1.setFont(QFont('Arial',10))
        
        prompt1 = QLabel("Enter file to be bunked:")
        prompt1.setWordWrap(True)
        prompt1.setFont(QFont('Arial', 12))
        layout.addWidget(prompt1,0,0)
        layout.addWidget(self.usrin1,0,1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
        
        start = QPushButton("Bunk!")
        start.setFixedWidth(90)
        start.setFont(QFont('Arial',10))
        start.clicked.connect(bunk)
        start.clicked.connect(finished_Process)
        
        opt1 = QCheckBox("Count number of duplicates")
        opt1.setFont(QFont('Arial',10))
        buttons.addWidget(opt1)
        
        opt2 = QCheckBox("Only return genes")
        opt2.setFont(QFont('Arial',10))
        buttons.addWidget(opt2)
        
        
        pickFile = QPushButton("Browse")
        pickFile.setFont(QFont('Arial',10))
        fn1 = pickFile.clicked.connect(file1_find)
        layout.addWidget(pickFile,0,2)
        layout.addLayout(buttons,1,0)
        
        layout.addWidget(start,2,2)
        self.setLayout(layout)
        self.setGeometry(850,400,550,250)
        self.setWindowTitle("BunkBed")

class Zelda(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()    
        global usrin1
        global marg1
        global infolbl
        
        layout = QGridLayout()
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)
        tb.addAction(ex_btn);
        ex_btn.triggered.connect(zeld_ex)
        infolbl = QLabel(" ")
        infolbl.setWordWrap(True)
        layout.setMenuBar(tb)
        layout.addWidget(infolbl,2,1)
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        layout.addWidget(backbtn,2,0)
        
        usrin1 = QLineEdit()
        self.usrin1 = usrin1
        
        prompt1 = QLabel("Select Isolate File:")
        prompt1.setFont(QFont('Arial', 10)) 
        prompt1.setWordWrap(True)
        layout.addWidget(prompt1,0,0)
        layout.addWidget(self.usrin1,0,1)
        usrin1.setFont(QFont('Arial',10))
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
        
        usrin2 = QLineEdit()
        self.usrin2 = usrin2
        usrin2.setFont(QFont('Arial',10))
        prompt2 = QLabel("Optional file modifier:")
        prompt2.setWordWrap(True)
        prompt2.setFont(QFont('Arial', 10)) 
        layout.addWidget(prompt2,1,0)
        layout.addWidget(self.usrin2,1,1)
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
        start = QPushButton("Go!")
        start.clicked.connect(zelda)
        start.setFont(QFont('Arial',10))
        start.clicked.connect(finished_Process)
        
        pickFile = QPushButton("Browse")
        pickFile.setFixedWidth(90)
        pickFile.setFont(QFont('Arial',10))
        
        fn1 = pickFile.clicked.connect(file1_find)
        layout.addWidget(pickFile,0,2)

        
        layout.addWidget(start,2,2)
        self.setLayout(layout)
        self.setGeometry(850,400,600,100)
        self.setWindowTitle("Zelda")
        
class Link(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()    
        global usrin1
        global marg1
        global infolbl
        
        layout = QGridLayout()
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)
        tb.addAction(ex_btn);
        ex_btn.triggered.connect(link_ex)
        infolbl = QLabel(" ")
        infolbl.setWordWrap(True)
        layout.setMenuBar(tb)
        layout.addWidget(infolbl,2,1)
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        layout.addWidget(backbtn,2,0)
        
        usrin1 = QLineEdit()
        self.usrin1 = usrin1
        
        prompt1 = QLabel("Select Isolate File:")
        prompt1.setFont(QFont('Arial', 10)) 
        layout.addWidget(prompt1,0,0)
        layout.addWidget(self.usrin1,0,1)
        usrin1.setText("Iso_list.txt")
        usrin1.setFont(QFont('Arial',10))
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
        
        usrin2 = QLineEdit()
        self.usrin2 = usrin2
        usrin2.setFont(QFont('Arial',10))
        prompt2 = QLabel("Optional file modifier:")
        prompt2.setWordWrap(True)
        prompt2.setFont(QFont('Arial', 10)) 
        layout.addWidget(prompt2,1,0)
        layout.addWidget(self.usrin2,1,1)
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
        start = QPushButton("Go!")
        start.clicked.connect(link)
        start.setFont(QFont('Arial',10))
        start.clicked.connect(finished_Process)
        
        pickFile = QPushButton("Browse")
        pickFile.setFixedWidth(90)
        pickFile.setFont(QFont('Arial',10))
        
        fn1 = pickFile.clicked.connect(file1_find)
        layout.addWidget(pickFile,0,2)

        
        layout.addWidget(start,2,2)
        self.setLayout(layout)
        self.setGeometry(850,400,550,100)
        self.setWindowTitle("Link")

class JAMS(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()    
        global usrin1
        global marg1
        global text
        global opt1
        global opt2
        global opt3
        global infolbl
        global ref

        
        layout = QGridLayout()
        ref_layout = QFormLayout()

        tb = QToolBar();
        ex_btn = QAction("Example",self)
        tb.addAction(ex_btn);
        ex_btn.triggered.connect(jam_ex)
        infolbl = QLabel(" ")
        infolbl.setWordWrap(True)
        layout.setMenuBar(tb)
        layout.addWidget(infolbl,3,1)
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        layout.addWidget(backbtn,3,0)
        
        usrin1 = QLineEdit()
        usrin1.setFont(QFont('Arial',10))
        self.usrin1 = usrin1
        
        prompt1 = QLabel("Select Input File: ")
        prompt1.setFixedWidth(90)
        prompt1.setFont(QFont('Arial', 10)) 

        marg1 = self.usrin1.textChanged.connect(marg1_hold)
        pickFile = QPushButton("Browse")
        pickFile.setFont(QFont('Arial',10))
        fn1 = pickFile.clicked.connect(file1_find)
        
        
        prompt2 = QLabel("Select Reference: ")
        prompt2.setWordWrap(True)
        prompt2.setFont(QFont('Arial', 10)) 
        prompt2.setFixedWidth(90)
        
        ref = QComboBox()
        ref.addItem("None")
        ref.addItem("Ng_CBS138")
        ref.addItem("Ng_BG2")
        ref.addItem("Ca_SC5314")
        ref.addItem("Sc_S288C")
        ref.addItem("Other")
        ref.setFont(QFont('Arial',10))
       # ref.setFixedWidth(100)
        

        a = ref.currentTextChanged.connect(test)
        pickFile2 = QPushButton("Other")
        pickFile2.setFont(QFont('Arial',10))
       # pickFile2.setFixedWidth(20)
        fn2 = pickFile2.clicked.connect(file2_find)
            
        prompt3 =QLabel("Select conversion format:")
        prompt3.setWordWrap(True)
        prompt3.setFont(QFont('Arial', 10)) 
        prompt3.setFixedWidth(90)
        
  
        
        options = QGroupBox()
        opt1 = QRadioButton("Bedtools")
        opt2 = QRadioButton("PhenoGram")
        opt3 = QRadioButton("Circos")
        
        opt1.setFont(QFont('Arial',10))
        opt2.setFont(QFont('Arial',10))
        opt3.setFont(QFont('Arial',10))
        
        opt1.toggled.connect(BedTools)
        opt2.toggled.connect(PhenoGram)
        opt3.toggled.connect(Circos)
        
        opt1.setChecked(True)
        
        vbox = QVBoxLayout()
        vbox.addWidget(opt1)
        vbox.addWidget(opt2)
        vbox.addWidget(opt3)
        options.setLayout(vbox)
        
        
        layout.addWidget(prompt1,0,0)
        layout.addWidget(self.usrin1,0,1)
        layout.addWidget(pickFile,0,2)
        
        
        layout.addWidget(prompt2,1,0)
        layout.addWidget(ref,1,1)
        layout.addWidget(pickFile2,1,2)

        layout.addWidget(prompt3,2,0)
        layout.addWidget(options,2,1)
        
        start = QPushButton("Go!")
        start.clicked.connect(jams)
        start.setFont(QFont('Arial',10))
        start.clicked.connect(finished_Process)
        layout.addWidget(start,3,2)
        
        
        self.setLayout(layout)
        self.setGeometry(850,400,450,100)
        self.setWindowTitle("Just Add MUMS")
        
class MUMCleaner(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        global usrin1
        global marg1
        global marg2
        global infolbl
        
        #So you can pick an isolate
        layout = QGridLayout()
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)
        tb.addAction(ex_btn);
        ex_btn.triggered.connect(mumclean_ex)
        infolbl = QLabel(" ")
        infolbl.setWordWrap(True)
        layout.setMenuBar(tb)
        layout.addWidget(infolbl,2,1)
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        layout.addWidget(backbtn,2,0)

        usrin1 = QLineEdit()
        self.usrin1 = usrin1
        usrin1.setFont(QFont('Arial',10))
        
        prompt1 = QLabel("Select file:")
        prompt1.setFont(QFont('Arial', 10)) 
        layout.addWidget(prompt1,0,0)
        layout.addWidget(self.usrin1,0,1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
   
   
        self.usrin2 = QLineEdit()
        self.usrin2.setFont(QFont('Arial',10))
        
        prompt2 = QLabel("Output name:")
        prompt2.setFont(QFont('Arial', 10)) 
        
        layout.addWidget(prompt2,1,0)
        layout.addWidget(self.usrin2,1,1)
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
        
        
        pickFile = QPushButton("Browse")
        pickFile.setFont(QFont('Arial',10))
        fn1 = pickFile.clicked.connect(file1_find)
        layout.addWidget(pickFile, 0,2)
               
               
        Go = QPushButton("Clean!")
        Go.setFont(QFont('Arial',10))
        self.Go = Go
        Go.pressed.connect(mumcleaner)
        Go.pressed.connect(finished_Process)
        
        

        layout.addWidget(Go,2,2)
        
        self.setLayout(layout)
        self.setGeometry(850,400,450,150)   
        self.setWindowTitle("MUMCleaner")

class MUMi(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()    
        global usrin1
        global usrin2
        global usrin3
        global marg1
        global marg2
        global marg3
        global infolbl
        global pl_btn


        
        layout = QGridLayout()
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)
        pl_btn = QAction("Perl Check",self)
        tb.addAction(ex_btn)
        tb.addAction(pl_btn)
        ex_btn.triggered.connect(MUMi_ex)
        pl_btn.triggered.connect(perlCheck)
        infolbl = QLabel(" ")
        infolbl.setTextInteractionFlags(Qt.TextSelectableByMouse)
        infolbl.setFont(QFont('Arial',10))
        layout.setMenuBar(tb)
        
        layout.addWidget(infolbl,3,1)    
        
        imptext = QLabel("Will NOT work unless PERL is installed!")
        imptext.setFixedHeight(30)
        imptext.setStyleSheet("font-weight: bold;font-size: 8; color: red")

        tb.addWidget(imptext)

        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        layout.addWidget(backbtn,3,0)
        
        usrin1 = QLineEdit()
        self.usrin1 = usrin1
        usrin1.setFont(QFont('Arial',10))
        self.usrin1.setReadOnly(True)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
        
        prompt1 = QLabel("MUMs File: ")
        prompt1.setFixedWidth(90)
        prompt1.setFont(QFont('Arial', 10)) 

        pickFile1 = QPushButton("Browse")
        pickFile1.setFont(QFont('Arial',10))
        fn1 = pickFile1.clicked.connect(file1_find)
        
        usrin2 = QLineEdit()
        usrin2.setFont(QFont('Arial',10))
        self.usrin2 = usrin2
        self.usrin2.setReadOnly(True)
        
        prompt2 = QLabel("Reference: ")
        prompt2.setWordWrap(True)
        prompt2.setFont(QFont('Arial', 10))

        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        pickFile2 = QPushButton("Browse")
        pickFile2.setFont(QFont('Arial',10))
        fn2 = pickFile2.clicked.connect(file2_find)        

        
        usrin3 = QLineEdit()
        usrin3.setFont(QFont('Arial',10))
        self.usrin3 = usrin3
        self.usrin3.setReadOnly(True)
        marg3 = self.usrin3.textChanged.connect(marg3_hold)
        
        prompt3 = QLabel("Query: ")
        prompt3.setFixedWidth(90)
        prompt3.setFont(QFont('Arial', 10)) 
        marg3 = self.usrin3.textChanged.connect(marg3_hold)
        pickFile3 = QPushButton("Browse")
        pickFile3.setFont(QFont('Arial',10))
        fn3 = pickFile3.clicked.connect(file3_find)
        

        layout.addWidget(prompt1,0,0)
        layout.addWidget(self.usrin1,0,1)
        layout.addWidget(pickFile1,0,2)
        
        
        layout.addWidget(prompt2,1,0)
        layout.addWidget(self.usrin2,1,1)
        layout.addWidget(pickFile2,1,2)

        layout.addWidget(prompt3,2,0)
        layout.addWidget(self.usrin3,2,1)
        layout.addWidget(pickFile3,2,2)
        
        start = QPushButton("Go!")
        start.clicked.connect(mumi)
        start.setFont(QFont('Arial',10))
        start.clicked.connect(finished_Process)
        layout.addWidget(start,3,2)
        
        
        self.setLayout(layout)
        self.setGeometry(850,400,470,100)
        self.setWindowTitle("MUMi")

class N2M (QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        global usrin1
        global marg1
        
        #So you can pick an isolate
        layout = QGridLayout()


        usrin1 = QLineEdit()
        self.usrin1 = usrin1
        prompt1 = QLabel("Select file:")
        prompt1.setFont(QFont('Arial', 10)) 
        layout.addWidget(prompt1,0,0)
        layout.addWidget(self.usrin1,0,1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
   
   
        self.usrin2 = QLineEdit()
        prompt2 = QLabel("Output name:")
        prompt2.setFont(QFont('Arial', 10)) 
        layout.addWidget(prompt2,1,0)
        layout.addWidget(self.usrin2,1,1)
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
        
        
        pickFile = QPushButton("Browse")
        pickFile.setFont(QFont('Arial',10))
        fn1 = pickFile.clicked.connect(file1_find)
        layout.addWidget(pickFile, 0,2)
               
               
        Go = QPushButton("NUM!")
        Go.setFont(QFont('Arial',10))
        self.Go = Go
        Go.pressed.connect(n2m)
        Go.pressed.connect(finished_Process)
        
        

        layout.addWidget(Go,2,2)
        
        self.setLayout(layout)
        self.setGeometry(850,400,450,100) 
        self.setWindowTitle("Num2MUM")

class NCBICleaner(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        global usrin1
        global marg1
        
        #So you can pick an isolate
        layout = QGridLayout()
        


        usrin1 = QLineEdit()
        self.usrin1 = usrin1
        prompt1 = QLabel("Select file:")
        prompt1.setFont(QFont('Arial', 10)) 
        layout.addWidget(prompt1,0,0)
        layout.addWidget(self.usrin1,0,1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
   
   
        self.usrin2 = QLineEdit()
        prompt2 = QLabel("Output name:")
        prompt2.setFont(QFont('Arial', 10)) 
        layout.addWidget(prompt2,1,0)
        layout.addWidget(self.usrin2,1,1)
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
        
        
        pickFile = QPushButton("Browse")
        pickFile.setFont(QFont('Arial',10))
        fn1 = pickFile.clicked.connect(file1_find)
        layout.addWidget(pickFile, 0,2)
               
               
        Go = QPushButton("Clean!")
        Go.setFont(QFont('Arial',10))
        self.Go = Go
        Go.pressed.connect(NCBI_CLEANER)
        Go.pressed.connect(finished_Process)
        
        

        layout.addWidget(Go,2,2)
        
        self.setLayout(layout)
        self.setGeometry(850,400,450,100) 
        self.setWindowTitle("NCBI Cleaner")

class fastAFinder(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        global usrin1
        global usrin2
        global marg1
        global Go
        global infolbl
        
        #So you can pick an isolate
        layout = QGridLayout()
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)
        tb.addAction(ex_btn);
        ex_btn.triggered.connect(FF_ex)
        infolbl = QLabel(" ")
        infolbl.setWordWrap(True)
        layout.setMenuBar(tb)
        layout.addWidget(infolbl,3,1)
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        layout.addWidget(backbtn,3,0)



        usrin1 = QLineEdit()
        usrin1.setFont(QFont('Arial',10))
        self.usrin1 = usrin1
        prompt1 = QLabel("Select file:")
        prompt1.setFont(QFont('Arial', 10)) 
        layout.addWidget(prompt1,0,0)
        layout.addWidget(self.usrin1,0,1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
   
   
        usrin2 = QLineEdit()
        self.usrin2 = usrin2
        self.usrin2.setFont(QFont('Arial',10))
        prompt2 = QLabel("User e-mail:")
        prompt2.setFont(QFont('Arial', 10)) 
        layout.addWidget(prompt2,1,0)
        layout.addWidget(self.usrin2,1,1)
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
        self.usrin3 = QLineEdit()
        self.usrin3.setFont(QFont('Arial',10))
        prompt3 = QLabel("Output name:")
        prompt3.setFont(QFont('Arial', 10)) 
        layout.addWidget(prompt3,2,0)
        layout.addWidget(self.usrin3,2,1)
        marg3 = self.usrin3.textChanged.connect(marg3_hold)
        
        pickFile = QPushButton("Browse")
        pickFile.setFont(QFont('Arial',10))
        fn1 = pickFile.clicked.connect(file1_find)
        layout.addWidget(pickFile, 0,2)
        
        mailbtn = QPushButton("I don't want to give you my e-mail")
        mailbtn.setFont(QFont('Arial',10))
        mailbtn.clicked.connect(manualGenes)
        layout.addWidget(mailbtn, 3,1)
        
        whymailbtn = QPushButton("Why?")
        whymailbtn.setFixedWidth(90)
        whymailbtn.setFont(QFont('Arial',10))
        whymailbtn.clicked.connect(whymail)
        layout.addWidget(whymailbtn, 1,2)
               
        Go = QPushButton("Fetch!")
        Go.setFont(QFont('Arial',10))
        self.Go = Go
        Go.pressed.connect(FF)
        Go.pressed.connect(finished_Process)
        
        

        layout.addWidget(Go,3,2)
        
        self.setLayout(layout)
        self.setGeometry(850,400,450,200)
        self.setWindowTitle("GeneGetter")

class Done(QWidget): #Run anytime program finishes
    def __init__(self): 
        super().__init__()
        layout = QVBoxLayout()
        self.msg = QLabel("Process completed!")
        self.msg.setFont(QFont('Arial', 12))
        self.msg.move(125,50)
        layout.addWidget(self.msg)
        
        
        text = QLabel()
        image = QPixmap('assets\Yes.jpg')
        image = image.scaled(175,175)
        text.move(200,50)
        text.setPixmap(image)
        text.setToolTip("Alvaro's GitHub")
        layout.addWidget(text)
        
        #Maybe add a button to close when done?
        self.setLayout(layout) 
        self.setWindowTitle("Woo Hoo")
        self.setGeometry(400,400,300,100)
        
        self.show()

class ManGeneWindow(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        layout = QVBoxLayout()
        
        
        text1 = QLabel("Step 1:")
        text1.setFont(QFont('Arial', 10))
        layout.addWidget(text1)
        self.btn9 = QPushButton("N2M")
        self.btn9.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn9)
        self.btn9.clicked.connect(N2M_time)   
        
        text2 = QLabel("Step 2:")
        text2.setFont(QFont('Arial', 10))
        layout.addWidget(text2)
        self.btn10 = QPushButton("BatchEntrez")
        self.btn10.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn10)
        self.btn10.clicked.connect(BE)  
        
        text3 = QLabel("Step 3:")
        text3.setFont(QFont('Arial', 10))
        layout.addWidget(text3)
        self.btn11 = QPushButton("Cleaner")
        self.btn11.setFont(QFont('Arial', 10))
        layout.addWidget(self.btn11)
        self.btn11.clicked.connect(NCBIClean_time)           
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        layout.addWidget(backbtn)
        
        self.setLayout(layout) 
        self.setGeometry(850,400,450,200)
        self.setWindowTitle("Manual Gene Collection")
        self.show()    

class RunWindow(QWidget): #Work in progress, don'treally know how to do this yet
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        layout.addWidget(self.progress)   
        self.setLayout(layout) 
        self.setGeometry(850,400,450,200)
        self.setWindowTitle("Manual Gene Collection")
        self.show()    

class SeqStrac(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        global usrin1
        global usrin2
        global usrin3
        global usrin4
        global marg1
        global marg4
        global infolbl
        
        layout = QGridLayout()
        row2 = QHBoxLayout()
        
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)
        tb.addAction(ex_btn);
        ex_btn.triggered.connect(ss_ex)
        infolbl = QLabel(" ")
        infolbl.setWordWrap(True)
        layout.setMenuBar(tb)
        layout.addWidget(infolbl,3,1)
        
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        layout.addWidget(backbtn,3,0)



        usrin1 = QLineEdit()
        usrin1.setFont(QFont('Arial',10))
        self.usrin1 = usrin1
        self.usrin1.setText("file_chomp.txt")
        
        prompt1 = QLabel("Select file:")
        prompt1.setFont(QFont('Arial', 10)) 
        
        layout.addWidget(prompt1,0,0)
        layout.addWidget(self.usrin1,0,1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
   
        usrin2 = QLineEdit()
        self.usrin2 = usrin2
        self.usrin2.setFont(QFont('Arial',10))
        self.usrin2.setText("Start")

        row2.addWidget(self.usrin2)
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
        spacer = QLabel("-")
        spacer.setFont(QFont('Arial', 10))
        row2.addWidget(spacer)
        
        usrin3 = QLineEdit()
        self.usrin3 = usrin3
        self.usrin3.setFont(QFont('Arial',10))
        self.usrin3.setText("End")
        row2.addWidget(self.usrin3)
        
        marg3 = self.usrin3.textChanged.connect(marg3_hold)
        
        usrin4 = QLineEdit()
        self.usrin4 = usrin4
        self.usrin4.setFont(QFont('Arial',10))
        self.usrin4.setText("Num")
        self.usrin4.setFixedWidth(50)
        
        prompt4 = QLabel("Scaffold Number:")
        prompt4.setWordWrap(True)
        prompt4.setFont(QFont('Arial', 10)) 
        layout.addWidget(prompt4,2,0)
        layout.addWidget(self.usrin4,2,1)
        marg4 = self.usrin4.textChanged.connect(marg4_hold)
        
        pickFile = QPushButton("Browse")
        pickFile.setFont(QFont('Arial',10))
        fn1 = pickFile.clicked.connect(file1_find)
        layout.addWidget(pickFile, 0,2)
        

       
               
        Go = QPushButton("Extract!")
        Go.setFont(QFont('Arial',10))
        self.Go = Go
        layout.addLayout(row2,1,1)
        Go.pressed.connect(seqstracter)
        Go.pressed.connect(finished_Process)
        
        

        layout.addWidget(Go,3,2)
        
        self.setLayout(layout)
        self.setGeometry(850,400,450,200)
        self.setWindowTitle("SeqStracter")
class MSeqStrac(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        global usrin1
        global usrin2
        global marg1
        global marg2
        global infolbl
        
        layout = QGridLayout()

        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)

        tb.addAction(ex_btn);
        ex_btn.triggered.connect(mseqstraq_ex)
        infolbl = QLabel(" ")
        infolbl.setFixedSize(200, 40)
        infolbl.setWordWrap(True)
        layout.setMenuBar(tb)
        
        imptext = QLabel("More genes take more time, please be patient")
        imptext.setFixedHeight(30)
        imptext.setStyleSheet("font-size: 10")
        tb.addWidget(imptext)
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        row3.addWidget(backbtn)
        row3.addWidget(infolbl)


        usrin1 = QLineEdit()
        usrin1.setFont(QFont('Arial',10))
        self.usrin1 = usrin1
        self.usrin1.setText("file_chomp.txt")
        
        prompt1 = QLabel("Select Isolate")
        prompt1.setFont(QFont('Arial', 10)) 
        prompt1.setFixedWidth(100)
        
        row1.addWidget(prompt1)
        row1.addWidget(self.usrin1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
   
        prompt2 = QLabel(" ")
        prompt2.setWordWrap(True)
        prompt2.setFixedWidth(100)
        prompt2.setFont(QFont('Arial',10))
        row2.addWidget(prompt2)
        
        usrin2 = QLineEdit()
        self.usrin2 = usrin2
        self.usrin2.setFont(QFont('Arial',10))
        self.usrin2.setText("file.coords")
        row2.addWidget(self.usrin2)
        
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
               
        Go = QPushButton("Extract!")
        Go.setFixedWidth(80)
        Go.setFont(QFont('Arial',10))
        self.Go = Go

        Go.pressed.connect(mseqstract)
        Go.pressed.connect(finished_Process)
        
        row3.addWidget(Go)
        
        layout.addLayout(row1,0,0)
        layout.addLayout(row2,1,0)
        layout.addLayout(row3,2,0)

        
        
        self.setLayout(layout)
        self.setGeometry(850,400,475,250)
        self.setWindowTitle("MultiSeqStracter")
class MMSeqStrac(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        global usrin1
        global usrin2
        global marg1
        global marg2
        global infolbl
        
        layout = QGridLayout()

        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)

        tb.addAction(ex_btn);
        ex_btn.triggered.connect(mmseqstraq_ex)
        infolbl = QLabel(" ")
        infolbl.setFixedSize(220, 50)
        infolbl.setWordWrap(True)
        layout.setMenuBar(tb)
        
        imptext = QLabel("More genes take more time, please be patient")
        imptext.setFixedHeight(30)
        imptext.setStyleSheet("font-size: 10")
        tb.addWidget(imptext)
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        row3.addWidget(backbtn)
        row3.addWidget(infolbl)


        usrin1 = QLineEdit()
        usrin1.setFont(QFont('Arial',10))
        self.usrin1 = usrin1
        self.usrin1.setText("Iso_List.txt")
        
        prompt1 = QLabel("Select Isolate File")
        prompt1.setFont(QFont('Arial', 10)) 
        prompt1.setFixedWidth(100)
        
        row1.addWidget(prompt1)
        row1.addWidget(self.usrin1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
        
        pickFile1 = QPushButton("Browse")
        pickFile1.setFont(QFont('Arial',10))
        fn1 = pickFile1.clicked.connect(file1_find)
        row1.addWidget(pickFile1)
   
        prompt2 = QLabel("Enter file modifier")
        prompt2.setWordWrap(True)
        prompt2.setFixedWidth(100)
        prompt2.setFont(QFont('Arial',10))
        row2.addWidget(prompt2)
        
        usrin2 = QLineEdit()
        self.usrin2 = usrin2
        self.usrin2.setFont(QFont('Arial',10))
        self.usrin2.setText(" ")
        row2.addWidget(self.usrin2)
        
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
               
        Go = QPushButton("Extract!")
        Go.setFixedWidth(80)
        Go.setFont(QFont('Arial',10))
        self.Go = Go

        Go.pressed.connect(mmseqstract)
        Go.pressed.connect(finished_Process)
        
        row3.addWidget(Go)
        
        layout.addLayout(row1,0,0)
        layout.addLayout(row2,1,0)
        layout.addLayout(row3,2,0)

        
        
        self.setLayout(layout)
        self.setGeometry(850,400,475,250)
        self.setWindowTitle("MultiSeqStracter")
class GeneStrac(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        global usrin1
        global usrin2
        global marg1
        global marg2
        global infolbl
        
        layout = QGridLayout()

        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)

        tb.addAction(ex_btn);
        ex_btn.triggered.connect(genestract_ex)
        infolbl = QLabel(" ")
        infolbl.setFixedSize(220, 50)
        infolbl.setWordWrap(True)
        layout.setMenuBar(tb)
        
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        row3.addWidget(backbtn)
        row3.addWidget(infolbl)


        usrin1 = QLineEdit()
        usrin1.setFont(QFont('Arial',10))
        self.usrin1 = usrin1
        self.usrin1.setText("Iso_chomp.txt")
        
        prompt1 = QLabel("Select File")
        prompt1.setFont(QFont('Arial', 10)) 
        prompt1.setFixedWidth(100)
        
        row1.addWidget(prompt1)
        row1.addWidget(self.usrin1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
        
        pickFile1 = QPushButton("Browse")
        pickFile1.setFont(QFont('Arial',10))
        fn1 = pickFile1.clicked.connect(file1_find)
        row1.addWidget(pickFile1)
   
        prompt2 = QLabel("Enter gene")
        prompt2.setWordWrap(True)
        prompt2.setFixedWidth(100)
        prompt2.setFont(QFont('Arial',10))
        row2.addWidget(prompt2)
        
        usrin2 = QLineEdit()
        self.usrin2 = usrin2
        self.usrin2.setFont(QFont('Arial',10))
        self.usrin2.setText(" ")
        row2.addWidget(self.usrin2)
        
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
               
        Go = QPushButton("Extract!")
        Go.setFixedWidth(80)
        Go.setFont(QFont('Arial',10))
        self.Go = Go

        Go.pressed.connect(genestracter)
        Go.pressed.connect(finished_Process)
        
        row3.addWidget(Go)
        
        layout.addLayout(row1,0,0)
        layout.addLayout(row2,1,0)
        layout.addLayout(row3,2,0)

        
        
        self.setLayout(layout)
        self.setGeometry(850,400,475,250)
        self.setWindowTitle("Genestracter")
class MGeneStrac(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        global usrin1
        global usrin2
        global usrin3
        global marg1
        global marg2
        global marg3
        global infolbl
        
        layout = QGridLayout()

        row1 = QHBoxLayout()
        row2 = QGridLayout()
        row3 = QGridLayout()
        row4 = QHBoxLayout()
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)

        tb.addAction(ex_btn);
        ex_btn.triggered.connect(mgenestract_ex)
        infolbl = QLabel(" ")
        infolbl.setFixedSize(220, 50)
        infolbl.setWordWrap(True)
        layout.setMenuBar(tb)
        
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        row4.addWidget(backbtn)
        row4.addWidget(infolbl)

        filler = QLabel(" ")
        filler.setFixedWidth(220)
        
        usrin1 = QLineEdit()
        usrin1.setFont(QFont('Arial',10))
        self.usrin1 = usrin1
        self.usrin1.setText("Gene_File.txt")
        
        prompt1 = QLabel("Select Gene File")
        prompt1.setWordWrap(True)
        prompt1.setFont(QFont('Arial', 10)) 
        prompt1.setFixedWidth(100)
        
        row1.addWidget(prompt1)
        row1.addWidget(self.usrin1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
        
        pickFile1 = QPushButton("Browse")
        pickFile1.setFont(QFont('Arial',10))
        fn1 = pickFile1.clicked.connect(file1_find)
        row1.addWidget(pickFile1)
   
        prompt2 = QLabel("Select Isolate:")
        prompt2.setWordWrap(True)
        prompt2.setFixedWidth(100)
        prompt2.setFont(QFont('Arial',10))
        row2.addWidget(prompt2,0,0)
        
        usrin2 = QLineEdit()
        self.usrin2 = usrin2
        self.usrin2.setFixedWidth(100)
        self.usrin2.setFont(QFont('Arial',10))
        self.usrin2.setText(" ")
        row2.addWidget(self.usrin2,0,1)
        row2.addWidget(filler,0,2)
        
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
        prompt3 = QLabel("File Modifier:")
        prompt3.setWordWrap(True)
        prompt3.setFixedWidth(100)
        prompt3.setFont(QFont('Arial',10))
        row3.addWidget(prompt3,0,0)
        row3.addWidget(filler,0,2)
        
        usrin3 = QLineEdit()
        self.usrin3 = usrin3
        self.usrin3.setFixedWidth(100)
        self.usrin3.setFont(QFont('Arial',10))
        self.usrin3.setText(" ")
        row3.addWidget(self.usrin3,0,1)
        
        marg3 = self.usrin3.textChanged.connect(marg3_hold)
        
               
        Go = QPushButton("Extract!")
        Go.setFixedWidth(80)
        Go.setFont(QFont('Arial',10))
        self.Go = Go

        Go.pressed.connect(mgenestracter)
        Go.pressed.connect(finished_Process)
        
        row4.addWidget(Go)
        
        layout.addLayout(row1,0,0)
        layout.addLayout(row2,1,0)
        layout.addLayout(row3,2,0)
        layout.addLayout(row4,3,0)

        
        
        self.setLayout(layout)
        self.setGeometry(850,400,475,250)
        self.setWindowTitle("MultiGenestracter")
class MMGeneStrac(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        global usrin1
        global usrin2
        global usrin3
        global marg1
        global marg2
        global marg3
        global infolbl
        
        layout = QGridLayout()

        row1 = QHBoxLayout()
        row2 = QGridLayout()
        row3 = QGridLayout()
        row4 = QHBoxLayout()
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)

        tb.addAction(ex_btn);
        ex_btn.triggered.connect(mmgenestract_ex)
        infolbl = QLabel(" ")
        infolbl.setFixedSize(220, 50)
        infolbl.setWordWrap(True)
        layout.setMenuBar(tb)
        
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        row4.addWidget(backbtn)
        row4.addWidget(infolbl)

        filler = QLabel(" ")
        filler.setFixedWidth(250)
        
        usrin1 = QLineEdit()
        usrin1.setFont(QFont('Arial',10))
        self.usrin1 = usrin1
        self.usrin1.setText("Isolate_File.txt")
        
        prompt1 = QLabel("Select Gene File")
        prompt1.setWordWrap(True)
        prompt1.setFont(QFont('Arial', 10)) 
        prompt1.setFixedWidth(100)
        
        row1.addWidget(prompt1)
        row1.addWidget(self.usrin1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)
        
        pickFile1 = QPushButton("Browse")
        pickFile1.setFont(QFont('Arial',10))
        fn1 = pickFile1.clicked.connect(file1_find)
        row1.addWidget(pickFile1)
   
        prompt2 = QLabel("Select Gene File:")
        prompt2.setWordWrap(True)
        prompt2.setFixedWidth(100)
        prompt2.setFont(QFont('Arial',10))
        row2.addWidget(prompt2,0,0)
        
        usrin2 = QLineEdit()
        self.usrin2 = usrin2
        self.usrin2.setFont(QFont('Arial',10))
        self.usrin2.setText("Gene_List.txt")
        row2.addWidget(self.usrin2,0,1)
        #row2.addWidget(filler,0,2)
        
        pickFile2 = QPushButton("Browse")
        pickFile2.setFont(QFont('Arial',10))
        fn2 = pickFile2.clicked.connect(file2_find)
        row2.addWidget(pickFile2,0,2)
        marg2 = self.usrin2.textChanged.connect(marg2_hold)
        
        prompt3 = QLabel("File Modifier:")
        prompt3.setWordWrap(True)
        prompt3.setFixedWidth(100)
        prompt3.setFont(QFont('Arial',10))
        row3.addWidget(prompt3,0,0)
        row3.addWidget(filler,0,2)
        
        usrin3 = QLineEdit()
        self.usrin3 = usrin3
        self.usrin3.setFixedWidth(100)
        self.usrin3.setFont(QFont('Arial',10))
        self.usrin3.setText(" ")
        row3.addWidget(self.usrin3,0,1)
        
        marg3 = self.usrin3.textChanged.connect(marg3_hold)
        
               
        Go = QPushButton("Extract!")
        Go.setFixedWidth(80)
        Go.setFont(QFont('Arial',10))
        self.Go = Go

        Go.pressed.connect(mmgenestracter)
        Go.pressed.connect(finished_Process)
        
        row4.addWidget(Go)
        
        layout.addLayout(row1,0,0)
        layout.addLayout(row2,1,0)
        layout.addLayout(row3,2,0)
        layout.addLayout(row4,3,0)

        
        
        self.setLayout(layout)
        self.setGeometry(850,400,475,250)
        self.setWindowTitle("MegaMultiGenestracter")

class RandoGene(QWidget):
    def __init__(self): #Make font bigger as I add subfunctions
        super().__init__()
        global usrin1
        global usrin2
        global marg1
        global marg2
        global infolbl
        
        layout = QGridLayout()
        row1 = QHBoxLayout()
        row2 = QGridLayout()
        row3 = QGridLayout()
        
        
        tb = QToolBar();
        ex_btn = QAction("Example",self)

        tb.addAction(ex_btn);
        ex_btn.triggered.connect(randogene_ex)
        infolbl = QLabel(" ")
        infolbl.setFixedSize(220, 50)
        infolbl.setWordWrap(True)
        layout.setMenuBar(tb)
        
        
        backbtn = QPushButton("Back")
        backbtn.setFixedWidth(80)
        backbtn.setFont(QFont('Arial',10))
        backbtn.clicked.connect(back)
        row3.addWidget(backbtn,0,0)
        row3.addWidget(infolbl,0,1)

        
        usrin1 = QLineEdit()
        usrin1.setFont(QFont('Arial',10))
        self.usrin1 = usrin1
        self.usrin1.setText("Gene_List.txt")
        
        prompt1 = QLabel("Select Gene File")
        prompt1.setWordWrap(True)
        prompt1.setFont(QFont('Arial', 10)) 
        prompt1.setFixedWidth(100)
        
        row1.addWidget(prompt1)
        row1.addWidget(self.usrin1)
        marg1 = self.usrin1.textChanged.connect(marg1_hold)  
        
        pickFile1 = QPushButton("Browse")
        pickFile1.setFont(QFont('Arial',10))
        fn1 = pickFile1.clicked.connect(file1_find)
        row1.addWidget(pickFile1)

        prompt2 = QLabel("Number of genes to pull:")
        prompt2.setWordWrap(True)
        prompt2.setFixedWidth(100)
        prompt2.setFont(QFont('Arial',10))
        row2.addWidget(prompt2,0,0)
        
        usrin2 = QLineEdit()
        self.usrin2 = usrin2
        self.usrin2.setFont(QFont('Arial',10))
        self.usrin2.setText("Number")
        row2.addWidget(self.usrin2,0,1)
        
        
        Go = QPushButton("Extract!")
        Go.setFixedWidth(80)
        Go.setFont(QFont('Arial',10))
        self.Go = Go

        Go.pressed.connect(randogene)
        Go.pressed.connect(finished_Process)
        
        row3.addWidget(Go,0,2)
        
        layout.addLayout(row1,0,0)
        layout.addLayout(row2,1,0)
        layout.addLayout(row3,2,0)
        
        self.setLayout(layout)
        self.setGeometry(850,400,475,250)
        self.setWindowTitle("MegaMultiGenestracter")
#Program window transitions and passing code to scripts
def back(self):
    w1.hide()
    w.show()
def selfhide(self):
    w.hide() #This feels like cheating but it works
def perlCheck(self):
    a = os.system("perl -v")
    if a == 0:
        pl_btn.setText("PERL Found")
    else:
        pl_btn.setText("PERL NOT FOUND")
 
def whymail(self):
    webbrowser.open("https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch")

def chomp_ex(self):
    usrin1.setText(r"examples\DNA.txt")
    usrin2.setText("DNA")
    infolbl.setText("Output is: DNA_chomp.txt")  
def chomp_time(self):
    global w1
    w.hide()
    w1 = Chomp()
    w1.show()  
def chomp():
    try:
        arg1 = temp1
        arg2 = temp2
    except NameError: #Cathes to see if it's empty
        arg1 = "none"
        arg2 = "none"
        
    program = QProcess()
    arguments = list()
    arguments.append('scripts\Chomp.py')
    arguments.append(arg1)
    arguments.append(arg2)
    args = " ".join(arguments)
    if os.path.isfile(arg1) == True and arg2 != "none" and arg2 != "":#See if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('ChompError.txt').read()
      #  print(errMess)
        error_hold()
        Error()


def flip_ex(self):
    usrin1.setText(r"examples\seq.txt")
    infolbl.setText("Output is: RevCom.txt")   
def flip_time(self):
    global w1
    w.hide()
    w1 = Flipper()
    w1.show()  
def flip():
    arguments = list()
  
    try:
        arg1 = temp1
    except NameError:
        arg1 = "none"
        
        
    arguments.append('scripts\Flipper.py')
    arguments.append(arg1)
    args = " ".join(arguments)

    if os.path.isfile(temp1) == True: #Checks to see if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('FlipError.txt').read()
        print(errMess)
        error_hold()
        Error()

def bunk_ex(self):
    usrin1.setText("examples\BedIn_Ex.txt")
    infolbl.setText("Output is: TuckedIn.txt")      
def bunk_time(self):
    global w1
    w.hide()
    w1 = BunkBed()
    w1.show()  
def bunk():
    arguments = list()
    
    #Are the boxes checked
    check1 = opt1.checkState()
    check2 = opt2.checkState()

    #Do something if yes
    if check1 > 1 :
        temp2 = "-g"
    else:
        temp2 = "none"
    if check2 > 1:
        temp3 = "-c"
    else:
        temp3 = "none"
        
    #Combine everything  
    arguments.append('scripts\BunkBed.py')
    arguments.append(temp1)  
    arguments.append(temp2)
    arguments.append(temp3)
    args = " ".join(arguments)
    if os.path.isfile(temp1) == True: #Checks to see if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('BedError.txt').read()
        print(errMess)
        error_hold()
        Error()

def zeld_ex(self):
    usrin1.setText(r"examples\Iso_ListEx.txt")
    infolbl.setText("Outputs will be: Iso1_pulled.txt, Iso2_pulled.txt, Iso3_pulled.txt")  
def zelda_time(self):
    global w1
    w.hide()
    w1 = Zelda()
    w1.show()  
def zelda():
    arguments = list()
    
    try:
        arg1 = temp1
        arg2 = temp2
    except NameError:
        arg2 = "none"
        
    arguments.append('scripts\Zelda.py')
    arguments.append(arg1)
    arguments.append(arg2)
    args = " ".join(arguments)

    if os.path.isfile(arg1) == True: #Checks to see if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('ZeldError.txt').read()
        print(errMess)
        error_hold()
        Error()

def link_ex(self):
    usrin1.setText(r"examples\Iso_ListEx.txt")
    infolbl.setText("Output will be IsoConcat.fasta")  
def link_time(self):
    global w1
    w.hide()   
    w1 = Link()
    w1.show()  
def link():
    arguments = list()
    
    try:
        temp1 = arg1
        temp2 = arg2
    except NameError:
        temp1 = "none"
        temp2 = "none"
    
    arguments.append('scripts\Link.py')
    arguments.append(temp1)
    arguments.append(temp2)
    args = " ".join(arguments)

    if os.path.isfile(temp1) == True: #Checks to see if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('LinkError.txt').read()
        print(errMess)
        error_hold()
        Error()

def jam_ex(self):
    usrin1.setText(r"examples\CleanMums.mums")
    if opt1.isChecked():
        of = "OutMUMs.bed"
    elif opt2.isChecked():
        of = "MUMMap.txt"
    elif opt3.isChecked():
        of = ('MUMLinks.txt')
    infolbl.setText("Output will be " + of)  
    ref.setCurrentIndex(1)
def jam_time(self):
    global w1    
    w.hide()
    w1 = JAMS()
    w1.show()  
def jams(self):
    global errMess
    arguments = list()
    path = "scripts" + "\\" + "autoJAMS.py"   
    arguments.append(path)


    try:
        arg1 = temp1
        arguments.append(arg1)
        if text != "Other":
            arg2 = "Chrom_Refs" + "\\" + text + ".txt"
        else:
            arg3 = fn2
            
        arguments.append(arg2)
        arg3 = opt
        arguments.append(arg3)
    except NameError or UnboundLocalError:
        arg1 = "none"
        noVar = "Missing at least one argument"
        errMess = noVar
        Error()


    
    args = " ".join(arguments)

    if os.path.isfile(arg1) == True: #Checks to see if the file exists
        os.system(args)
    else:
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('JamError.txt').read()
        error_hold()
        Error()

def mumclean_ex(self):
    usrin1.setText(r"examples\DirtyMums.mums")
    infolbl.setText("Output will be CleanMUMs.mums")  
def mumclean_time(self):
    global w1    
    w.hide()
    w1 = MUMCleaner()
    w1.show()  
def mumcleaner():
    arguments = list()
    arguments.append('scripts\MUMCleaner.py')
    try:
        arg1 = temp1
        arg2 = temp2
    except NameError:
        arg1 = temp1
        arg2 = "none"
        
        

    arguments.append(arg1)
    arguments.append(arg2)
    
    args = " ".join(arguments)
    if os.path.isfile(arg1) == True:#See if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('CleanError.txt').read()
        error_hold()
        Error()

def  MUMi_ex(self):# Find way to get this working with some sample sequcnes
    usrin1.setText("examples\Ex.mums")
    usrin2.setText("examples\CBS138_Full.txt")
    usrin3.setText("examples\BG2_Full.txt")
def mumi_time(self):
    global w1
    w.hide()
    w1 = MUMi()
    w1.show()  
def mumi():
    
    arguments = list()
    arguments.append('scripts\MUMi.pl')
    try:
        arg1 = temp1
        arg2 = temp2
        arg3 = temp3
    except IndexError:
        arg1 = "none"
        arg2 = "none"
        arg3 = "none"
        

    arguments.append(arg1)
    arguments.append(arg2)
    arguments.append(arg3)
    
    args = " ".join(arguments)
    print(args)
    if os.path.isfile(arg1) == True and os.path.isfile(arg2) == True and os.path.isfile(arg3) == True:#See if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = "Can't find file. Check if any arguments are missing."
        error_hold()
        Error()
    
    a = open('MUMi_out.txt').read()
    infolbl.setText("MUMi = "+ a)

def N2M_time(self):
    global w1
    w1 = N2M()
    w1.show()  
def n2m():
    arguments = list()
    path = r"scripts\N2M.py"
    arguments.append(path)
    try:
        arg1 = temp1
        arg2 = temp2
    except NameError:
        arg1 = temp1
        arg2 = "none"
        
    arguments.append(arg1)
    arguments.append(arg2)
    
    args = " ".join(arguments)
    if os.path.isfile(arg1) == True:#See if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('NumError.txt').read()
        error_hold()
        Error()

def NCBIClean_time(self):
    global w1
    w1 = NCBICleaner()
    w1.show()  
def NCBI_CLEANER():
    global w1
    w1 = N2M()
    w1.show()  
    arguments = list()
    path = r"scripts\NCBICleaner.py"
    arguments.append(path)
    try:
        arg1 = temp1
        arg2 = temp2
    except NameError:
        arg1 = temp1
        arg2 = "none"
        
    arguments.append(arg1)
    arguments.append(arg2)
    
    args = " ".join(arguments)
    if os.path.isfile(arg1) == True:#See if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('NCBICleanError.txt').read()
        error_hold()
        Error()


def FF_ex(self):
    usrin1.setText(r"examples\Gene_List.txt")
    usrin2.setText(r"RealEmail@Email.com")
    infolbl.setText("Output will be a value")  
def fastA_time(self):
    global w1
    w.hide()
    w1 = fastAFinder()
    w1.show()  
def FF():
    arguments = list()
    try:
        arg1 = temp1
        arg2 = temp2
        arg3 = temp3
    except NameError:
        arg1 = temp1
        arg2 = temp2
        arg3 = "none"   

    
    arguments.append('scripts\FastAFetcher.py')
    arguments.append(arg1)
    arguments.append(arg2)
    arguments.append(arg3)
    args = " ".join(arguments)

    if os.path.isfile(temp1) == True: #Checks to see if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('AUTONCBIError.txt').read()
        print(errMess)
        error_hold()
        Error()
    
def ss_ex(self):
    usrin1.setText(r"examples\CBS138_Full.txt")
    usrin2.setText("10")
    usrin3.setText("30")
    usrin4.setText("1")
    infolbl.setText("Output will be XTRCT.txt")  
def seqstract_time(self):
    global w1
    w.hide()
    w1 = SeqStrac()
    w1.show()  
def seqstracter():
    arguments = list()
    path = r"scripts\SeqStracter.py"
    arguments.append(path)
    try:
        arg1 = temp1
        arg2 = temp4
        arg3 = temp2
        arg4 = temp3
    except IndexError:
        arg1 = "none"
        arg2 = "none"
        arg3 = "none"
        arg4 = "none"
        
    arguments.append(arg1)
    arguments.append(arg2)
    arguments.append(arg3)
    arguments.append(arg4)

    args = " ".join(arguments)
    print(args)
    if os.path.isfile(arg1) == True:#See if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('SeqError.txt').read()
        error_hold()
        Error()

def mseqstraq_ex(self):
    usrin1.setText("examples\CBS138")
    usrin2.setText("_Example")
    infolbl.setText("Output will be in examples folder as CBS138_Example_genes.txt")
def mseqstract_time(self):
    global w1
    w.hide()
    w1 = MSeqStrac()
    w1.show()  
def mseqstract():

    arguments = list()
    path = r"scripts\MultiSeqStracter.py"
    arguments.append(path)
    try:
        arg1 = temp1
        arg2 = temp2
    except IndexError:
        arg2 = "none"

        
    arguments.append(arg1)
    arguments.append(arg2)
    args = " ".join(arguments)
    if arg1 != "none":#See if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('MSeqError.txt').read()
        error_hold()
        Error()

def mmseqstraq_ex(self):
    usrin1.setText("examples\Iso_List.txt")
    usrin2.setText("_Example")
    infolbl.setText("Output will be in examples folder with the Example_genes.txt appended to each isolate")
def mmseqstract_time(self):
    global w1
    w.hide()
    w1 = MMSeqStrac()
    w1.show()  
def mmseqstract():
    arguments = list()
    path = r"scripts\MegaMultiSeqStracter.py"
    arguments.append(path)
    try:
        arg1 = temp1
        arg2 = temp2
    except IndexError:
        arg2 = "none"

        
    arguments.append(arg1)
    arguments.append(arg2)
    args = " ".join(arguments)
    if arg1 != "none":#See if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('MMSeqError.txt').read()
        error_hold()
        Error()


def genestract_ex(self):
    usrin1.setText("examples\CBS138_Example_genes.txt")
    usrin2.setText("CAGL0L03520g")
    infolbl.setText("Output will be CAGL0L03520g.txt")    
def genestract_time(self):
    global w1
    w.hide()
    w1 = GeneStrac()
    w1.show()
def genestracter():
    arguments = list()
    path = r"scripts\Genestracter.py"
    arguments.append(path)
    try:
        arg1 = temp1
        arg2 = temp2
    except IndexError:
        arg1 = "none"
        arg2 = "none"

        
    arguments.append(arg1)
    arguments.append(arg2)
    args = " ".join(arguments)
    if arg1 != "none":#See if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('GSError.txt').read()
        error_hold()
        Error()

def mgenestract_ex(self):
    usrin1.setText("examples\Small_Gene_List.txt")
    usrin2.setText("examples\CBS138")
    usrin3.setText("_Example")
    infolbl.setText("Output will be CBS138_Example_pulled.txt")       
def mgenestract_time(self):
    global w1
    w.hide()
    w1 = MGeneStrac()
    w1.show()
def mgenestracter():
    arguments = list()
    path = r"scripts\MultiGeneStracter.py"
    arguments.append(path)
    try:
        arg1 = temp1
        arg2 = temp2
        arg3 = temp3
    except IndexError:
        arg1 = temp1
        arg2 = temp2
        arg3 = "none"

        
    arguments.append(arg1)
    arguments.append(arg2)
    arguments.append(arg3)
    args = " ".join(arguments)
    if arg1 != "none":#See if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('MGSError.txt').read()
        error_hold()
        Error()

def mmgenestract_ex(self):
    usrin1.setText("examples\Iso_List.txt")
    usrin2.setText("examples\Small_Gene_List.txt")
    usrin3.setText("_Example")
    infolbl.setText("Output will be CBS138_Example_pulled.txt and BG2_Example_pulled.txt")     
def mmgenestract_time(self):
    global w1
    w.hide()
    w1 = MMGeneStrac()
    w1.show()
def mmgenestracter():
    arguments = list()
    path = r"scripts\MegaMultiGeneStracter.py"
    arguments.append(path)
    try:
        arg1 = temp1
        arg2 = temp2
        arg3 = temp3
    except IndexError:
        arg1 = temp1
        arg2 = temp2
        arg3 = "none"

        
    arguments.append(arg1)
    arguments.append(arg2)
    arguments.append(arg3)
    args = " ".join(arguments)
    if arg1 != "none":#See if the file exists
        os.system(args)
    else:
        global errMess
        os.system(args)
        errMess = QPlainTextEdit()
        errMess=open('MMGSError.txt').read()
        error_hold()
        Error()

def randogene_ex(self):
    usrin1.setText("examples\Gene_List.txt")
    usrin2.setText("45")
    infolbl.setText("Output will be RandPick.txt")
def randogene_time(self):
    global w1
    w.hide()
    w1 = RandoGene()
    w1.show()
def randogene():
    print()
def manualGenes(self):
    global w1
    w1 = ManGeneWindow()
    w1.show()  
    
def test(self): #gets the info from wheel thing
    global text
    text = self
    return text
    
#Jams options
def BedTools (self):
    global opt
    if opt1.isChecked():
        opt = "-b"
def PhenoGram(self):
    global opt
    if opt2.isChecked():
        opt = "-p"
def Circos(self):
    global opt
    if opt3.isChecked():
        opt = "-c"
        
def BE(self):
    webbrowser.open('https://www.ncbi.nlm.nih.gov/sites/batchentrez')
#M for manual hold    
def marg1_hold(marg1): #Temporarily stores 1st argument
    global temp1
    temp1 = "none"
    temp1 = marg1
def marg2_hold(marg2): #Temporarily stores 2nd argument
    global temp2
    temp2 = "None"
    temp2 = marg2
def marg3_hold(marg3): #Temporarily stores 3rd argument
    global temp3
    temp3 = "none"
    temp3 = marg3
def marg4_hold(marg4): #Temporarily stores 4th argument
    global temp4
    temp4 = marg4
    
def error_hold():
    global error
    error = True    
def finished_Process():
    global d
    global error
    if error == False:
        d = Done()
        d.show()
    error = False #resets back to false so it can recheck later

#File locaters
def file1_find(self):
    global fn1
    path = "\\"
    filepath1 = QFileDialog.getOpenFileName()
    filelist1 = list(filepath1)
    filelist1.pop(1)
    files1 = str(filelist1)
    if files1 != "['']":
        filename1 = files1.split("/")[-1]
        folder = (files1.split("/")[-2])
        fn1 = (str(filename1[:-2]))
    
        if folder == "PythonUI":
            Fn1 = fn1
        else:
            Fn1 = (folder + path + fn1)#Also gets the path
        usrin1.setText(Fn1)
def file2_find(self):
    global fn2
    path = "\\"
    filepath2 = QFileDialog.getOpenFileName()
    filelist2 = list(filepath2)
    filelist2.pop(1)
    files2 = str(filelist2)
    if files2 != "['']":
        filename2 = files2.split("/")[-1]
        fn2 = (str(filename2[:-2]))
        folder = (files2.split("/")[-2])
    
        if folder == "PythonUI":
            Fn2 = fn2
        else:
            Fn2 = (folder + path + fn2)#Also gets the path

        usrin2.setText(Fn2)
def file3_find(self):
    global fn3
    path = "\\"
    filepath3 = QFileDialog.getOpenFileName()
    filelist3 = list(filepath3)
    filelist3.pop(1)
    files3 = str(filelist3)
    if files3 != "['']":
        filename3 = files3.split("/")[-1]
        fn3 = (str(filename3[:-2]))
        folder = (files3.split("/")[-2])
    
        if folder == "PythonUI":
            Fn3 = fn3
        else:
            Fn3 = (folder + path + fn3)#Also gets the path

        usrin3.setText(Fn3)
    
def show_help(self):
    os.startfile(r'README\AOT_README.txt') 
def show_use(self):
    os.startfile(r'README\USES_README.txt')



#Main Window Transitions
def working(self): #Work in progress
    global w2
    w2 = Working()
    w2.show()
def manip_options(self):
    global w
    w = ManipWindow()
    w.show()
 
def ext_options(self):
    global w
    w = ExtracWindow()
    w.show()
    
def help_options(self):
    global w
    w = HelpWindow()
    w.show()

#Resets error after error code reiggered  
def error_reset():
    global error
    if error == True:
        error = False

#Holder until i can get thing working
def button_clicked(self):
   global w1
   w1 = NotYet()
   w1.show()   

#Cheeky little promos
def openGitHub(self):
    webbrowser.open('https://github.com/Alvarortor')

def openLab(self):
    webbrowser.open('https://www.theromolab.com/')

if __name__ == '__main__':
   global m
   m = MainWindow()
   m.show()
app.exec()