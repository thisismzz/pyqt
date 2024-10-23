from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import sys
from time import sleep

# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self) 
#         self.resize(400,300)
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sleep(2)
# screen.setMinimumWidth(800)
# sys.exit(app.exec_())

#____________________________________

# class window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         self.resize(500,500)
#         layout = QBoxLayout(QBoxLayout.LeftToRight)
#         self.setLayout(layout)
#         lable = QLabel("lable 1")
#         layout.addWidget(lable,0,Qt.AlignCenter)
#         layout2 = QBoxLayout(QBoxLayout.TopToBottom)
#         layout.addLayout(layout2)
#         lable = QLabel("lable 2")
#         layout2.addWidget(lable)
#         lable = QLabel("lable 3")
#         layout2.addWidget(lable)
        
# app=QApplication(sys.argv)
# screen = window()
# screen.show()
# sys.exit(app.exec_())

#_______________________________________


# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,600)
#         lable1 = QLabel("lablel1 spanning 2 columns")
#         layout.addWidget(lable1,0,0,0,2)
#         lable2 = QLabel("lable2 spanning 2 rows")
#         layout.addWidget(lable2,2,0,2,2)
        
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
#         self.resize(500,500)
#         lable = QLabel("Faradars")
#         layout.addWidget(lable)
#         lable.setIndent(10)
#         lable.setMargin(50)
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#_________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,500)
#         button = QPushButton("Click me!")
#         layout.addWidget(button)
#         button.clicked.connect(self.buttonclicked)
        
#     def buttonclicked(self):
#         print("Feshar")
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#___________________________________

# class Window(QWidget):
    
#     rb1 = None
#     rb2 = None
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         Window.rb1 = QRadioButton("python")
#         layout.addWidget(Window.rb1)
#         Window.rb1.toggled.connect(self.rb1clicked)
#         Window.rb2=QRadioButton("java")
#         layout.addWidget(Window.rb2)
#         Window.rb2.toggled.connect(self.rb2clicked)
        
#     def rb1clicked(self):
#         if Window.rb1.isChecked():
#             print("python clicked")
            
#     def rb2clicked(self):
#         if Window.rb2.isChecked():
#             print("java clicked")
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#_____________________

# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         self.cb1 = QCheckBox("number 1")
#         self.cb1.setChecked(True)
#         layout.addWidget(self.cb1)
#         self.cb1.toggled.connect(self.checkbox)
#         self.cb2 = QCheckBox("number 2")
#         layout.addWidget(self.cb2)
#         self.cb2.toggled.connect(self.checkbox)
#         self.cb2.setTristate(True)
        
#     def checkbox(self):
#         if self.cb1.isChecked():
#             print("Checked box one")
#         if self.cb2.isChecked():
#             print("Checked box two")
        
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#_______________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         button1 = QPushButton("button 1")
#         button2 = QPushButton("button 2")
#         button3 = QPushButton("button 3")
#         button1.setToolTip("tooltip button 1")
#         button2.setToolTip("tooltip button 2")
#         button3.setWhatsThis("whatsthis button 3")
#         layout.addWidget(button1,0,0)
#         layout.addWidget(button2,1,0)
#         layout.addWidget(button3,2,0)
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#___________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global buttongroup
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         button1 = QPushButton("button1")
#         layout.addWidget(button1)
#         button2 = QPushButton("button2")
#         layout.addWidget(button2)
#         button3 = QPushButton("button3")
#         layout.addWidget(button3)
#         buttongroup = QButtonGroup()
#         buttongroup.addButton(button1,1)
#         buttongroup.addButton(button2,2)
#         buttongroup.addButton(button3,3)
#         buttongroup.buttonClicked[int].connect(self.on_button)
        
#     def on_button(self,id):
#         print("number %s clicked" %id)
        

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#_______________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(400,400)
#         box = QGroupBox("group box")
#         layout.addWidget(box)
#         box.setCheckable(True)
#         sublayout = QGridLayout()
#         box.setLayout(sublayout)
#         button1 = QPushButton("button 1")
#         sublayout.addWidget(button1)
#         button2 = QPushButton("button 2")
#         sublayout.addWidget(button2)

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())       

#________________________________________


