from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


# class Window(QWidget):
    
#     def __init__(self):
#         global label1,label2
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         menubar = QMenuBar()
#         layout.addWidget(menubar,0,0)
#         new = menubar.addMenu("File")
#         new.addAction("Create new file")
#         new.triggered.connect(self.on_click)
#         new.addSeparator()
#         new.addAction("Create new project")
#         new.addSeparator()
#         new.addAction("Settings")
#         new.addSeparator()
#         new.addAction("Exit")
#         new2 = menubar.addMenu("Help")
#         newaction = QAction(QIcon("C:/Users/MZZ/Desktop/MZZ's/Personal img/unnamed.jpg"),"About us",self)
#         newaction.setShortcut("Ctrl+N")
#         newaction.triggered.connect(self.newcall)
#         new2.addAction(newaction)
#         label1 = QLabel("New file created")
#         layout.addWidget(label1,2,0)
#         label1.hide()
#         label2 = QLabel("Fradars (PYQT5)")
#         # layout.addWidget(label2)
#         label2.hide()
    
#     def on_click(self):
#         label1.show()
#         print("OK")
        
#     def newcall(self):
#         label2.resize(300,300)
#         label2.show()
#         print("OK")
        

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


#_______________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         label1 = QLabel("PYQT5")
#         label2 = QLabel("Faradrs")
#         button = QPushButton("button")
#         tabwidget = QTabWidget()
#         layout.addWidget(tabwidget)
#         tabwidget.addTab(label1,"Tab1")
#         tabwidget.addTab(label2,"Tab2")
#         tabwidget.addTab(button,"Tab Button")        
#         button.setGeometry(QRect(200,200,200,200))
#         button.setMaximumWidth(200)
#         tabwidget.setTabsClosable(True)
#         tabwidget.setMovable(True)
#         tabwidget.setTabPosition(QTabWidget.South)

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


#_______________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(900,600)
#         tabbar = QTabBar()
#         tabbar.addTab("Tab 1")
#         tabbar.addTab("Tab 2")
#         tabbar.addTab("Tab 3")
#         tabbar.addTab("button")
#         layout.addChildWidget(tabbar)
#         tabbar.setGeometry(QRect(50,50,350,50))
#         tabbar.setMovable(True)
#         tabbar.setTabsClosable(True)
#         button = QPushButton("button")
#         layout.addChildWidget(button)
#         button.setGeometry(QRect(200,150,170,80))
#         button.clicked.connect(self.on_click)
        
#     def on_click(self):
#         exit()

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


#_______________________________________________


# class Window(QWidget):
    
#     def __init__(self):
#         global stackedwidget
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(700,600)
#         stackedwidget = QStackedWidget()
#         layout.addChildWidget(stackedwidget)
#         stackedwidget.setGeometry(QRect(400,200,200,200))
#         label = QLabel("Faradars")
#         stackedwidget.addWidget(label)
#         label2 = QLabel("setting")
#         stackedwidget.addWidget(label2)
#         label3 = QLabel("Exit")
#         stackedwidget.addWidget(label3)
#         button = QPushButton("Main")
#         button2 = QPushButton("Setting")
#         button3 = QPushButton("Exit")
#         layout.addChildWidget(button)
#         layout.addChildWidget(button2)
#         layout.addChildWidget(button3)
#         button.setGeometry(QRect(30,100,100,100))
#         button2.setGeometry(QRect(30,250,100,100))
#         button3.setGeometry(QRect(30,400,100,100))
#         button.clicked.connect(self.on_click1)
#         button2.clicked.connect(self.on_click2)
#         button3.clicked.connect(self.on_click3)
        
#     def on_click1(self):
#         stackedwidget.setCurrentIndex(0)
        
#     def on_click2(self):
#         stackedwidget.setCurrentIndex(1)
        
#     def on_click3(self):
#         stackedwidget.setCurrentIndex(2)


# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


#_______________________________________________


# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         dockwidget = QDockWidget()
#         layout.addWidget(dockwidget)
#         button = QPushButton("button 1")
#         dockwidget.setWidget(button)
#         dockwidget2 = QDockWidget()
#         layout.addWidget(dockwidget2)
#         button2 = QPushButton("button 2")
#         dockwidget2.setWidget(button2)
#         label = QLabel("Faradars")
#         dockwidget.setTitleBarWidget(label)
#         dockwidget2.setWindowTitle("This is a push button")

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


#_______________________________________________


# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QFormLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         button = QPushButton("button 1")
#         layout.addRow("formlayout" ,button)
#         layout.setVerticalSpacing(200)
#         layout.setHorizontalSpacing(200)
#         button2 = QPushButton("button 2")
#         layout.insertRow(2,"formlayout2",button2)

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#_______________________________________________


# class Window(QWidget):
    
#     def __init__(self):
#         global combobox,button
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         combobox = QComboBox()
#         combobox.addItem("python")
#         combobox.addItem("C++")
#         combobox.addItem("java")
#         layout.addWidget(combobox)
#         combobox.currentTextChanged.connect(self.comboboxchanged)
#         button = QPushButton("show popup")
#         layout.addWidget(button)
#         button.clicked.connect(self.buttonclicked)
#         button.hide()
#         combobox.setEditable(True)
#         combobox.setMaxVisibleItems(2)


#     def comboboxchanged(self):
#         text = combobox.currentText()
#         print(text)
#         if text == "java":
#             button.show()
#         else:
#             button.hide()
            
#     def buttonclicked(self):
#         combobox.showPopup()
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())