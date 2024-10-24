from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys



# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         toolbar = QToolBar()
#         layout.addWidget(toolbar)
#         toolbutton1 = QToolButton() 
#         toolbutton1.setText("button1")
#         toolbutton1.setCheckable(True)
#         toolbar.addWidget(toolbutton1)
#         toolbutton2 = QToolButton()
#         toolbutton2.setText("button2")
#         toolbutton2.setCheckable(True)
#         toolbar.addWidget(toolbutton2)
#         toolbar.setOrientation(Qt.Vertical)
#         toolbar.addSeparator()
#         button = QPushButton("push button")
#         layout.addWidget(button)

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#______________________________


# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,600)
#         toolbox = QToolBox()
#         layout.addWidget(toolbox)
#         label = QLabel()
#         toolbox.addItem(label,QIcon("C:/Users/MZZ/Desktop/MZZ's/Personal img/unnamed.jpg"),"python")
#         label = QLabel()
#         toolbox.addItem(label,"C++")
#         toolbar = QToolBar()
#         button = QPushButton("button1")
#         toolbar.addWidget(button)
#         button = QPushButton("button2")
#         toolbar.addWidget(button)
#         toolbox.insertItem(0,toolbar,"button")
#         print(toolbox.count())
#         toolbutton = QToolButton()
#         toolbutton.setText("faradars")
#         toolbox.addItem(toolbutton,"tool button")

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())