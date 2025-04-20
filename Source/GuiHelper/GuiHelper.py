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
        self.runButton = QPushButton('Run')
        self.stopButton = QPushButton('Stop')
        self.exitButton = QPushButton('Exit')
    
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