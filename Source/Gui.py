from .GuiHelper        import GuiHelper
#from .Database         import Database
#from .SignalProcessing import SignalProcessing

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

class Gui(QWidget, GuiHelper):
    def __init__(self, *args, **kwargs): 
        QWidget.__init__(self, *args, **kwargs)
        
        # Bools
        self.isRunning = False
        
        # Creating Window
        self.setWindowTitle("Anime Song Identifier")
        self.setGeometry(100, 100, 320, 210)
        self.layout = QGridLayout()
        
        # Mapping Buttons
        self.RunButton()
        self.StopButton()
        self.ExitButton()
        
        # Setting layout
        self.setLayout(self.layout)
        
        # Displaying Gui
        self.show()
        sys.exit(app.exec())
        
    def DisplaySongInfo(self):
        pass
    
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
            
            time.sleep(0.5)