from .GuiHelper        import GuiHelper
#from .Database         import Database
from .SignalProcessing import SignalProcessing

import time
import os
import sys
from pathlib import Path
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
    QListWidget,
    QGridLayout,
    QLabel,
    QProgressBar,
    QMessageBox
)

app = QApplication(sys.argv)

class Gui(QWidget, GuiHelper, SignalProcessing):
    def __init__(self, *args, **kwargs): 
        QWidget.__init__(self, *args, **kwargs)
        
        # Bools
        self.isRunning = False
        
        # Creating Window
        self.setWindowTitle("Anime Song Identifier")
        self.setGeometry(100, 100, 320, 210)
        self.layout = QGridLayout()
        
        # Adding Song Info Text
        self.SongText()
        
        # Mapping Buttons
        self.RunButton()
        self.StopButton()
        self.ExitButton()
        
        # Setting layout
        self.setLayout(self.layout)
        
        # Populating hash file
        self.PopulateHashFile()
        
        # Displaying Gui
        self.show()
        sys.exit(app.exec())
        
    # Displaying Song Information
    def DisplaySongInfo(self):
        self.animeText.setText(self.animeName)
        self.typeText.setText(self.typeName)
        self.songText.setText(self.songName)
        self.artistText.setText(self.artistName)
        self.composerText.setText(self.composerName)
        self.arrangerText.setText(self.arrangerName)
    
    # Maps Text to Gui
    def SongText(self):
        # Setting and adding text
        self.layout.addWidget(self.animeText   , 1, 1)
        self.layout.addWidget(self.typeText    , 2, 1)
        self.layout.addWidget(self.songText    , 3, 1)
        self.layout.addWidget(self.artistText  , 4, 1)
        self.layout.addWidget(self.composerText, 5, 1)
        self.layout.addWidget(self.arrangerText, 6, 1)
        
    # Maps run button to Gui
    def RunButton(self):
        # Mapping button to RunProgram() function
        self.runButton.clicked.connect(self.RunProgram)
        
        # Setting and adding button
        self.layout.addWidget(self.runButton, 10, 1)
    
    # Maps stop button to Gui
    def StopButton(self):
        # Mapping button to StopButton() function
        self.stopButton.clicked.connect(self.StopProgram)
        
        # Setting and adding button
        self.layout.addWidget(self.stopButton, 11, 1)
        
    # Maps exit button to Gui
    def ExitButton(self):
        # Mapping button to ExitProgram() function
        self.exitButton.clicked.connect(self.ExitProgram)
        
        # Setting and adding button
        self.layout.addWidget(self.exitButton, 12, 1)
    
    # Stopping Program
    def StopProgram(self):
        self.isRunning = False
    
    def ExitProgram(self):
        sys.exit()
    
    # Run Program
    def RunProgram(self):
        
        # Disabling Run Button
        self.DisableButtons()
        self.isRunning = True
        
        # Starting Progress Bar Thread
        self.StartThread(self.FindSong, self.EnableButtons)
        
    # Finding Song
    def FindSong(self):
        while(self.isRunning == True):
            print("Finding Song!")
            # Run code for Finding Song
            songArray = self.GetSongInformation()
            
            self.SetSongInformation(songArray)
            self.DisplaySongInfo()
            
            time.sleep(0.5)