from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep
import sys


# class Window(QWidget):
    
#     def __init__(self):
#         global label,lineedit,lineedit2
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,500)
#         lineedit = QLineEdit()
#         layout.addWidget(lineedit,0,0)
#         lineedit.setPlaceholderText("Name")
#         lineedit.returnPressed.connect(self.press)
#         lineedit2 = QLineEdit()
#         layout.addWidget(lineedit2,1,0)
#         lineedit2.setPlaceholderText("Family name")
#         lineedit2.returnPressed.connect(self.press)
#         label = QLabel("label")
#         layout.addWidget(label)
#         lineedit.setMaxLength(6)
#         lineedit2.setMaxLength(8)
        
#     def press(self):
#         label.setText("Fullname of user is : " + lineedit.text() + " " + lineedit2.text())
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


#_________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global label,textedit
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,500)
#         textedit = QTextEdit()
#         textedit.setPlaceholderText("Describe yourself : ")
#         textedit.textChanged.connect(self.press)
#         layout.addWidget(textedit,0,0)
#         label = QLabel("press enter ro show the text")
#         layout.addWidget(label)
#         button = QPushButton("undo")
#         layout.addWidget(button)
#         button.clicked.connect(self.clickundo)
#         button2 = QPushButton("redo")
#         layout.addWidget(button2)
#         button2.clicked.connect(self.clickredo)
        
        
#     def press(self):
#         label.setText(textedit.toPlainText())
        
#     def clickundo(self):
#         textedit.undo()
        
#     def clickredo(self):
#         textedit.redo()
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#_________________________________________


# class Window(QWidget):
    
#     def __init__(self):
#         global gif,splashscreen,button,giflabel2,gif2,progress,giflabel
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(1280,600)
#         self.setStyleSheet("background-color: White;")
#         splashscreen = QSplashScreen(QPixmap("C:/Users/MZZ/Desktop/MZZ's/Personal img/unnamed.jpg"))
#         giflabel = QLabel()
#         gif = QMovie("C:/Users/MZZ/Desktop/Wow-gif.gif")
#         giflabel.setMovie(gif)
#         gif.start()
#         layout.addChildWidget(giflabel)
#         giflabel.setGeometry(QRect(200,100,600,300))
#         giflabel2 = QLabel()
#         gif2 = QMovie("C:/Users/MZZ/Desktop/22.gif")
#         giflabel2.setMovie(gif2)
#         gif2.stop()
#         giflabel2.hide()
#         layout.addChildWidget(giflabel2)
#         giflabel2.setGeometry(QRect(200,10,800,500))
#         layout.addWidget(splashscreen)
#         progress = QProgressBar(splashscreen)
#         progress.setGeometry(QRect(450,500,450,30))
#         progress.setMaximum(10)
#         splashscreen.hide()
#         button = QPushButton("Start Windows")
#         button.clicked.connect(self.click)
#         button.setGeometry(QRect(520,400,300,100))
#         layout.addChildWidget(button)
#         button.setStyleSheet("background-color: blue;")
        
#     def click(self):
#         value = 0
#         gif.stop()
#         giflabel.hide()
#         splashscreen.show()
#         button.hide()
#         while(value<11):
#             sleep(1)
#             value += 1
#             progress.setValue(value)
#             app.processEvents()
#         splashscreen.finish(self)
#         giflabel2.show()
#         gif2.start()

        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#_________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         mb = QMessageBox()
#         layout.addWidget(mb)
#         mb.setStandardButtons(QMessageBox.Ok | QMessageBox.Reset)
#         mb.setText("# WARNING! ")
#         mb.setInformativeText("This application cannot be installed on Windows.")
#         mb.setIcon(QMessageBox.Critical)

        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#_________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global wizard
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         button = QPushButton("Launch")
#         button.clicked.connect(self.click)
#         layout.addWidget(button)
#         button2 = QPushButton("Back")
#         button2.clicked.connect(self.click2)
#         layout.addWidget(button2)
#         wizard = QWizard()
#         w = QWizardPage()
#         w2 = QWizardPage()
#         wizard.setPage(1,w)
#         w.setTitle("This is page 1")
#         w.setSubTitle("faradars")
#         wizard.setPage(2,w2)
#         w2.setTitle("This is page 2")
        
#     def click(self):
#         wizard.open()
    
#     def click2(self):
#         wizard.restart()

        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#_________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global label,clipboard
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,600)
#         clipboard = QApplication.clipboard()
#         clipboard.setText("Faradars")
#         label = QLabel("text")
#         layout.addWidget(label)
#         clipboard.dataChanged.connect(self.clipboard)
#         label.setStyleSheet("color: red")
        
#     def clipboard(self):
#         label.setText(clipboard.text())
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())