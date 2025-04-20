from .ThreadingHelper import ThreadingHelper

import os
import sys
from pathlib import Path
import time

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

from PyQt6.QtCore import (
    QThread,
    pyqtSignal
)

class GuiHelper():
    def __init__(self):
        # Initializing Buttons
        self.animeText    = QLabel("Anime Name")
        self.typeText     = QLabel("Type")
        self.songText     = QLabel("Song Name")
        self.artistText   = QLabel("Artist Name")
        self.composerText = QLabel("Composer Name")
        self.arrangerText = QLabel("Arranger Name")
        self.runButton    = QPushButton('Run')
        self.stopButton   = QPushButton('Stop')
        self.exitButton   = QPushButton('Exit')
        
        # song text
        self.animeName    = ""
        self.typeName     = ""
        self.songName     = ""
        self.artistName   = ""
        self.composerName = ""
        self.arrangerName = ""
        
    # Pass in function to run and endFunction
    def StartThread(self, func, endFunc = None):
        self.thread = ThreadingHelper(func)
        self.thread.finished.connect(lambda: print(str(func), "Thread Finished"))
        
        if endFunc != None:
            self.thread.finished.connect(endFunc)
            
        self.thread.start()
    
    def DisableButtons(self):
        self.runButton.setDisabled(True)
        
    def EnableButtons(self):
        self.runButton.setDisabled(False)
        
    
    def SetSongInformation(self, songArray):
        self.animeName    = songArray[0]
        self.typeName     = songArray[1]
        self.songName     = songArray[2]
        self.artistName   = songArray[3]
        self.composerName = songArray[4]
        self.arrangerName = songArray[5]