from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,600)
#         button1 = QPushButton("button 1")
#         button2 = QPushButton("button 2")
#         button3 = QPushButton("button 3")
#         splitter = QSplitter()
#         layout.addWidget(splitter)
#         splitter.addWidget(button1)
#         splitter.addWidget(button2)
#         splitter.addWidget(button3)
#         splitter.setOrientation(Qt.Vertical)
#         splitter.setHandleWidth(50)
#         s = splitter.count()
#         print(s)
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())
        
#___________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global frame
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(1000,1000)
#         button = QPushButton("Click me")
#         layout.addWidget(button)
#         button.clicked.connect(self.buttonclick)
#         frame = QFrame()
#         layout.addWidget(frame)
#         frame.setLineWidth(50)
#         frame.setFrameShape(QFrame.WinPanel)
#         frame.setStyleSheet("background-color:pink;")
        
#     def buttonclick(self):
#         frame.setStyleSheet("background-image: url(C:/Users/MZZ/Desktop/IMG_1402.jpg);")
        
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#_________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global label,slider1
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,600)
#         slider1 = QSlider(Qt.Horizontal)
#         slider1.setValue(4)
#         layout.addWidget(slider1,0,0)
#         slider2 = QSlider(Qt.Vertical)
#         slider2.setValue(4)
#         slider2.setTickPosition(QSlider.TicksBothSides)
#         layout.addWidget(slider2,0,1)
#         label = QLabel("label")
#         layout.addWidget(label)
#         button = QPushButton("slider1 value")
#         layout.addWidget(button)
#         button.clicked.connect(self.buttonclick)

#     def buttonclick(self):
#         label.setText(str(slider1.value()))

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#__________________________________

# class Window(QWidget):
        
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,600)
#         scrollbar = QScrollBar(Qt.Vertical)
#         layout.addWidget(scrollbar)
#         scrollarea = QScrollArea()
#         layout.addWidget(scrollarea)
#         scrollarea.setAlignment(Qt.AlignTop)
#         label = QLabel("ierughnoruwogwnvhergisjuhroghwonrgoh8wruthgow8rnhtog8wngilwhrngjshjnflkjuhfgosuehrgnhrhrgsun")
#         scrollarea.setWidget(label)
    

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#______________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global spinbox
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         spinbox = QSpinBox()
#         layout.addWidget(spinbox)
#         spinbox.setRange(0,100)
#         spinbox.setPrefix("value : ")
#         spinbox.setSuffix(" cm")
#         spinbox.setSingleStep(2)
#         spinbox.valueChanged.connect(self.spinchange)

#     def spinchange(self):
#         print(spinbox.value())


# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#__________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global dspinbox
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         dspinbox = QDoubleSpinBox()
#         layout.addWidget(dspinbox)
#         dspinbox.setRange(0,1)
#         dspinbox.setPrefix("value : ")
#         dspinbox.setSuffix(" cm")
#         dspinbox.setSingleStep(0.01)
#         dspinbox.valueChanged.connect(self.dspinchange)
    
#     def dspinchange(self):
#         print(dspinbox.value())

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global dial,label
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,600)
#         dial = QDial()
#         layout.addWidget(dial)
#         dial.setMaximum(0)
#         dial.setMaximum(100)
#         dial.setValue(0)
#         dial.valueChanged.connect(self.dialchange)
#         label = QLabel("label")
#         layout.addWidget(label)
        
#     def dialchange(self):
#         print(dial.value())
#         if dial.value() == 0:
#             label.setText("minimum")
#         elif dial.value() == 100:
#             label.setText("maximum")
#         else:
#             label.setText("mid")


# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,600)
#         lcdnumber = QLCDNumber()
#         layout.addWidget(lcdnumber)
#         lcdnumber.display(15)
#         lcdnumber.setBinMode()

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#____________________________________

# count = 0
# class Window(QWidget):
    
#     def __init__(self):
#         global pd,pb,count
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(700,700)
#         spaceritem = QSpacerItem(100,100)
#         layout.addItem(spaceritem,0,1)
#         pb = QProgressBar()
#         layout.addWidget(pb,0,0)
#         pb.setMinimum(0)
#         pb.setMaximum(100)
#         pb.setValue(0)
#         pb.setOrientation(Qt.Horizontal)
#         pb.setTextVisible(True)
#         buttonadd = QPushButton("add")
#         layout.addWidget(buttonadd)
#         buttonadd.clicked.connect(self.add)
#         buttonexit = QPushButton("exit")
#         layout.addWidget(buttonexit)
#         buttonexit.clicked.connect(self.exitbutton)
#         pd = QProgressDialog()
#         layout.addWidget(pd)
#         pd.setMinimum(0)
#         pd.setMaximum(100)
#         pd.setValue(0)
        
#     def add(self):
#         global count
#         count += 1
#         pd.setValue(count)
#         pb.setValue(count)
#         if pd.wasCanceled() == True:
#             print("canceled")
    
#     def exitbutton(self):
#         exit()

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())