from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import sys
import time

class ThreadingHelper(QThread):
    finished = pyqtSignal() 
    
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
    
    def run(self):
        # Calling function
        self.func(*self.args, **self.kwargs)
        self.finished.emit()  # Emitting signal when function is done