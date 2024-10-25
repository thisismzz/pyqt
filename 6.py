from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Window(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)

        
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())